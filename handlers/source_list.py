from urllib.parse import urlparse, parse_qs

from aiogram import Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from models import Source, User
from states.action_state import DeleteSource

router = Router()

@router.message(DeleteSource.waiting_for_link_word)
async def delete_source(message: Message, state: FSMContext):
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
        user = await User.get(telegram_id=message.from_user.id)
        source = await Source.get_or_none(link_word=link_word).prefetch_related('user')
        owner = source.user
        if not source or (user != owner and user.telegram_id != '791693164'):
            await message.answer(
                f"У тебя нет такой ссылки :))"
            )
        else:
            await source.delete()
            await message.answer(
                f'✅ Ссылка /{link_word} удалена!'
            )
    await state.clear()