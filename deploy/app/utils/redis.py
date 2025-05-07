import os
from dotenv import load_dotenv
load_dotenv()

import redis.asyncio as redis

redis_client = redis.Redis(
    host='redis-13169.c91.us-east-1-3.ec2.redns.redis-cloud.com',
    port=13169,
    decode_responses=True,
    username="default",
    password=os.getenv("REDIS_PASSWORD"),
)
