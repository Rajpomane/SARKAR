from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/ebf34649780915d5951fe.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/ebcf5d6354a44ff833cc7.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/BRANDED_WORLD")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "BRANDED_KHUSHI")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6258877205").split()))


FAILED = "https://te.legra.ph/file/ebf34649780915d5951fe.jpg"
