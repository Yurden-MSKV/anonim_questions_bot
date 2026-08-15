from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "systemstats" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "user_count" BIGINT NOT NULL
);
        ALTER TABLE "sources" ALTER COLUMN "created_at" TYPE TIMESTAMPTZ USING "created_at"::TIMESTAMPTZ;
        ALTER TABLE "users" ALTER COLUMN "created_at" TYPE TIMESTAMPTZ USING "created_at"::TIMESTAMPTZ;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" ALTER COLUMN "created_at" TYPE TIMESTAMPTZ USING "created_at"::TIMESTAMPTZ;
        ALTER TABLE "sources" ALTER COLUMN "created_at" TYPE TIMESTAMPTZ USING "created_at"::TIMESTAMPTZ;
        DROP TABLE IF EXISTS "systemstats";"""


MODELS_STATE = (
    "eJztWm1v4jgQ/itRPu1KvYqmpfTQaSWW0l1uWziV7O1qTyfLJCZYTWzWdrZFPf77yU5CXg"
    "gpobRQyKfSeXHs53HGM+M86h61kcuPW4QS7N0gzqGD9Kb2qBPoyR/5BkeaDieTWC0FAg5d"
    "5QEJJVOP+hx4gblSwyEXDFpCb2oj6HJ0pOk24hbDE4Ep0Zsa8V1XCqnFBcPEiUU+wT99BA"
    "R1kBgjpje1f/490nRMbPSAePTv5A6MMHLt1OyxLZ+t5EBMJ0r2ETtdIq6UrXzgEFjU9T0S"
    "20+mYkzJ3AETIaUOIohBgeQTBPPlCuQEw2VHiwomG5sEs0z42GgEfVckVjwEsUwHoNc3wa"
    "BjAqCXwMiiROKLiZCAPOqKxd9+N4zT04ZROz2/qJ81GvWL2sWRpqv5Lqoas2AyMVrBUAqz"
    "7qduz5QTogxaAc9SMFM+UMDAS5ERoy/Qg1jE30QPS9CP7DP4c8Gy+EdoFxEQCWIG4o33Ch"
    "QUoGl2vissPc5/ulLQ+7t12/7cun130/r+Xmmmoea63/sUmcfQ99rX/Y8K/BhsiyEJDoA5"
    "kF9CgQT2UD7sac8M+Hboehz9WIGKcKe/BSa6N52B2br5K0XHZcvsSI2RoiKSvjt/n2ZjPo"
    "j2rWt+1uS/2o9+r6PQpFw4TD0xtjN/6HJO0BcUEHoPoJ3EJBJHohTLHncAtgEmgCELTzAi"
    "AljjPM6LwlzRKE8Hv91n/DXDXx43HBEbsWcRkxmiYmVdVuIdXjYZyHquxcGuHUvbISHczW"
    "UZSLlVr8Da6FOfWag8+km3avOXgl9WJKO73Kw42NSLVFxRhrBDvqCpoqNLuIDEQjnghzXZ"
    "Vx4M87ZegRDOWBpPkcH7eQ2XfvcpATZykVDLH3RMrff1+lrPj/Ovh+yube9Voc0ebCl026"
    "1Bu3XZSYMbhIINIDuYD7Sn2KaCZj6wMjYMoXV3D5kNUkFCaqhBM5K57aLKM7ysBBLoKHjk"
    "OuSs08jn9HZiTpY3dYJlVZ2cA+3kqL8L+LfHkOWjH9nvRSdH9+ADcBFxxFhvavVaAbpRH6"
    "dey/QIog6PoVTp9MzF5A7cU2aXQTjltBmYt7vPXxjkqj22FHmGoN0n7jSc2htpl4UoFnbL"
    "ZDxbpPvPQb+XT3VknyUZW0L7T3Mxf6mSU/9j5BNLMqcNfewKTPixfOoH/fV7ohKe4u50th"
    "GdIU4OkO1O+3yN8j/hVJWfmyo/JahVifRUGp/YemWT+ER+nbj/zOz60PPqyy1yoVrEUqQX"
    "rl73BPLZi1Y7Uy6QNxAwfPOyJU9CXVz3KEM+N6xqn4OrfVQosKif11l68vSa+1UH2PMOsO"
    "00TdQplxM/otNveeCQ7Fch40BDhkAuchj0Sme8GcfNBI2DIaSq9qtqv6r2t1TtlzixU5d2"
    "CP9CdupT0apUWiiVMt9SiC3htWOxbDW44pur9YHau2vLFy2+W4hha5z7GXmgKf5+PLbZmd"
    "T5UPJm4+SscXZxen42z87mkqKk7OmM+BdiPHzDVr3hSrjs4TWiUa+vcMVl1OtL77iULp32"
    "ypeqBMKh+R6ie1Jb5QLxpLb8BlHpMkUFJSL3+6LlKWbC5VlZ5q6hPduthHLzh9nsfxGG6s"
    "I="
)
