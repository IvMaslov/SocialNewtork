from redis import Redis
from config.config import app_config

redis_client = Redis(app_config["redis"]["host"], port=app_config["redis"]["port"])
