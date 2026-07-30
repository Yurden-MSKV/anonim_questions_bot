from aiogram import Router
from aiogram.filters import CommandStart, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from handlers.start import cmd_start

router = Router()

@router.message(CommandStart())
async def cmd_start_deeplink(message: Message, command: CommandObject, state: FSMContext):
    link_word = command.args
    if not link_word:
        await state.clear()
        await message.answer("")