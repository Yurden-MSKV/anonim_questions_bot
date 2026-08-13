import zoneinfo
from datetime import datetime
from zoneinfo import ZoneInfo

from aiogram import Router, F, Bot
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from keyboards.actions import ActionCallback, get_actions_keyboard, get_blacklist_keyboard
from models import User, Source, AnonimMessage
from states.action_state import ActionForm, AddSource, SendAnonymousMessage, DeleteSource

router = Router()


def now_msk():
    return datetime.now(zoneinfo.ZoneInfo('Europe/Moscow'))


@router.message(CommandStart())
async def cmd_start(message: Message, command: CommandObject, state: FSMContext):
    tg_user = message.from_user
    user, created = await User.get_or_create(
        telegram_id=tg_user.id,
        defaults={
            "created_at": now_msk(),
        }
    )

    link_word = command.args

    if not link_word:
        if created:
            # print(f"Новый пользователь — {message.from_user.first_name}!")
            await message.answer(
                f"👋 Привет, {message.from_user.first_name}! Я помогу тебе получать анонимные вопросы из разных мест!\n\n"
                    f"🗂 Создавай ссылки для блогов, каналов, сайтов — даже если тематики разные, ты не запутаешься!\n\n"
                    f"Попробуй, это удобно!",
                reply_markup=get_actions_keyboard()
            )
        else:
            # print(f"Пользователь {message.from_user.first_name} есть в базе!")
            await message.answer(
                f"Привет, {message.from_user.first_name}! 👋\n\n"
                    f"Что делаем?",
                reply_markup=get_actions_keyboard()
            )
        await state.set_state(ActionForm.action_choose)

    else:
        source = await Source.get_or_none(link_word=link_word).prefetch_related("user")
        if not source:
            await message.answer("⚠️ Источник не существует, или ссылка устарела")
            return
        if source.user.telegram_id == message.from_user.id:
            bot_info = await message.bot.get_me()
            await message.answer(
                "🫵 Это созданная тобой ссылка! Поделись ею с аудиторией :))\n\n"
                f"<code>t.me/{bot_info.username}?start={link_word}</code>"
            )
            return
        await state.update_data(source_id=source.id)

        current_month = datetime.now().strftime("%Y-%m")

        if not source.data:
            source.data = {
                'total_clicks': 0,
                'total_msg': 0,
                'month_key': current_month,
                'month_clicks': 0,
                'month_msg': 0
            }

        last_month = source.data.get('month_key')

        if last_month != current_month:
            source.data['month_key'] = current_month
            source.data['month_clicks'] = 0
            source.data['month_msg'] = 0

        source.data['total_clicks'] += 1
        source.data['month_clicks'] += 1

        await source.save(update_fields=['data'])

        await message.answer(
            f"👋 Привет! Ты перешёл по ссылке /{link_word} для анонимных сообщений.\n\n"
            "✏️ Напиши своё сообщение, получатель не узнает, что оно от тебя!"
        )
        await state.set_state(SendAnonymousMessage.waiting_for_text)



@router.message(SendAnonymousMessage.waiting_for_text)
async def process_message(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(text=message.text)
    user_data = await state.get_data()
    sender = await User.get(telegram_id=message.from_user.id)
    source = await Source.get(id=user_data['source_id']).prefetch_related('user')
    recipient = source.user

    sent_message = await bot.send_message(
        chat_id=recipient.telegram_id,
        text=(
            f"📩 <b>Новая анонимка!</b>\n"
            f"📫 <b>Источник:</b> {source.name}\n\n"
            f"<blockquote>{message.text}</blockquote>\n\n"
            f"Ты можешь ответить человеку или уточнить вопрос прямо здесь — просто свайпни или ПКМ → Ответить"
        ),
        reply_markup=get_blacklist_keyboard()
    )

    await AnonimMessage.create(
        sender=sender,
        recipient=recipient,
        source=source,
        text=user_data['text'],
        created_at=now_msk(),
        msg_id_in_recipient_chat=sent_message.message_id
    )

    current_month = datetime.now().strftime("%Y-%m")

    if not source.data:
        source.data = {
            'total_clicks': 0,
            'total_msg': 0,
            'month_key': current_month,
            'month_clicks': 0,
            'month_msg': 0
        }

    last_month = source.data.get('month_key')

    if last_month != current_month:
        source.data['month_key'] = current_month
        source.data['month_clicks'] = 0
        source.data['month_msg'] = 0

    source.data['total_msg'] += 1
    source.data['month_msg'] += 1

    await source.save(update_fields=['data'])

    await message.answer(
        f"✅ Твоё сообщение отправлено!\n\nТы можешь сделать себе такую ссылку и получать анонимные вопросы — /start"
    )

    await state.clear()


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
        user = await User.get(telegram_id=callback.from_user.id)
        bot_info = await callback.bot.get_me()
        source_list = await Source.filter(user=user)
        if source_list:
            answer = "<b>🗂 Твои ссылки:</b>\n\n"
            for source in source_list:
                answer += f"  – {source.name}:\n<code>t.me/{bot_info.username}?start={source.link_word}</code>\n\n"
            answer += f"🗑 Если нужно удалить ссылку — отправь мне её целиком."
            await callback.message.edit_text(
                answer
            )
            await state.set_state(DeleteSource.waiting_for_link_word)

        else:
            await callback.message.edit_text(
                f"🙂‍↔️ У тебя ещё нет ни одной ссылки. Чтобы создать — жми /start"
            )


@router.message(AddSource.waiting_for_name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(AddSource.waiting_for_link_word)
    await message.answer("А теперь введи именную фразу для ссылки (латиницей, вместо пробелов — подчёркивание (_).\n\nНапример: vlad_vopros")


@router.message(AddSource.waiting_for_link_word)
async def process_link_word(message: Message, state: FSMContext):
    link_word = message.text.strip()

    exists = await Source.filter(link_word=link_word).exists()
    if exists:
        await message.answer(
            "Эта ссылка уже занята другим источником!\n\nПопробуй вести другую фразу."
        )
        return

    user_data = await state.get_data()
    user = await User.get(telegram_id=message.from_user.id)
    source = await Source.create(
        user=user,
        name=user_data["name"],
        link_word=message.text,
        created_at=now_msk(),
    )

    await state.clear()

    bot_info = await message.bot.get_me()
    await message.answer(
        f"✅ <b>Источник «{source.name}» успешно создан!</b>\n\n"
        f"🔗 Твоя ссылка:\n<code>t.me/{bot_info.username}?start={source.link_word}</code>\n\n"
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
