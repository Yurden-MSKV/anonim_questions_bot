from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "anonymous_messages" ADD "msg_id_in_recipient_chat" BIGINT;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "anonymous_messages" DROP COLUMN "msg_id_in_recipient_chat";"""


MODELS_STATE = (
    "eJztmm1v4jgQgP9KlE89qVfRtJQuWp0UWnrLbYFToXenXa0sk5hgNbGp7WwX9fjvKzvvId"
    "CmheX1E2E849jP+GXGzrPuURu5/MQklGCvjTiHDtLr2rNOoCcfihWONR2Ox0mxFAg4cJUF"
    "JJRMPOpz4AXqqhgOuGDQEnpdG0KXo2NNtxG3GB4LTIle14jvulJILS4YJk4i8gl+9BEQ1E"
    "FihJhe175+O9Z0TGz0A/Ho7/gBDDFy7UzrsS3freRATMZK1sBOi4gbpStfOAAWdX2PJPrj"
    "iRhREhtgIqTUQQQxKJB8g2C+7IFsYNjtqFNBYxOVoJUpGxsNoe+KVI8HIJHpAHS6fdBr9g"
    "HQSzCyKJF8MRESyLOuvPj7B8M4O6sZlbOLy+p5rVa9rFwea7pq72xRbRo0JqEVVKWYtf5s"
    "dfqyQZRBK/CzFEyVDRQwsFLOSOgzZOExRrJNM14wGYOTYidkzXLOcDGf8UbEPuWOEHbsjU"
    "glcUcyCmP2z1N9Rf54Ee3Xb4plwk5CnaX2V6/bKYYW6edw2dgS2v/aKql9HPrEkkC0gY9d"
    "gQk/kW/9Yw0sJR5Zs8f5oysFnX/Mu6tP5t1R2/zvt+zw7VzddhuKGOXCYaoWVUEj5wmPOw"
    "DbABMQD0xgjaAot7IsquXl9WZJvtqRFafINxwRG7F3OSZXxcErb/VKCLLs5psxO9B/M33q"
    "MwuVp582exP9mRBob/DL+HP4UBgDBYN61hU3lCHskM8oCIJahAtILFQAP4zA73lQzXZNgR"
    "BnIk2ayOBTHLFn5z4lwEYuEqr7vWZf69zf3uoFg3wJWHtxRVs2ul9NNj2vM2SvzN6Ved3U"
    "1fAdQOvhCTIbZMaxLKEGzUli3dkiz/DyEkigo/DIfshWZ8kXJJuJT+ZnmUG3DqnlnqaW6n"
    "eG/9UIsmL6kX6OPxdsC6e+7sEfwEXEESO9rlUrC+hG+U+1kk9/whJDFWUjCBeTB/BEmV2G"
    "cMZoOZjXO85XDNliSKIARfnKNRRIYA8Vk85a5hP+0PQketi+mEFnCNpd4k7Cpi0g32+1m7"
    "2+2f47k/Vfm/2mLDGUdJKTHl3kvBRXov3b6n/S5F/tS7fTzB8OxHr9LzIY0aEvKCD0CUA7"
    "NTgjaUTtcKqzkac6Pn9DhpoyOmRIy8qQJNRflx9taxifGnplg/hUfJ26kMmN+tDy5vMdcq"
    "HqxFzSM3dBO4J8utJsZ8IF8noChjMvn/KkihfnPUqRx4qH3Gfvch+1FFjUD/iV3L1iu8MG"
    "9r4NbD2HJmqXK1g/ot1v/sIhvX9YMvZ0yRDIRQ6DXumIN2e4nEVjbxxyyPb3OtvHHEBL4O"
    "8FJ5UNSl0EyZy1L22X8/iAUndVG3U0DX/xBzDd7m3GoY1Wbjp17tuN5t3RqfIkf3SxmDPL"
    "Dscr6zxeKREiZe5HBVhPXrphC+HctHT23vOdoHbuznOlmbuJGLZGhR/FBiWLv4ZNdDYm7t"
    "6XoNs4Pa+dX55dnMehXSxZFNG9HE5/R4yHM+y112Mpkx28gzSq1VfcjxnV6twLMlWW3c3l"
    "pCpBOFTfQbqnldfcPp5W5l8/qrJcRkKJQEVHSPPDpZTJuyKmTaM93azgaPmb2fQnw9niMA"
    "=="
)
