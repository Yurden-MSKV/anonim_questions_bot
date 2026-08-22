from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


class ActionCallback(CallbackData, prefix="action"):
    action_code: str


def get_actions_keyboard():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="📝Создать ссылку",
        callback_data=ActionCallback(action_code="add")
    )

    builder.button(
        text="🔎Посмотреть ссылки",
        callback_data=ActionCallback(action_code="show")
    )

    builder.adjust(1)
    return builder.as_markup()


def get_blacklist_keyboard(is_blocked: bool = False) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    if is_blocked:
        builder.button(
            text="🔓Разблокировать",
            callback_data=ActionCallback(action_code="unblock").pack()
        )
    else:
        builder.button(
            text="🚫Заблокировать",
            callback_data=ActionCallback(action_code="block").pack()
        )
    builder.adjust(1)
    return builder.as_markup()


def get_edit_keyboard():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="➕Добавить получателя",
        callback_data=ActionCallback(action_code="add_new_recipient")
    )

    builder.button(
        text="✏️Изменить название",
        callback_data=ActionCallback(action_code="edit_name")
    )

    builder.button(
        text="✏️Изменить ссылку",
        callback_data=ActionCallback(action_code="edit_link")
    )

    builder.button(
        text="🗑Удалить источник",
        callback_data=ActionCallback(action_code="delete_source")
    )

    builder.button(
        text="⬅️Назад к ссылкам",
        callback_data=ActionCallback(action_code="back_to_links")
    )

    builder.adjust(1)
    return builder.as_markup()


def back_keyboard():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="⬅️Назад",
        callback_data=ActionCallback(action_code="back")
    )

    builder.adjust(1)
    return builder.as_markup()
