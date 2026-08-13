from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "sources" ADD "data" JSONB;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "sources" DROP COLUMN "data";"""


MODELS_STATE = (
    "eJztmu9v2jgYx/+VKK82qVdRWtoeOk1ilG7cWjiV7DbtdLJM8hCsJjaznbWox/9+spOQHw"
    "QKjFIGeQU89uPYn6/jPM8TnkyfOeCJ4wZllPi3IAR2wawbTybFvvpS3OHIMPFolDQrg8R9"
    "T3tgyujYZ4FAfthdN+O+kBzb0qwbA+wJODJMB4TNyUgSRs26QQPPU0ZmC8kJdRNTQMn3AJ"
    "BkLsghcLNu/PPvkWES6sAjiPjn6B4NCHhOZvbEUdfWdiTHI217T9w2lde6r7pgH9nMC3ya"
    "9B+N5ZDRqQOhUlldoMCxBHUFyQO1AjXBaNnxosLJJl3CWaZ8HBjgwJOpFfdRYjMR6nQt1G"
    "tZCJkrMLIZVXwJlQrIk6lV/O33avX09KJaOT2/rJ1dXNQuK5dHhqnnO9t0MQknk9AKh9LM"
    "2h/aHUtNiHFshzorw0T7YIlDLy1GQl/Co5zlb8HjHPpx/xx/IXmef0x7kQCxIVEg2XhbkG"
    "ABTav1VbP0hfjuKUPn78Zd82Pj7s1t4+tb3TKOWm66nQ9x9wR9p3nTfa/hJ7BtDgoOwgXI"
    "r7AESXwoxp71zMF3Itfj+MsSUkQ7/VdQon3b6lmN278yclw1rJZqqWakiK1vzt9m1ZgOYn"
    "xpWx8N9dP41u20NE0mpMv1FZN+1jdTzQkHkiHKHhB20kxic2zKqOwLFxEHEYo42GREgEpk"
    "D4s0X3TMLRrl+cNv9xXf5vFXpI0A6gD/KWFyQ5SqrKtKssNXDQbynmtpsGuPpdcRIdrNqy"
    "qQcStvgbXps4DbsDr9tFu5+VfCrzKSwX1hVBxu6lkprhkH4tJPMNZytKmQmNpQAD/KyT6L"
    "cJhf6xaIcCbWZIocP0xzuOy9zyhywAOpl99rWUbn882NWXzOb4/srm3vZdHmH2wZus1Gr9"
    "m4amXhhkfBBsj2pgPtKdvMoVkMVp0NfWzfP2DuoMwhoVpYleUs076zTX7Vz1swxa7Go9ah"
    "Zp0lX1DbSTSZX9QJl1VWcg60kqM/Z/g3h5gX04/770Ulx/TxI/KAunJo1o1aZQHduI5Tq+"
    "RqBHGFp6qbsuGZR+g9emDcWYVwxmkzmF93n78w5LI8dgjlMXWAzer7Z6/bKdY27p9XldjS"
    "+M/wiHipHNP8YxBQW0ll9APiSULFsbrqO3P7Kis8i8vR+cpzTjk1QL4cHYg18v2UU5lvbi"
    "rfVFDLnOi5uD219VaN2lMBdeqFZ27XR57Xn+7Aw3oRc0nPvGvdE+STl0xv9PYsSG7ibTs/"
    "tVHKl4nNgSY2EjxwOfZXflTlHDfzuDoYQcq4vIzLy7h8W3H5THC4TCzDwQbyA5zMv7jKoG"
    "YmqMm95pSvxGs3D69ncCVF5fVB7d0bhRcNkxvAiT0s/Idn2LL4r51Jn52JlQ8lUK6enF2c"
    "XZ6en03DsallURT2fAj8A7iI7rBli88plz2s8FdrtSWqz9VabW75Wbdl41x1U61AOOq+h3"
    "RPKsvU9k8q84v7ui2XRTAqC1/9zw8xUy4/FWXuGu3JbgWUm3+YTf4HoaeIFA=="
)
