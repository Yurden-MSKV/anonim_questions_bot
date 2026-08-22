from urllib.parse import urlparse, parse_qs

from aiogram import Router, Bot, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from keyboards.actions import get_edit_keyboard, ActionCallback, back_keyboard
from models import Source, User
from states.action_state import EditSource

router = Router()

async def show_user_sources(message: Message, user_id: int, state: FSMContext):
    user = await User.get(telegram_id=user_id)
    bot_info = await message.bot.get_me()
    source_list = await Source.filter(user=user)

    if source_list:
        answer = "<b>🗂 Твои ссылки:</b>\n\n"
        for source in source_list:
            answer += f"  – {source.name}:\n<code>t.me/{bot_info.username}?start={source.link_word}</code>\n\n"
        answer += "✏️ Для настройки/удаления ссылки — отправь мне её целиком."
        await message.answer(answer)
        await state.set_state(EditSource.waiting_for_link_word)
    else:
        await message.answer("🙂‍↔️ У тебя ещё нет ни одной ссылки. Чтобы создать — жми /start")
        await state.clear()


@router.message(EditSource.waiting_for_link_word)
async def edit_source(message: Message, state: FSMContext):
    if not message.text:
        await message.answer('Это не ссылка.')
        return
    link = message.text.strip()
    if not link.startswith(('http://', 'https://')):
        link = 'https://' + link
    await state.update_data(link=link)
    parsed_link = urlparse(link)
    query_params = parse_qs(parsed_link.query)
    start_values = query_params.get('start')
    if start_values:
        link_word = start_values[0]
        await state.update_data(link_word=link_word)
        user = await User.get(telegram_id=message.from_user.id)
        source = await Source.get_or_none(link_word=link_word).prefetch_related('user')
        owner = source.user
        if not source or (user != owner and user.telegram_id != '791693164'):
            await message.answer(
                f"У тебя нет такой ссылки :))"
            )
            return
        else:
            await message.answer(
                f"Выбрана ссылка <b>[{link_word}]</b>. Что с ней нужно сделать?",
                reply_markup=get_edit_keyboard()
            )
            user_data = await state.get_data()
            print(user_data.get('link_word'))
            await state.set_state(EditSource.edit_action_choose)


@router.callback_query(EditSource.edit_action_choose, ActionCallback.filter())
async def edit_action_chosen(
        callback: CallbackQuery,
        callback_data: ActionCallback,
        state: FSMContext
):
    # await state.update_data(chosen_action=callback_data.action_code)
    await callback.answer()

    if callback_data.action_code == "add_new_recipient":
        await callback.message.edit_text(
            f"Один источник может присылать анонимки нескольким получателям.\n\nЧтобы добавить пользователя в группу, "
            f"попроси его написать тебе по нужной ссылке и <b>ответом</b> (↩️) напиши команду /add.",
            reply_markup=back_keyboard()
        )
        await state.set_state(EditSource.back_action)

    elif callback_data.action_code == "edit_name":
        await callback.message.edit_text(
            f"Введи новое название:",
            reply_markup=back_keyboard()
        )
        await state.set_state(EditSource.edit_name)

    elif callback_data.action_code == "edit_link":
        await callback.message.edit_text(
            f"Введи новую фразу для ссылки:",
            reply_markup=back_keyboard()
        )
        await state.set_state(EditSource.edit_link)

    elif callback_data.action_code == "delete_source":
        user_data = await state.get_data()
        link_word = user_data.get('link_word')
        source = await Source.get(link_word=link_word)
        await source.delete()
        await callback.message.edit_text(f'✅ Ссылка <b>[{link_word}]</b> удалена!')
        await state.clear()
        await show_user_sources(callback.message, callback.from_user.id, state)

    elif callback_data.action_code == "back_to_links":
        await state.clear()
        await show_user_sources(callback.message, callback.from_user.id, state)


@router.message(EditSource.edit_name)
async def get_new_name(message: Message, state: FSMContext):
    if not message.text:
        await message.answer(
            f"Нужно ввести текст. Попробуй ещё раз:",
            reply_markup=back_keyboard()
        )
        return

    new_name = message.text

    user_data = await state.get_data()
    link_word = user_data.get('link_word')
    source = await Source.get(link_word=link_word)

    source.name = new_name
    await source.save()

    await message.answer(
        f"Сохранено новое название: <b>«{new_name}»</b>."
    )

    await message.answer(
        f"Выбрана ссылка <b>[{link_word}]</b>. Что с ней нужно сделать?",
        reply_markup=get_edit_keyboard()
    )
    await state.set_state(EditSource.edit_action_choose)


@router.message(EditSource.edit_link)
async def get_new_link(message: Message, state: FSMContext):
    if not message.text:
        await message.answer(
            f"Нужно ввести текст. Попробуй ещё раз:",
            reply_markup=back_keyboard()
        )
        return

    new_link = message.text

    user_data = await state.get_data()
    link_word = user_data.get('link_word')
    source = await Source.get(link_word=link_word)

    source.link_word = new_link
    await source.save()

    await state.update_data(link_word=new_link)

    await message.answer(
        f"Сохранена новая ссылка для источника: <b>«{new_link}»</b>."
    )

    await message.answer(
        f"Выбрана ссылка <b>[{new_link}]</b>. Что с ней нужно сделать?",
        reply_markup=get_edit_keyboard()
    )
    await state.set_state(EditSource.edit_action_choose)


@router.callback_query(
    StateFilter(EditSource.back_action, EditSource.edit_name, EditSource.edit_link),
    ActionCallback.filter(F.action_code == "back")
)
async def back_action_chosen(
        callback: CallbackQuery,
        callback_data: ActionCallback,
        state: FSMContext
):
    # await state.update_data(chosen_action=callback_data.action_code)
    await callback.answer()

    user_data = await state.get_data()
    link_word = user_data.get('link_word')

    if callback_data.action_code == "back":
        await callback.message.edit_text(
            f"Выбрана ссылка <b>[{link_word}]</b>. Что с ней нужно сделать?",
            reply_markup=get_edit_keyboard()
        )
        await state.set_state(EditSource.edit_action_choose)
