from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    LOGGER = True

    API_ID = int(getenv("API_ID", 25395782))
    API_HASH = getenv("API_HASH", "3c0f6066a07142d664690cfd34447450")
    ARQ_API_KEY = "PMPTTD-HOMLMF-SRBHNH-RZMWXL-ARQ"
    SPAMWATCH_API = None
    TOKEN = getenv("TOKEN", "7519139941:AAE6jFCGiqvhLu1i7HoNL9qdQRZgrQm6HqM")
    OWNER_ID = int(getenv("OWNER_ID", 1886390680))
    OWNER_USERNAME = getenv("OWNER_USERNAME", "sung_jinwo4")
    SUPPORT_CHAT = getenv("SUPPORT_CHAT", "souls_societyy")
    UPDATE_CHAT = getenv("UPDATE_CHAT", "soul_networks")
    LOGGER_ID = int(getenv("LOGGER_ID", "-1002046276298"))
    EVENT_LOG = int(getenv("EVENT_LOG", "-1002046276298"))
    MONGO_URI = getenv(
        "MONGO_DB_URI",
        "mongodb+srv://kiraPersonalDB:KiraDB2023@cluster0.qm8bgzb.mongodb.net/",
    )
    DB_NAME = getenv("DB_NAME", "HoshinoBotV3")
    REDIS_URL = "redis://default:QuPcQZrXEMAQ6KCrsAKWwL1aQW3gsZEu@redis-16159.c274.us-east-1-3.ec2.cloud.redislabs.com:16159"
    DATABASE_URL = getenv("DATABASE_URL", "postgres://avnadmin:AVNS_Ez0UFOgjgaSCk-Gr7NQ@sung-erenyeager.h.aivencloud.com:23096/defaultdb?sslmode=require")

    # ɴᴏ ᴇᴅɪᴛ ᴢᴏɴᴇ
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
