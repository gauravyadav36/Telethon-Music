import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 5679766357:AAGI58nRjE7lpC9VtwBqbJFCjcUaJuwXT8A")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOGcBu3Rj3s9TD9u1tLac4dczyMWgfX0pOCtDCMqEGRFWAO4H1uaAlV4m7NDSoB8sHklgO_YkJ7_G2QyAQxATdENR5pp-FvcF-EGT4X3mCFEz7eU7yl82S51QztccnAytuW622a5vRWJvUisfSEAJid5bAkjh6u31fqBjNV-JQ_o88mTtmov6hvO5VakBE0lp6GkewA8tUPGyH4MeuseK3KExhuCawdSim1QCEsQ_W_WyfLL4-BLri6LtUr8GmOmWRcJ4WJqBZKIAuhbx6BgMUjUGGl1qljqSbensWWqi4N8f69n9iHcyeevs6ChhiTXyRwcyOdPcgFKcwekvOFGzKGCtAds=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "lofi_fridey347")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "2083840977")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
