from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "telegram_id" BIGINT NOT NULL UNIQUE,
    "created_at" TIMESTAMPTZ
);
CREATE INDEX IF NOT EXISTS "idx_users_telegra_ab91e9" ON "users" ("telegram_id");
CREATE TABLE IF NOT EXISTS "sources" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(50) NOT NULL,
    "link_word" VARCHAR(50) NOT NULL UNIQUE,
    "created_at" TIMESTAMPTZ,
    "user_id" BIGINT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "anonymous_messages" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "text" TEXT NOT NULL,
    "created_at" TIMESTAMPTZ,
    "source_id" BIGINT NOT NULL REFERENCES "sources" ("id") ON DELETE CASCADE,
    "user_id" BIGINT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztmu9v2jgYx/+VyK82qTfRtJQe7zJKN24rnEq2m3aaLJO4wapjM9tZi3r87yc7CSa/GG"
    "jttgKvgOeHY38ex/7i5AHEPMRUvvIYZyS+wlKiCIOu8wAYivWX+oAjB6DZzLq1QaEJNRmI"
    "cTaPeSJhnIYbN5pIJVCgQNe5QVTiIweEWAaCzBThDHQdllCqjTyQShAWWVPCyNcEQ8UjrK"
    "ZYgK7z75cjBxAW4nss85+zW3hDMA0LvSehvraxQzWfGdtrEg2YujSx+oITGHCaxMzGz+Zq"
    "ytkygTClrRFmWCCF9RWUSPQIdAezYeeDSjtrQ9JeruSE+AYlVK2MeAKtDUA4HPlw3PchBF"
    "swCjjTfAlTGsgDMFX840/XPTnpuK2Ts/P2aafTPm+dHznA9Lfq6izSzlhaaVOG2eDNYOjr"
    "DnGBgrTO2rAwOUihNMsUw9JX+F5V+fv4voF+Hl/iL5Uo889prytAbrAVsBPvJ5RgDU2//8"
    "mwjKX8SrVh+NG77r31rl9ceZ9eGs8887wfDd/k4Rb9sPd+9NrAt7ADgTUciGqQXyCFFYlx"
    "PfZiZgl+mKW+yr9sUIpspj+HSgyu+mPfu/q7UI4Lz+9rj1soRW59cfayWI1lI84/A/+to3"
    "86n0fDvqHJpYqEuaKN8z8D3SeUKA4Zv4MoXGWSm3NTocqSJyLAcNt1rZD2/eXtGdxeP3OF"
    "s/gTicXW8FeSDui3Qq/39Zvb2r1FQ62W4ZILTCL2Ds9NKQZMKsQCXIM+0zUfsmaeWQkymt"
    "ZqV12B7pZCaHXqcQZDTLEyo+9545530Qc1a8sjQB0vG9pRrIXltB6snroTFNzeIRHCwhzW"
    "Hu7ykmUZW3XFbly2IIYig0ePQ/e6SL5GwNuaNCv3dFgHub6nct18Vvj3pkjU08/jd0Kugx"
    "jdQ4pZpKag67Rba+jmYr3dKgnBXMa7xlVUDpSwW3jHRbgN4ULS42D+tfP8iSEf/gPtw3+g"
    "gwg/iPCdEuHNWnFFxq2cpZZmfZZ5+e4aU2QG0Ui6coy7I8gXTymqzfSskdT5tG0W1LryBz"
    "m9p3JaYYojgeKtt6pS4uNsV3tTkIMa3H01WJEkm+ygiNLCE8nDLlrZRaungT9IaudOAp9U"
    "aHhYkGBa+/g99ax/7m5jfhu1sS9Swz0+7Zyen5ydLje0pWXdPvZ9EfENC5ndYZseGq2k7O"
    "DJnNtub3Bq5LbbjcdGxldUCvqm2oJwFr6DdI9bm5zJHbeaD+WMr6TDOFM4vbWLhP8aj4YN"
    "AsymlNUXCZTzn0OJfI6nNotmuBpGQXNVXgopv/9RElO6Af1SyBbi6PE3s8X/Yq82Yw=="
)
