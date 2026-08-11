from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "anonymous_messages" ALTER COLUMN "sender_id" DROP NOT NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "anonymous_messages" ALTER COLUMN "sender_id" SET NOT NULL;"""


MODELS_STATE = (
    "eJztmlFz2jgQx7+Kx0/tTK5DnBByvFFCWq4JdIJ71+nNjUbYG6OJLVFJbsLk+O43km2MjS"
    "GYIwkBP4WstLL0W1n6a61HM2Au+OJDizJKgmsQAntgNo1Hk+JA/SiucGSYeDxOi5VB4qGv"
    "PTBldBKwUKAgqq6L8VBIjh1pNo1b7As4MkwXhMPJWBJGzaZBQ99XRuYIyQn1UlNIyc8QkG"
    "QeyBFws2n8/c+RYRLqwgOI5N/xHbol4LuZ3hNXPVvbkZyMte0j8bpUXuq66oFD5DA/DGha"
    "fzyRI0ZnDoRKZfWAAscS1BMkD9UIVAfjYSeDijqbVol6Oefjwi0OfTk34iFKbSZCvb6NBh"
    "0bIbMEI4dRxZdQqYA8mjqKv/1uWScnDat2cnZeP2006ue18yPD1P1dLGpMo86ktKKmNLPu"
    "p27PVh1iHDtRnJVhqn2wxJGXDkZKX8KDXORvw8MS+kn9HH8heZ5/QntVABJDGoF04r1ACF"
    "bQtDvfNctAiJ++MvT+bN20P7du3l23vr/XJZO45Krf+5RUT9H32lf9jxp+CtvhoOAgXID8"
    "AkuQJIBi7FnPHHw3dv2Q/FgjFPFMfwuR6F53Bnbr+msmHBctu6NKrEwoEuu7s/fZaMwaMf"
    "7q2p8N9a/xo9/raJpMSI/rJ6b17B+m6hMOJUOU3SPszjNJzIkpE+VAeIi4iFDEwSFjAlQi"
    "Z1QU81XL3KpWnl78dj/iL7n8FcVGAHWB/6/A5JqoorJpVNIZXlYM5D03isGubUuvE4R4Np"
    "eNQMategU2ps9C7kB5+vNu1eQvhV+dSG7vClVxNKkXQ3HJOBCPfoGJDkeXCompAwXw4zPZ"
    "NxE187ZegRhnak27yPH97AyXffcZRS74IPXwBx3b6H27ujKL1/mXI7tr03tdtPmNLUO33R"
    "q0WxedLNxoKdgC2cGsoT1lm1k0i8GqtWGInbt7zF2UWSRUCbNYzjKru1gUWEHegin2NB41"
    "DtXrLPmC3E4ak+VJnWhYVSbnQDM5+u8C//YI82L6Sf29yOSYAX5APlBPjsymUa+toJvkce"
    "q1XI4gyfBYuigrz3xC79A9424Zwhmn7WB+3Xn+zJCr9NghpMdCscEpc86pOuVs65SjoFZK"
    "/Cm1ODf1ymrFORk395ktN+tjz8svN+BjPYilpBe+8O0J8ulzimo9PQskdTJtlwtqFflKTh"
    "+onJbgg8dxUHqryjluZ7s6mIBUanD/1eCCJFlnB+XgAPkFbubGSrWVLmyluU868pV47eYr"
    "8wSuNIG2Oai9y54+qzhrASfOqPA2W1Sy+hpbWmdnFNqhyDPr+LRxen5ydjoTATPLqr3/ae"
    "H1C7iI37B1E21zLnuYzbTq9TUybVa9vjTVpsuy6kq9VCUIx9X3kO5xbZ085nFteSJTl+W0"
    "K6Oy8DPnH4N+b4loTV3yipU40vjX8Il4i5mu6XK4CkZGpy7cscxfp8wJUNWAumNZQlBufz"
    "Ob/gcMp457"
)
