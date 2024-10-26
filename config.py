import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 23028479
API_HASH = "c1e6a93b04c0810a5c282d8d8d44ea6f"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7892211587:AAGrn0aYADE75zX9pJOrofw0iaTbTwv1bPk"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://GOKU:MISSBHOPALI@goku.pzzsl8d.mongodb.net/?retryWrites=true&w=majority"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002252184024

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 7038202445

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/Shorekeeper_updates"
SUPPORT_GROUP = "https://t.me/Anime_Group_India_Chat"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "STRING_SESSION"
STRING2 = getenv("BQGWS8YAcExf2Cp-m9-Z388GFSKeUyXsv-rauB0jNKp6BQRnlxZoflKYQJsUDpk0ii2VAAmduJZ79ncqyuejJyckRijhrWkWzQdbFiz-eH95xLciXrPprMBVDDup95_s81jAjIWJ2zO0_Vvg7RMNIY0weyX36A66oL9KS9GlkZb0tGOFrXJZG1qeio5LsvP1j8adtmGhcA_P6l8CXB8mMU-L_P21bFOIsgqlUTfYuhNPbsjZx-oTKNsr1Mf51XR7pGiYbdUIf9t9dCIsyAg_jKEyoBeTAvfn8UDCp2mnVMgiR8nYRmOZh3sRwrXcrFArpcZD-v49NFm-pUfsj1xZk6L2D77zIwAAAAG-IuuuAA", None)
STRING3 = getenv("BQGWS8YAcExf2Cp-m9-Z388GFSKeUyXsv-rauB0jNKp6BQRnlxZoflKYQJsUDpk0ii2VAAmduJZ79ncqyuejJyckRijhrWkWzQdbFiz-eH95xLciXrPprMBVDDup95_s81jAjIWJ2zO0_Vvg7RMNIY0weyX36A66oL9KS9GlkZb0tGOFrXJZG1qeio5LsvP1j8adtmGhcA_P6l8CXB8mMU-L_P21bFOIsgqlUTfYuhNPbsjZx-oTKNsr1Mf51XR7pGiYbdUIf9t9dCIsyAg_jKEyoBeTAvfn8UDCp2mnVMgiR8nYRmOZh3sRwrXcrFArpcZD-v49NFm-pUfsj1xZk6L2D77zIwAAAAG-IuuuAA", None)
STRING4 = getenv("BQGWS8YAcExf2Cp-m9-Z388GFSKeUyXsv-rauB0jNKp6BQRnlxZoflKYQJsUDpk0ii2VAAmduJZ79ncqyuejJyckRijhrWkWzQdbFiz-eH95xLciXrPprMBVDDup95_s81jAjIWJ2zO0_Vvg7RMNIY0weyX36A66oL9KS9GlkZb0tGOFrXJZG1qeio5LsvP1j8adtmGhcA_P6l8CXB8mMU-L_P21bFOIsgqlUTfYuhNPbsjZx-oTKNsr1Mf51XR7pGiYbdUIf9t9dCIsyAg_jKEyoBeTAvfn8UDCp2mnVMgiR8nYRmOZh3sRwrXcrFArpcZD-v49NFm-pUfsj1xZk6L2D77zIwAAAAG-IuuuAA", None)
STRING5 = getenv("BQGWS8YAcExf2Cp-m9-Z388GFSKeUyXsv-rauB0jNKp6BQRnlxZoflKYQJsUDpk0ii2VAAmduJZ79ncqyuejJyckRijhrWkWzQdbFiz-eH95xLciXrPprMBVDDup95_s81jAjIWJ2zO0_Vvg7RMNIY0weyX36A66oL9KS9GlkZb0tGOFrXJZG1qeio5LsvP1j8adtmGhcA_P6l8CXB8mMU-L_P21bFOIsgqlUTfYuhNPbsjZx-oTKNsr1Mf51XR7pGiYbdUIf9t9dCIsyAg_jKEyoBeTAvfn8UDCp2mnVMgiR8nYRmOZh3sRwrXcrFArpcZD-v49NFm-pUfsj1xZk6L2D77zIwAAAAG-IuuuAA", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://envs.sh/AJT.jpg"

PING_IMG_URL = "https://envs.sh/W_z.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/763a841a2ad5cbb1e2fc5.jpg"
STATS_IMG_URL = "https://envs.sh/AJA.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
TELEGRAM_VIDEO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
