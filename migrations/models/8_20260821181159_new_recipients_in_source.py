from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "anonymous_messages" ADD "recipients" BIGINT[] DEFAULT '{}';
        ALTER TABLE "anonymous_messages" ADD "data" JSONB;
        ALTER TABLE "anonymous_messages" ALTER COLUMN "recipient_id" DROP NOT NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "anonymous_messages" DROP COLUMN "recipients";
        ALTER TABLE "anonymous_messages" DROP COLUMN "data";
        ALTER TABLE "anonymous_messages" ALTER COLUMN "recipient_id" SET NOT NULL;"""


MODELS_STATE = (
    "eJztW/9PIjkU/1cm85ObeAZR1DOXTQBxl1uFi+DtZjebpszUoXGmxbajEo///dLO9zKDgC"
    "Io8xPw+l6n/Xza1/dehyfTozZy+V6dUIK9S8Q5dJB5ajyZBHryS77CrmHC0ShplgIBB66y"
    "gISSsUd9DrxAXTXDARcMWsI8NW6gy9GuYdqIWwyPBKbEPDWI77pSSC0uGCZOIvIJvvMREN"
    "RBYoiYeWr8+r1rmJjY6BHx6OfoFtxg5NqZ0WNbPlvJgRiPlKyBnTYR50pXPnAALOr6Hkn0"
    "R2MxpCQ2wERIqYMIYlAg+QTBfDkDOcBw2tGkgsEmKsEoUzY2uoG+K1IzHoBEZgLQ6fZBr9"
    "UHwFwAI4sSiS8mQgLyZCoW//izWj04OK5WDo5OaofHx7WTysmuYarxTjcdT4LBJGgFXSnM"
    "2l/anb4cEGXQCniWgomygQIGVoqMBH2GLDzCSI5pioU6Y3CcT0LWTCPDxXyKjQj7FB0h2D"
    "EbkUpCR7IKY+yfJuaK+HgW2l+/FZYJdgI9imnU+uixYOVG+hpcXLA50JpavPPAtcLlOwOu"
    "fuuHWoce53euFHT+rV81v9avdi7rPz6plnHYctHtfInUk2XbaV50GxrYFkMSHABzID+DAg"
    "nsoXzYs5Ya+HZouhd9WdHCXRMT7ctWr1+//CdDx1m935It1QwVkXTn6FOWjbgT43u7/9WQ"
    "P42f3U5LoUm5cJh6YqLX/2nKMUFfUEDoA4B2GpNIHIkyLEs/Nc3v371uJ5/bSF9nFVvC+M"
    "9YpSP668YnlqTKGPjYFZjwPfnUz2twTxKe2ftN31oac7IDfb953AHYBpiA2NcDa5i3+2Yd"
    "1rN6ef4I3/y995aHeB43HBEbsRcRo3VRsrIsK8kKXzSk1S1LDpblIFzMixKQMSvRXxp96j"
    "MLLY5+2mwp9DctOH47+GVafXObm9oFi3qainPKEHbINxTkdm3CBSQWygE/LCxc86Cb97UF"
    "QjgTaTJEBh/iQkR271MCbOQioabfa/WNzvXFhZnv5ktkn0FWP9Yy4DbrvWb9rJXFNvAErw"
    "BsL+7onXmOuVdt2mfmAytdwwBatw+Q2SDjI2QLrVJNEutON3lVT5dAAh0Fj5yHHHUW+Zz6"
    "ZMJJcWEymFZZjdzSaqT6nMK/OYQsH/1I/0NU1EwPPgIXEUcMzVOjVpmBbpTf1yp6eh+2VF"
    "VTNjpzMbkFD5TZiyCcMXodmNe7zlcMclmmLESeIWh3iTsOh/ZOypYhimXV8l1ULX2+RPaf"
    "Miqzz9fKPiWob5chvdcwPrX0Fg3iU/F16g5fW/Wh5fm3K+RCNYlCpKdeH/ggkE9Wmu2MuU"
    "BeT8Bw5+kpT6p5dt6jFHmsWOY+W5f7KFdgUT+vsPTs6RXblQfYyw6w9RRN1CmX4z+i06/Y"
    "cUj2S5expS5DIBc5DHoLR7ya4es4ja0hpMz2tzrbxxxAS+D7nEplg1IXQVLg+9J2GuMDSt"
    "1VHdTRNnzjdya73YsMoY22/pbf9WWjdbWzr5jkdy4WBbusLK+ss7yyQIiUuSRF+B7ZYD25"
    "6YY5w8LUVHt1RZRwzQ9XclO4PFAf7pp4pcWOOmLYGub+9SRomf2fk0RnY1KVbclTqvuHx4"
    "cnB0eHcTQcS2YFwc9nIPeI8XCHzXujmDL5gNe21VptjivFaq1WeKeo2rIBkNxUCyAcqn9A"
    "dPcr81zY7leKb2xVm5bEUSJyX+cqjjBTJi8KMjcN7clmxZOvf5hN/gdTlUNM"
)
