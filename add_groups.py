import asyncio

from aiogram import Bot

from models import Source


async def add_groups_in_sources(bot: Bot):
    sources = await Source.all().prefetch_related('user')
    print(f"Загружено источников: {len(sources)}")

    for source in sources:
        user_id = source.user.telegram_id
        try:
            group = source.data.setdefault('user_group', [])
            if user_id not in group:
                group.append(user_id)
                await source.save(update_fields=['data'])
                print("Группа добавлена!")
            else:
                print("Группа уже существует, и создатель в ней состоит.")

        except:
            print(f"[{source.link_word}] — что-то пошло не так.")

        await asyncio.sleep(0.05)