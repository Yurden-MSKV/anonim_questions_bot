from tortoise import Tortoise
import config


async def init_db():
    await Tortoise.init(
        db_url=config.BASE_URL,
        modules={
            'models': ['models']
        },
        use_tz=False,
    )
    await Tortoise.generate_schemas()

async def close_db():
    await Tortoise.close_connections()