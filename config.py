import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
# للنشر المحلي
if os.path.exists(".env"):
    load_dotenv(".env")
# الفارات
API_ID = int(os.getenv("API_ID", "14446688"))
API_HASH = os.getenv("API_HASH", "cb812098f053fe4b537e9e0ba4e1d806")
SESSION = os.getenv("SESSION", "AgAA_pwfmU5iiIU-ORGj5ZqrW0wUb5iNdxE3lQipiXUQM5U4C-jVRIvkxg2JmJRzYObMqQM4dYWVRKaCP7VqqFIrhgi9S_wd490LB4eGw-gmuZylLSlM37GTacnGu43Fwj3C6BrhZYx7_cHTZfARG_nNyN8QDsn7fDj30pTKgpUvtOClsUNkWduzpsPZpSLJpDsTFXwNHYprXYU5vsyyOEaf_cznVruEWkzm8eTWj6sEYj30z8_Z4-q6g0qoYYDqhfodJw9KsPuCQuIXb8TFa7obpZuCEGFKYf6eyjW8tyz7Z46z36erNu-OROJOBMvV7oQ1jWSyuSda0bM84jA3JdNpAAAAATlXs_YA")
HNDLR = os.getenv("HNDLR", "$")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "5191100896").split()))
contact_filter = filters.create(    lambda _, __, message: (message.from_user and message.from_user.is_contact)    or message.outgoing)
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicTelethon"))
call_py = PyTgCalls(bot)
