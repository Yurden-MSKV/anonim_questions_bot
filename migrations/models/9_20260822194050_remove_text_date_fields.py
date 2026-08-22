from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "anonymous_messages" DROP COLUMN "created_at";
        ALTER TABLE "anonymous_messages" DROP COLUMN "text";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "anonymous_messages" ADD "created_at" TIMESTAMPTZ;
        ALTER TABLE "anonymous_messages" ADD "text" TEXT NOT NULL;"""


MODELS_STATE = (
    "eJztmm1v4jgQgP9KlE89qVdRWkoXnU6Clt5yW+BU6N1pVyvLJCZYTWxqO+2iHv/9ZOfdBC"
    "gUlhbyqXTscZxn7PHMOC+mR23k8pM6oQR7bcQ5dJBZM15MAj35I7/DsWHC8ThplgIBB67S"
    "gISSiUd9Drygu2qGAy4YtIRZM4bQ5ejYMG3ELYbHAlNi1gziu64UUosLhomTiHyCH30EBH"
    "WQGCFm1oxv348NExMb/UA8+nf8AIYYuXZm9tiWz1ZyICZjJWtgp0XEjeorHzgAFnV9jyT9"
    "xxMxoiRWwERIqYMIYlAg+QTBfPkGcoLha0cvFUw26RLMMqVjoyH0XZF64wFIZCYAnW4f9J"
    "p9AMwVGFmUSL6YCAnkxVRW/PVTuXx2Vi2Xzi4uK+fVauWydHlsmGq+s03VaTCZhFYwlGLW"
    "+qPV6csJUQatwM5SMFU6UMBASxkjoc+QhccYyTnNWKHOGJzkGyGrphnDxXzGGhH7lDlC2L"
    "E1oi6JOZJVGLN/mZpbssdStN++K5YJOwl1ltqfvW4nH1rUX8NlY0sY/xnbpPbb0CeWBGIM"
    "fOwKTPiJfOrvO2Ap8ciRPc4fXSno/F2/u/pcvztq1//9Jbt8O1e33YYiRrlwmBpFDdDQLO"
    "FxB2AbYALihQmsERSreZZFoyz3Nxuy1Z54nDzbcERsxN5kGG2IwirrWiVZ4auev7pmYYN1"
    "bRAu5lUNkFEr6K9Nn/rMQqvTT6utRX8mDD0Y/DIHGD7kxqHBop41xQ1lCDvkCwoC0RbhAh"
    "IL5cAPs6B7HgzzsbZAiDORJlNk8DnOmrJ7nxJgIxcJ9fq9Zt/o3N/emvluviC7hKx+rGXg"
    "XtV7V/XrZpZt4Ak2ALYXD/TBPMerV23aZ+aDla5hAK2HZ8hskPERsoWWqSaJ+842eWVPl0"
    "ACHYVHvoecdZZ8TjElscn8KkrwWkXp5EBLJ+rvDP+rEWT59KP+Gn8u2Afc+qYHfwAXEUeM"
    "zJpRKS2gG+X3lZKe3octZdWUjc5cTB7AM2X2KoQzSpvBvNt1vmXIFkMSBcjLx6+hQAJ7KJ"
    "90VlMvaIWqJ9GPjxc1mAxBu0vcSTi1BeT7rXaz16+3/8pUta7r/aZsKSvpRJMeXWhWigcx"
    "/mn1PxvyX+Nrt9PUi19xv/5XGYyY0BcUEPoMoJ1anJE0olZULd9l1dLna2T/KaUi+9xU9i"
    "mh/rwM6aOG8amlt2oQn4qvUxeO2qoPNW++3CEXqpeYS3rmrnNPkE+3mu1MuEBeT8Bw5+kp"
    "T6p5cd6jOvK4Y5H7HFzuo1yBRf28wtLS0yvWKw6wtx1guymaqFMux39Ep998xyGtX7iMA3"
    "UZArnIYdBbOeLVFDfjNA7GIEW2f9DZPuYAWgI/5VQqG5S6CJI5vi+tp1l8QKm7rYM62oY/"
    "+QOvbvc2Y9BGS9tOnft2o3l3dKosyR9dLObssqK8ssvyygohUuaSFOEnZIPd5KbvzBnOTU"
    "21T1dEgev1uJKbwvVB7d018VaLHXXEsDXK/U4+aFn8gXzS592kKoeSp5RPz6vnl2cX53E0"
    "HEsWBcHLM5AnxHi4w157o5hS2cNr23Kl8oorxXKlMvdOUbVlAyC5qVYgHHbfQ7qnpddc2J"
    "6W5t/YqjYtiaNE5H7ONT/CTKm8Kch8b7Sn7yue3PxhNv0fR7M1jA=="
)
