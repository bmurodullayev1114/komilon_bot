# from environs import Env

# # environs kutubxonasidan foydalanish
# env = Env()
# env.read_env()

# # .env fayl ichidan quyidagilarni o'qiymiz
# BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
# ADMINS = env.list("ADMINS")  # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili

# CHANNELS = ["@komilon_savdo"]

import os

# env fayl ichidan quydagilarni o'qiymiz
BOT_TOKEN=str(os.environ.get("BOT_TOKEN")) #Bot token
ADMINS=str(os.environ.get("ADMINS")) #Admin ro'yxati
IP=str(os.environ.get("ip")) #Xosting ip manzili
PROVIDER_TOKEN=str(os.environ.get("PROVIDER_TOKEN"))
CHANNELS=str(os.environ.get("CHANNELS"))



