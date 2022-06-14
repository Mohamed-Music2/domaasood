import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
# للنشر المحلي
if os.path.exists(".env"):
    load_dotenv(".env")
# الفارات
API_ID = int(os.getenv("API_ID","16115488"))
API_HASH = os.getenv("API_HASH","6d63bf20bc5c986c77332a98e5d65894")
SESSION = os.getenv("SESSION","BAAmB3X6Lzhe8Q3J5VwB8WdBg8B6K3Hgz8em1cSWTO8OdYfpCp5zMMHHIF7cv0B7hOrC4Ik_tjJN5EAX5WfMtlOKU0ExcpbbBxF2iXhKvhuzPpTIf0ci5CEhOCeTWt1N1BaB3HK7LaN_O20YBa3h_5a5LI2qcLwQW2RMO9DuKS_m7HO6u2GFtK9m5GyBsr1gqEyPNyXjiOAHUmu-4G80ZJycmUYy44p2Jt6zMK82RCRoI1W737G3nAJ3iT4rjrVTp_m0aDL7JI1GnAXzSmrqMq40eI7-OsqN60IGSFCJBQ0lmPdb87LB5NA6Qtl1vaCjNjyCxH3eM7vQ46RRe-giRwnfAAAAATB36rAA")
HNDLR = os.getenv("HNDLR", "")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS","5191100896").split()))
contact_filter = filters.create(    lambda _, __, message: (message.from_user and message.from_user.is_contact)    or message.outgoing)
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicTelethon"))
call_py = PyTgCalls(bot)
