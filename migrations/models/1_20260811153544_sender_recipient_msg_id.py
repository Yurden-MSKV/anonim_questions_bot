from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "anonymous_messages" DROP CONSTRAINT IF EXISTS "fk_anonymou_users_436d2186";
        ALTER TABLE "anonymous_messages" RENAME COLUMN "user_id" TO "sender_id";
        ALTER TABLE "anonymous_messages" ADD "msg_id_in_recipient_chat" BIGINT;
        ALTER TABLE "anonymous_messages" ADD "recipient_id" BIGINT NOT NULL;
        ALTER TABLE "anonymous_messages" ADD CONSTRAINT "fk_anonymou_users_85c748cd" FOREIGN KEY ("sender_id") REFERENCES "users" ("id") ON DELETE CASCADE;
        ALTER TABLE "anonymous_messages" ADD CONSTRAINT "fk_anonymou_users_dc79614c" FOREIGN KEY ("recipient_id") REFERENCES "users" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "anonymous_messages" DROP CONSTRAINT IF EXISTS "fk_anonymou_users_dc79614c";
        ALTER TABLE "anonymous_messages" DROP CONSTRAINT IF EXISTS "fk_anonymou_users_85c748cd";
        ALTER TABLE "anonymous_messages" RENAME COLUMN "sender_id" TO "user_id";
        ALTER TABLE "anonymous_messages" DROP COLUMN "msg_id_in_recipient_chat";
        ALTER TABLE "anonymous_messages" DROP COLUMN "recipient_id";
        ALTER TABLE "anonymous_messages" ADD CONSTRAINT "fk_anonymou_users_436d2186" FOREIGN KEY ("user_id") REFERENCES "users" ("id") ON DELETE CASCADE;"""


MODELS_STATE = (
    "eJztmm1z2jgQx7+Kx6/amVyHOCGkvKOEtFwb6ATurtObG42wN0YTW6KSnIRJ+e43km2EjX"
    "lwhrQJ+BWw2pWl3wrp77Uf7ZB5EIh3LcooCa9ACOyD3bQebYpD9aXY4ciy8WRimpVB4lGg"
    "IzBldBqySKAwdtfNeCQkx660m9YNDgQcWbYHwuVkIgmjdtOiURAoI3OF5IT6xhRR8iMCJJ"
    "kPcgzcblr//ndk2YR68AAi/Tm5RTcEAi8zeuKpa2s7ktOJtn0gfpfKS+2rLjhCLguikBr/"
    "yVSOGZ0HECqV1QcKHEtQV5A8UjNQA0ymnU4qHqxxiUe5EOPBDY4CuTDjETI2G6Fef4gGnS"
    "FCdglGLqOKL6FSAXm0dRb/eO84JycNp3Zydl4/bTTq57XzI8vW411uasziwRhacVeaWfdj"
    "tzdUA2Icu3GelWGmY7DEcZROhqEv4UEu8x/Cwwr6qX+Ov5A8zz+lvS4BqcFkwCy8X5CCNT"
    "SHnW+aZSjEj0AZen+3rtufWtdvrlrf3uqWadLypd/7mLob9L32l/4HDd/AdjkoOAgXIL/A"
    "EiQJoRh7NjIH30tC36VftkhFstJfQya6V53BsHX1NZOOi9awo1qcTCpS65uzt9lszDux/u"
    "kOP1nqp/W93+tomkxIn+srGr/hd1uNCUeSIcruEfYWmaTm1JTJcih8RDxEKOLgkgkBKpE7"
    "Lsr5um1uXS+bN7+Xn/Ffuf2Z3BiWZY+dfOSTcvDSNsDfkwQB1ANeOgOZsAr/0/GziLtQHv"
    "9iWIW/FH4lfm9uCwVYvKqXU3HJOBCffoapTkeXCompCwXwE/n/l4i7eWVJSHgaqzmqOL6f"
    "3y9k//2MIg8CkHr+7dag3bro2MUbfUV2E9n8ybYZbrwV7IDsYN7RnrLNbJrFYNXeMMLu7T"
    "3mHspsEqqFOSxnmfsuN4VOmLdgin2NR81DjTpLvqCMYHKyun4QT6sqGhxo0UB/LvFvjzEv"
    "pp/670XRwA7xAwqA+nJsN616bQ3dtGRQr+VuR9NigqObsvIsIPQW3TPulSGcCdoN5t+7zp"
    "8ZclWJOYRKTCSecJu5EFTd5ezqLkdBrZT4JrW4sPTKasUFGbfwRCe36pPIy8/XEGA9iZWk"
    "lx4m7Qny2XOKar08CyR1umxXC2qV+UpOH6iclhCAz3FY+qjKBe7muDqYhFRqcP/V4JIk2e"
    "YE5eACuQMv83JEdZQuHaW5Zzqy4lWCl6mgPZ3U3pVPn1WdtYATd1z45lTcsv6VKePzYiTa"
    "oegz5/i0cXp+cnY6VwFzy7rDf7PyugMukn/YtpW2hZA9LGc69foWpTanXl9Za9NtWXml/l"
    "QlCCfue0j3uLZNIfO4trqSqdty4pVRWfic889Bv7dCtZqQvGQlrrR+WgERr7HUNVsNV8HI"
    "CNWl9/nyr+7lFKjqQL3PV0JR7v4wm/0P8wUP0w=="
)
