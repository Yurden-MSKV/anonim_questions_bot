from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" ADD "is_active" BOOL NOT NULL DEFAULT True;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" DROP COLUMN "is_active";"""


MODELS_STATE = (
    "eJztWm1v4jgQ/itRPnWlXkVpaXvV6SRo6S63vJwKvVvt6WSZZAhWE5vaTlvU47+f7CTkhU"
    "Chb1DIp9LxjGM/jz2eGfvJ9JgNrjioUkaJ1wIhsAPmufFkUuypH/kK+4aJR6O4WQkk7rva"
    "AlNGxx7zBfICdd2M+0JybEnz3BhgV8C+YdogLE5GkjBqnhvUd10lZJaQnFAnFvmU3PmAJH"
    "NADoGb58Y//+4bJqE2PIKI/h3dogEB106Nntjq21qO5HikZTXiNKi80rrqg31kMdf3aKw/"
    "Gssho1MDQqWSOkCBYwnqC5L7agZqgOG0o0kFg41VglEmbGwYYN+ViRn3USwzEWp3eqhb7y"
    "FkroCRxajCl1CpAHkyNYu//FouHx2dlktHJ2eV49PTylnpbN8w9Xhnm04nwWBitIKuNGaN"
    "r412Tw2IcWwFPCvBRNtgiQMrTUaMvoRHOYt/Dx7noB/pZ/AXkmfxj9BeREAkiBmIF94HUL"
    "AAzV79h8bSE+LOVYL2X9Xri2/V671W9ccX3TIOW5qd9tdIPYa+fdHs1DT4MdgWBwUOwjmQ"
    "X2IJkniQD3vaMgO+HZoeRD+WoCJc6Z+BiUar3u1VW3+m6Lis9uqqpZyiIpLunXxJszHtxP"
    "i70ftmqH+Nn512XaPJhHS4/mKs1/tpqjFhXzJE2QPCdhKTSByJUix7wkHERoQiDhYZEaAS"
    "WcM8zhe5uUW9PO/8Np/xj3R/edwIoDbwVxGT6aJg5aWsxCt81WAga/kiDjbtWFoPCeFqXp"
    "WBlFmxBV6MPvO5BaujnzQrFv9K8KuMZHCbGxUHi3qWiivGgTj0O4w1HQ0qJKYW5IAf5mQ3"
    "Iujmc22BEM5YGg+R44dpDpfe+4wiG1yQevrdes9o3zSbZr6f/zhkN215Lwtt9mBLoXtR7V"
    "5UL+tpcANX8AbIdqcdbSm2KaeZD6zyDX1s3T5gbqOUk1AtrMwykqnubJNX9rISTLGj4VHz"
    "UKNOI59T24k5mV/UCaZVVHJ2tJKj/87gfzHEPB/9SH8rKjmmhx+RC9SRQ/PcqJQWoBvVcS"
    "qlTI0gqvCUdVM6PHMJvUUPjNurIJwyehuY17vO3xnkojw2F3kO2O5QdxwO7ZOUy0IUF1bL"
    "lD+bpfuPbqedT3WknyWZWNL4z3CJeK+U0/xt4FNLMWf0feJKQsWB+urv5sfXRBU8i6vT2U"
    "J0hjjVQbY67YsXpP8JoyL9fKv0U4FapEjPhfGJpbdqEJ+IrxP3n5lVH1pefb8GF+tJzEV6"
    "5up1SyCfvGu2MxYSvK7E4c7LpjyJ5sV5j1YUU8Ui99m53Ee7Aov5eZWlZ0+vqV1xgL3uAF"
    "tP0USfcjn+Izr95jsOxX7hMnbUZUhwweHYWznizRi+jdPYGUKKbH+ns30iELYkuc+pVNYY"
    "cwHTOb4vaZdhvM+Y+14HdbQNPza9r3U6zRShtUb2ddlNq1a/3jvUTIo7l8g5u6wor6yzvL"
    "JCiJS6JQVyD3bqbW6Rm87kppnHK3JNeG3Y4bEcXPFV4cuB2rp74netdlSBE2uY+24/aFn8"
    "YD/W2ZhcZVcSlfLh8enx2dHJ8TQcnkoWRcHPpyD3wEW4w5a9UkyYbOG9bblSWeJOsVypzL"
    "1U1G3pCEhtqhUQDtW3EN3D0jI3toel+Ve2ui2TxTEqcx90zQ8xEyavijI3De3JZgWUb3+Y"
    "Tf4HMoJgHQ=="
)
