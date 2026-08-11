from aiogram.fsm.state import StatesGroup, State


class ActionForm(StatesGroup):
    action_choose = State()


class AddSource(StatesGroup):
    waiting_for_name = State()
    waiting_for_link_word = State()


class SendAnonymousMessage(StatesGroup):
    waiting_for_text = State()

class DeleteSource(StatesGroup):
    waiting_for_link_word = State()