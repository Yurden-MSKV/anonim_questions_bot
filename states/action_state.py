from aiogram.fsm.state import StatesGroup, State


class ActionForm(StatesGroup):
    action_choose = State()


class AddSource(StatesGroup):
    waiting_for_name = State()
    waiting_for_link_word = State()


class SendAnonymousMessage(StatesGroup):
    waiting_for_text = State()


class EditSource(StatesGroup):
    waiting_for_link_word = State()
    edit_action_choose = State()
    back_action = State()
    edit_name = State()
    edit_link = State()