from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    LOGGER = True

    API_ID = int(getenv("API_ID", 25395782))
    API_HASH = getenv("API_HASH", "3c0f6066a07142d664690cfd34447450")
    ARQ_API_KEY = "PMPTTD-HOMLMF-SRBHNH-RZMWXL-ARQ"
    SPAMWATCH_API = None
    TOKEN = getenv("TOKEN", "")
    OWNER_ID = int(getenv("OWNER_ID", 6848223695))
    OWNER_USERNAME = getenv("OWNER_USERNAME", "its_damiann")
    SUPPORT_CHAT = getenv("SUPPORT_CHAT", "")
    UPDATE_CHAT = getenv("UPDATE_CHAT", "the_hogwart")
    LOGGER_ID = int(getenv("LOGGER_ID", "-1002023182491"))
    EVENT_LOG = int(getenv("EVENT_LOG", "-1002023182491"))
    MONGO_URI = getenv(
        "MONGO_DB_URI",
        "mongodb+srv://@.",
    )
    DB_NAME = getenv("DB_NAME", "HoshinoBotV3")
    REDIS_URL = "redis://default::12586"
    DATABASE_URL = getenv("DATABASE_URL", "postgres://wsnioboi:/wsnioboi")

    # ɴᴏ ᴇᴅɪᴛ ᴢᴏɴᴇ
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
