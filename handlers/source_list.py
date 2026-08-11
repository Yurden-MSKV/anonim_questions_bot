from urllib.parse import urlparse, parse_qs

from aiogram import Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from states.action_state import DeleteSource

router = Router()

@router.message(DeleteSource.waiting_for_link_word)
async def delete_source(message: Message, state: FSMContext):
    await state.update_data(link=message.text)
    user_data = await state.get_data()
    link = user_data["link"]
    parsed_link = urlparse(link)
    query_params = parse_qs(parsed_link.query)
    start_values = query_params.get('start')
    if start_values:
        link_word = start_values[0]
        # TODO: дописать