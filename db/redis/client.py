from redis import Redis
from config.config import app_config


redis_client = Redis(app_config["redis"]["host"], port=app_config["redis"]["port"])


# r.sadd("likes", "3:4")
# r.sismember("likes", "3:4")
# r.srem("likes", "3:4")