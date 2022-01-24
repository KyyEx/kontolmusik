##Config

from os import getenv
from dotenv import load_dotenv

load_dotenv()
get_queue = {}
SESSION_NAME = getenv('SESSION_NAME', 'session')
BOT_TOKEN = getenv('BOT_TOKEN')
API_ID = int(getenv('API_ID', "10892147"))
API_HASH = getenv('API_HASH')
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '30'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ . , : ; !').split())
MONGO_DB_URI = getenv("MONGO_DB_URI")
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '').split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", '-1001288822269'))
ASS_ID = int(getenv("ASS_ID", '2130437611'))
OWNER_ID = list(map(int, getenv('OWNER_ID', '').split()))
GROUP = getenv("GROUP", None)
CHANNEL = getenv("CHANNEL", None)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://KyyEx: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@github.com/KyyEx/kontolmusik")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
AUTO_LEAVE = int(getenv("AUTO_LEAVE", "1500"))
MUST_JOIN = getenv("MUST_JOIN", None)
 if MUST_JOIN.startswith("@"):
     MUST_JOIN = MUST_JOIN.replace("@", "")
