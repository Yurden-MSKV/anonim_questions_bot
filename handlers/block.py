from aiogram import Router, F, Bot
from aiogram.filters import ChatMemberUpdatedFilter, MEMBER, KICKED
from aiogram.types import ChatMemberUpdated

from models import SystemStats

router = Router()


@router.my_chat_member(
    ChatMemberUpdatedFilter(member_status_changed=MEMBER >> KICKED)
)
async def user_blocked_bot(event: ChatMemberUpdated):
    stats = await SystemStats.get(id=1)
    stats.user_count -= 1
    await stats.save()


@router.my_chat_member(
    ChatMemberUpdatedFilter(member_status_changed=KICKED >> MEMBER)
)
async def user_unblocked_bot(event: ChatMemberUpdated):
    stats = await SystemStats.get(id=1)
    stats.user_count += 1
    await stats.save()
