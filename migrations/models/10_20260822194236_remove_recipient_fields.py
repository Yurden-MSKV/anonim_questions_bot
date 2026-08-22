from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "anonymous_messages" DROP CONSTRAINT IF EXISTS "fk_anonymou_users_dc79614c";
        ALTER TABLE "anonymous_messages" DROP COLUMN "recipient_id";
        ALTER TABLE "anonymous_messages" DROP COLUMN "msg_id_in_recipient_chat";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "anonymous_messages" ADD "recipient_id" BIGINT;
        ALTER TABLE "anonymous_messages" ADD "msg_id_in_recipient_chat" BIGINT;
        ALTER TABLE "anonymous_messages" ADD CONSTRAINT "fk_anonymou_users_dc79614c" FOREIGN KEY ("recipient_id") REFERENCES "users" ("id") ON DELETE CASCADE;"""


MODELS_STATE = (
    "eJztmm1v4jgQgP9KlE89qVfRtLRdtDopUHrLbYFToXenXa0sk5hgNbGp7WwX9fjvKzvvId"
    "CmheX1E2E849jP+GXGzrPuURu5/MQklGCvjTiHDtJr2rNOoCcfihWONR2Ox0mxFAg4cJUF"
    "JJRMPOpz4AXqqhgOuGDQEnpNG0KXo2NNtxG3GB4LTIle04jvulJILS4YJk4i8gl+9BEQ1E"
    "FihJhe075+O9Z0TGz0A/Ho7/gBDDFy7UzrsS3freRATMZKVsdOi4gbpStfOAAWdX2PJPrj"
    "iRhREhtgIqTUQQQxKJB8g2C+7IFsYNjtqFNBYxOVoJUpGxsNoe+KVI8HIJHpAHS6fdBr9g"
    "HQSzCyKJF8MRESyLOuvPj7B8M4O7s0KmcXV9Xzy8vqVeXqWNNVe2eLLqdBYxJaQVWKWevP"
    "VqcvG0QZtAI/S8FU2UABAyvljIQ+QxYeYyTbNOMFkzE4KXZC1iznDBfzGW9E7FPuCGHH3o"
    "hUEnckozBm/zzVV+SPF9F+/aZYJuwk1Flqf/W6nWJokX4Ol40tof2vrZLax6FPLAlEG/jY"
    "FZjwE/nWP9bAUuKRNXucP7pS0PnHvGt8Mu+O2uZ/v2WHb6dx260rYpQLh6laVAX1nCc87g"
    "BsA0wAR8RGDFgjKMotK3OreHmlWZKXdmStSbwSgiy7wGfMDvTfTJ/6zELl6afN3kR/Zpvd"
    "G/wyxhk+FO6zwaCedcUNZQg75DMKNtoW4QISCxXAD6O8ex5Us11TIMSZSJMmMvgUR4XZuU"
    "8JsJGLhOp+r9nXOve3t3rBIF8C1l5c0ZaN7leTTc/rDNmG2WuY101dDd8BtB6eILNBZhzL"
    "EmrQnCTWnS3yDC8vgQQ6Co/sh2x1lnxBQpP4ZH4mE3TrkL7safqifmf4N0aQFdOP9HP8uW"
    "BbOPV1D/4ALiKOGOk1rVpZQDeKsauVfIgdlhiqKBtBuJg8gCfK7DKEM0bLwbzecb5iyBZD"
    "EgUoyleuoUACe6iYdNYyn1SGpifRw/bFDDpD0O4SdxI2bQH5fqvd7PXN9t+ZzPLa7Ddlia"
    "Gkk5z06CLnpbgS7d9W/5Mm/2pfup1mPgGN9fpfZDCiQ19QQOgTgHZqcEbSiNrh5GAjTw58"
    "/oYMNWV0yJCWlSFJqL8uP9rWMD419MoG8an4OnXonxv1oeXN5zvkQtWJuaRn7ht2BPl0pd"
    "nOhAvk9QQMZ14+5UkVL857lCKPFQ+5z97lPmopsKgf8Cu5e8V2hw3sfRvYeg5N1C5XsH5E"
    "u9/8hUN6/7Bk7OmSIZCLHAa90hFvznA5i8beOOSQ7e91to85gJbA3wtOKuuUugiSOWtf2i"
    "7n8QGl7qo26mga/uKPLLrd24xD663cdOrct+vNu6NT5Un+6GIxZ5YdjlfWebxSIkTK3I8K"
    "sJ68dMMWwrlp6ey95ztB7dyd50ozdxMxbI0KP7wMShZ/cZnobEzcvS9Bt3F6fnl+dXZxHo"
    "d2sWRRRPdyOP0dMR7OsNdej6VMdvAO0qhWX3E/ZlSrcy/IVFl2N5eTqgThUH0H6Z5WXnP7"
    "eFqZf/2oynIZCSUCFR0hzQ+XUibvipg2jfZ0s4Kj5W9m059dV2CG"
)
