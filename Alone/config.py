from os import getenv
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Initialize configuration variables
que = {}
admins = {}

# Fetch and set environment variables with sensible defaults
SESSION_NAME = getenv("SESSION_NAME", "BQCGDdUATyw-qX_T22xrw1Q_tJbMrcOheKS_Qc-dYe4RINWGs5ruvkRG9s01tvOJCRle9IaskG1LDptTsDeCOsZWfWp-t8vpOe0K3_8mA9Xo9r421oK0OB77ahw012uELpc_f8psP7dVKdOzm-3M0pSIFGE2GMEIX_P-sqjXyykhvuwRxLiqkk9x3Y9wjQiNVXrJQ1CER4jxD5wjkILB_pk2xuG6avP2svZApjaoETaG8AeGnezmgyAe5ibO5_JqYBuk7OlfBk1bteajO0nCvZFsjZfdEx2N52fx7X8jZkhnVUaen-4dT92HeDLmoq6pkwatldXUzTQMSgu9IESfIeManUb2ugAAAAFDAnVeAA")
BOT_TOKEN = getenv("7760699975:AAGQMKV0oTlK7A4d9LM4_y99a-kHWLAkaaA")  # Ensure you have a BOT_TOKEN defined in your .env
BOT_NAME = getenv("BOT_NAME", "Tamil Music Bot")
BOT_USERNAME = getenv("BOT_USERNAME", "MusictamilanRobot")
ASSID = int(getenv("ASSID", "5419201886"))  # Use a sensible default for IDs
ASSNAME = getenv("ASSNAME", "Yaaro Oruthan")
ASSUSERNAME = getenv("ASSUSERNAME", "Tamilan_143")
BOT_ID = int(getenv("BOT_ID", "7760699975"))  # Use a sensible default for IDs
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://defaultrepo.com")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "your_heroku_api_key")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "your_app_name")
MONGO_DB_URI = getenv("MONGO_DB_URI", "your_mongo_db_uri")
API_ID = int(getenv("API_ID", "8785365"))
API_HASH = getenv("API_HASH", "48c1934c1df9da5b218cfc1382be1bdf")
OWNER_ID = int(getenv("OWNER_ID", "7074356361"))  # Default to 0 if not set
UPDATE = getenv("UPDATE", "hgbotsupdates")
SUPPORT = getenv("SUPPORT", "hgbotSupportgroup")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "999"))
CMD_MUSIC = list(getenv("CMD_MUSIC", "/ !").split())
BG_IMG = getenv("BG_IMG", "default_bg_image_url")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "0").split()))  # Default to an empty list
START_PIC = getenv("START_PIC", "default_start_pic_url")
OWNER_USERNAME = getenv("OWNER_USERNAME", "hemanthgaming_1k")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/default1.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/default2.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/default3.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/default4.png")

# Check for essential variables and raise exceptions if they are missing
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set in the environment variables.")
if not API_ID:
    raise ValueError("API_ID is not set in the environment variables.")
if not API_HASH:
    raise ValueError("API_HASH is not set in the environment variables.")
