from datetime import datetime

from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram import Router

from handlers.start import now_msk
from keyboards.actions import ActionCallback
from models import User, Source
from states.action_state import ActionForm, AddSource, EditSource

router = Router()


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
            answer += f"✏️ Для настройки/удаления ссылки — отправь мне её целиком."
            await callback.message.edit_text(
                answer
            )
            await state.set_state(EditSource.waiting_for_link_word)

        else:
            await callback.message.edit_text(
                f"🙂‍↔️ У тебя ещё нет ни одной ссылки. Чтобы создать — жми /start"
            )


@router.message(AddSource.waiting_for_name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(AddSource.waiting_for_link_word)
    await message.answer(
        "А теперь введи именную фразу для ссылки (латиницей, вместо пробелов — подчёркивание (_).\n\nНапример: vlad_vopros")


@router.message(AddSource.waiting_for_link_word)
async def process_link_word(message: Message, state: FSMContext):
    link_word = message.text.strip()

    exists = await Source.filter(link_word=link_word).exists()
    if exists:
        await message.answer(
            "🙂‍↔️ Эта ссылка уже занята другим источником!\n\nПопробуй вести другую фразу."
        )
        return

    user_data = await state.get_data()
    user = await User.get(telegram_id=message.from_user.id)
    current_month = datetime.now().strftime("%Y-%m")
    source = await Source.create(
        user=user,
        name=user_data["name"],
        link_word=message.text,
        created_at=now_msk(),
        data={
            'user_group': [message.from_user.id],
            'total_clicks': 0,
            'total_msg': 0,
            'month_key': current_month,
            'month_clicks': 0,
            'month_msg': 0
        }
    )

    await state.clear()

    bot_info = await message.bot.get_me()
    await message.answer(
        f"✅ <b>Источник «{source.name}» успешно создан!</b>\n\n"
        f"🔗 Твоя ссылка:\n<code>t.me/{bot_info.username}?start={source.link_word}</code>\n\n"
        f"Делись этой ссылкой в одном блоге/чате, чтобы не путать источники."
    )
