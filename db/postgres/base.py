from databases import Database
from sqlalchemy import MetaData,create_engine
from config import config

DATABASE_URL = config.app_config["database"]["url"]

database = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(DATABASE_URL, )