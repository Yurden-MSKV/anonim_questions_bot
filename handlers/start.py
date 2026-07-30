from datetime import datetime
from zoneinfo import ZoneInfo

from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from keyboards.actions import get_actions_keyboard, ActionCallback
from models import User
from states.action_state import ActionForm

router = Router()


@router.message(Command(commands=["start", "menu"]))
async def cmd_start(message: Message, state: FSMContext):
    tg_user = message.from_user
    now_msk = datetime.now(ZoneInfo("Europe/Moscow"))
    user, created = await User.get_or_create(
        telegram_id=tg_user.id,
        defaults={
            "created_at": now_msk
        }
    )
    if created:
        await message.answer(
            f"Привет, {message.from_user.first_name}! 👋\n"
        )
    else:
        await message.answer(
            f"Привет, {message.from_user.first_name}! 👋\n"
            "Это бот-агрегатор для анонимных сообщений. Заведи несколько источников в одном месте, чтобы не путать, откуда тебе пишут читатели."
        )

    await state.set_state(ActionForm.action_choose)

    await message.answer(
        "Что делаем?",
        reply_markup=get_actions_keyboard()
    )


@router.callback_query(ActionForm.action_choose, ActionCallback.filter())
async def action_chosen(
        callback: CallbackQuery,
        callback_data: ActionCallback,
        state: FSMContext
):
    await state.update_data(chosen_action=callback_data.action_code)
    # await state.set_state(ActionForm.waiting_for_exp)
    await callback.answer()
    if callback_data.action_code == "add":
        await callback.message.edit_text(
            f"Выбрана команда ADD"
        )
    elif callback_data.action_code == "show":
        await callback.message.edit_text(
            "Выбрана команда SHOW"
        )
# @router.message(Command(commands=["help"]))
# @router.message(F.text.lower() == "помощь")
# async def cmd_help(message: Message):
#     await message.answer(
#         f""
#     )
