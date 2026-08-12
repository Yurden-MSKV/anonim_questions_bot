from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" ADD "data" JSONB;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" DROP COLUMN "data";"""


MODELS_STATE = (
    "eJztml1v4jgUhv9KlKsZqVvRtJQuWq1EKZ1hp4VVyeyOZrWyTHIIVhObsZ1pUZf/vrKTkA"
    "8CBYa2DHBVeuyT2M/rOG9O8mQGzAVfHDcooyS4BSGwB2bdeDIpDtSP8g5HholHo7RZBSTu"
    "+zoDU0bHAQsFCqLuuhn3heTYkWbdGGBfwJFhuiAcTkaSMGrWDRr6vgoyR0hOqJeGQkq+hY"
    "Ak80AOgZt1459/jwyTUBceQST/ju7RgIDv5kZPXHVuHUdyPNKxS+K1qbzWfdUJ+8hhfhjQ"
    "tP9oLIeMThMIlSrqAQWOJagzSB6qGagBxtNOJhUNNu0SjTKT48IAh77MzLiP0piJUKdro1"
    "7LRshcgZHDqOJLqFRAnkyt4i+/Wtbpac2qnJ5fVM9qtepF5eLIMPV4Z5tqk2gwKa3oUJpZ"
    "+0O7Y6sBMY6dSGcVmOgcLHGUpcVI6Ut4lLP8bXicQz/pX+AvJC/yT2gvEiAJpAqkC+8VJF"
    "hA02590SwDIb75KtD5q3HX/Ni4e3fb+PJet4zjlptu50PSPUXfad50LzX8FLbDQcFBuAT5"
    "FZYgSQDl2POZBfhunHqc/FhCinil/wxKtG9bPbtx+2dOjquG3VItVk6KJPru/H1ejelBjL"
    "/b9kdD/Wt87XZamiYT0uP6jGk/+6upxoRDyRBlDwi7WSZJOAnlVA6Eh4iLCEUcHDIiQCVy"
    "hmWaL9rmFh3l+c1v+xV/ze2vTBsB1AX+Q8IUDnFQZV1V0hW+qhkoZq6lwbbdlt5GhHg1r6"
    "pALu1wCaxNn4XcgdXpZ9MOi38l/OqJZHBf6oqjRT0rxTXjQDz6CcZajjYVElMHSuDHz2Sf"
    "RXSYn+sSiHGm0XSIHD9Mn+Hy1z6jyAUfpJ5+r2Ubnc83N2b5Pv96ZLdteS+Ltnhjy9FtNn"
    "rNxlUrDzfaCjZAtjc90I6yzW2a5WDV3tDHzv0D5i7KbRKqhVmsEJn2nW0KrKAYwRR7Go+a"
    "hxp1nnxJbSfVZH5RJ5rWoZKzp5Uc/XeGf3OIeTn9pP9OVHLMAD8iH6gnh2bdqFYW0E3qON"
    "VKoUaQVHgs3ZS3Zz6h9+iBcXcVwrmkzWB+23X+wpAP5bF9KI+FYo2nzEzS4SlnU085CurB"
    "iT/nFjNLb1WvmLFxmddshVUfZ15/ugMf60nMJT3zhm9HkE9e0lTr5VliqZNlO99QK+UPdn"
    "pP7bQEHzyOg5VvVYXEzdyu9kaQgxvcLzeorr9Zff/odTvl2ib9i6oSRxr/GT4RL/XGwfxt"
    "EFJHSWX0Q+JLQsWxOuvv5uurrPAs/jih+B1CQTl1gMsyc7iMl+HgAPkObu7boYOpmTE1hZ"
    "dr8o14befm9QyutJS5Pqidq2O/qE1uACfOsPS7wqhl8QeFaZ+t8cr7YpStk7Pa2cXp+dnU"
    "jk0ji1zY8xb4O3ARX2HLljwzKTtYV7aq1SVqnla1OrfoqdvyPlddVCsQjrvvIN2TyjIV5Z"
    "PK/JKybis8RTAqS184z7eYmZQfcpnbRnuyXYZy8zezyf9SGgtP"
)
