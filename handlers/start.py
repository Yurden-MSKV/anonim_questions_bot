from datetime import datetime
from zoneinfo import ZoneInfo

from aiogram import Router, F
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from keyboards.actions import get_actions_keyboard, ActionCallback
from models import User, Source
from states.action_state import ActionForm, AddSource, SendAnonymousMessage

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, command: CommandObject, state: FSMContext):
    tg_user = message.from_user
    now_msk = datetime.now(ZoneInfo("Europe/Moscow"))
    user, created = await User.get_or_create(
        telegram_id=tg_user.id,
        defaults={
            "created_at": now_msk
        }
    )

    link_word = command.args

    if not link_word:

        if created:
            print("Новый пользователь")
            await message.answer(
                f"Привет, {message.from_user.first_name}! 👋\n"
                "Это бот-агрегатор для анонимных сообщений. Заведи несколько источников в одном месте, чтобы не путать, откуда тебе пишут читатели.",
                reply_markup=get_actions_keyboard()
            )
        else:
            print("Пользователь есть в базе")
            await message.answer(
                f"Привет, {message.from_user.first_name}! 👋\n",
                reply_markup=get_actions_keyboard()
            )

        await state.set_state(ActionForm.action_choose)

    source = await Source.get_or_none(link_word=link_word).prefetch_related("user")

    if not source:
        await message.answer("⚠️ Источник не существует, или ссылка устарела")
        return

    if source.user.telegram_id == message.from_user.id:
        bot_info = await message.bot.get_me()
        await message.answer(
            "Это созданная тобой ссылка! Поделись ею с читателями :))\n\n"
            f"t.me/{bot_info.username}?start={link_word}"
        )
        return

    await state.update_data(source_id=source.id)
    await state.set_state(SendAnonymousMessage.waiting_for_text)

    await message.answer(
        f"✍️ Напиши анонимное сообщение, оно упадёт в папку **{source.name}**.\n"
        f"Получатель не узнает, кто его отправил."
    )

@router.callback_query(ActionForm.action_choose, ActionCallback.filter())
async def action_chosen(
        callback: CallbackQuery,
        callback_data: ActionCallback,
        state: FSMContext
):
    await state.update_data(chosen_action=callback_data.action_code)
    await callback.answer()
    if callback_data.action_code == "add":
        await callback.message.edit_text(
            f"Введи название источника."
        )
        await state.set_state(AddSource.waiting_for_name)


    elif callback_data.action_code == "show":
        await callback.message.edit_text(
            "Твои источники"
        )


@router.message(AddSource.waiting_for_name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(AddSource.waiting_for_link_word)
    await message.answer("А теперь введи фразу для ссылки (латиницей, вместо пробелов — подчёркивание (_)")


@router.message(AddSource.waiting_for_link_word)
async def process_link_word(message: Message, state: FSMContext):
    link_word = message.text.strip()

    exists = await Source.filter(link_word=link_word).exists()
    if exists:
        await message.answer(
            "Эта ссылка уже занята другим источником!\nПопробуй вести другую фразу."
        )
        return

    user_data = await state.get_data()
    now_msk = datetime.now(ZoneInfo("Europe/Moscow"))
    source = await Source.create(
        user_id=message.from_user.id,
        name=user_data["name"],
        link_word=message.text,
        created_at=now_msk
    )

    await state.clear()

    bot_info = await message.bot.get_me()
    await message.answer(
        f"✅ **Источник «{source.name}» успешно создан!**\n\n"
        f"🔗 Твоя ссылка:\nt.me/{bot_info.username}?start={source.link_word}\n\n"
        f"Делись этой ссылкой в одном блоге/чате, чтобы не путать источники."
    )

@router.message(SendAnonymousMessage.waiting_for_text)
async def process_anonymous_message(message: Message, state: FSMContext):
    fsm_data = await state.get_data()
    source_id = fsm_data.get("source_id")

    source = await Source.get_or_none(id=source_id).prefetch_related("user")
    if not source:
        await message.answer("Ошибка: источник больше не существует.")
        await state.clear()
        return

    