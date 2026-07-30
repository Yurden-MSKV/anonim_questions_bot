from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


class ActionCallback(CallbackData, prefix="action"):
    action_code: str

def get_actions_keyboard():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="📝Добавить источник",
        callback_data=ActionCallback(action_code="add")
    )

    builder.button(
        text="🔎Посмотреть источники",
        callback_data=ActionCallback(action_code="show")
    )

    builder.adjust(1)
    return builder.as_markup()