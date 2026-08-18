import asyncio
from typing import Any, Awaitable, Callable, Dict, List
from aiogram import BaseMiddleware
from aiogram.types import Message


class AlbumMiddleware(BaseMiddleware):

  def __init__(self, latency: float = 0.2):
    self.latency = latency
    self.storage: Dict[str, List[Message]] = {}
    super().__init__()

  async def __call__(
      self,
      handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
      event: Message,
      data: Dict[str, Any],
  ) -> Any:
    if not event.media_group_id:
      return await handler(event, data)

    if event.media_group_id in self.storage:
      self.storage[event.media_group_id].append(event)
      return

    self.storage[event.media_group_id] = [event]

    await asyncio.sleep(self.latency)

    album = self.storage.pop(event.media_group_id)

    album.sort(key=lambda x: x.message_id)

    data['album'] = album
    return await handler(event, data)
