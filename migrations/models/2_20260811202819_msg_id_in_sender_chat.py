from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "anonymous_messages" ADD "msg_id_in_sender_chat" BIGINT;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "anonymous_messages" DROP COLUMN "msg_id_in_sender_chat";"""


MODELS_STATE = (
    "eJztml1z2jgUhv+Kx1ftTLZDnBCy3FFCWrYN7AR2t9OdHY2wT4wmtkQluQmT5b/vSLYRNu"
    "bDLGkT8FXIkY4tPa+QXh/8ZIfMg0C8a1FGSXgDQmAf7Kb1ZFMcqg/FHU4sG08mplkFJB4F"
    "OgNTRqchiwQK4+66GY+E5NiVdtO6w4GAE8v2QLicTCRh1G5aNAoCFWSukJxQ34QiSr5FgC"
    "TzQY6B203r739OLJtQDx5BpP9O7tEdgcDLjJ546t46juR0omPvid+l8lr3VTccIZcFUUhN"
    "/8lUjhmdJxAqVdQHChxLUHeQPFIzUANMpp1OKh6s6RKPciHHgzscBXJhxiNkYjZCvf4QDT"
    "pDhOwSjFxGFV9CpQLyZGsVf/nVcc7OGk7t7OKyft5o1C9rlyeWrce73NSYxYMxtOJLaWbd"
    "D93eUA2IcezGOqvATOdgieMsLYahL+FRLvMfwuMK+mn/HH8heZ5/SnudAGnAKGAW3g+QYA"
    "3NYeeLZhkK8S1Qgd6frdv2x9btm5vWl7e6ZZq0fO73PqTdDfpe+3P/vYZvYLscFByEC5Bf"
    "YQmShFCMPZuZg+8lqe/SD1tIkaz016BE96YzGLZufs/IcdUadlSLk5Eijb65eJtVY34R66"
    "/u8KOl/rW+9nsdTZMJ6XN9R9Nv+NVWY8KRZIiyB4S9RSZpOA1lVA6Fj4iHCEUcXDIhQCVy"
    "x0War9vm1l1l8+b38hX/kdtfkTYCqAf8fwmTu0Slyq6qmBVe1gzkM3fS4KUdSz9HhGQ1l1"
    "Ugk1bh3x0/i7gL5fEvplX4S+FXjyR394W2OF7Vy1JcMw7Ep59gquXoUiExdaEAfvJQ9oeI"
    "L/PKREh4mqg5qjh+mD/FZb/9jCIPApB6/u3WoN266tjFG31FdhPZ/Mm2GW68FeyB7GB+oQ"
    "Nlm9k0i8GqvWGE3fsHzD2U2SRUC3NYLjLvu9wUOmE+gin2NR41DzXqLPmC4o7RZHVVJ55W"
    "Vco50lKO/rvEvz3GvJh+2v8gSjl2iB9RANSXY7tp1Wtr6KaFnHotVyRISzyObsras4DQe/"
    "TAuFeGcCZpP5h/7jp/ZshVfewY6mOR2OExcyGpesrZ11OOglo58U1ucWHplfWKCzZu4Xe2"
    "3KpPMq8/3UKA9SRWkl76ie9AkM+e01Tr5VlgqdNlu9pQK+UrO32kdlpCAD7HYemjKpe4n+"
    "PqaASp3ODhu8ElS7LNCcrBBfIdvMwrK9VRunSU5n7TkRWvErxMBW13UgdXPn1Wd9YCTtxx"
    "4ftsccv6F9lMnxdj0Y7Fnzmn543zy7OL87kLmEfWHf6bndd34CL5hm1baVtIOcByplOvb1"
    "Fqc+r1lbU23Za1V+pLVYJw0v0A6Z7WtilkntZWVzJ1W868MioLf+f8bdDvrXCtJiVvWYkr"
    "rX+tgIjXWOqarYarYGSM6tJblvkXKnMOVF1AvWVZwlHu/zCb/QcMMI75"
)
