# Coded by @SMDxTG - if Any Query Ask him Directly 

import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file

# Telegram
API_ID = int(os.getenv("API_ID", "36964156"))
API_HASH = os.getenv("API_HASH", "dc4a0e6570a3440c2fc25bc1ac7223bc")
USER_SESSION = os.getenv("USER_SESSION", "AQI0BzwArBF6vAZSGNdhat75W81dANymi35MldcO-0HQBAADrG8u431zN5tGcAEgwxNMvXedsYcZuSxZBRWMAW0OTZJvWwOJAiwqp5We3e-rEaysfLtSaUnrSSod6tEdewMn5yBNanr1-e8UEoWCocEMdFCgdxpcSuMwS2UWn4L8W92JMlOrXr_JaX8UmyIAZ5Omenu8q7rmgq4wI2chNexGmWpvVSxf1e-lxfTHiz_-BLG1wDIW437WK4GLT-QpP_sLg-_Fitz-bPSC3TTJSiz08ZJQ97gVEcD-tinKlVrze7PchCfJXu_TFs2loB38NK28OJh9JKPYahEkmQhCyb2xiurZrgAAAAHaM6NvAA") # Use Pyrogram V2 String Session 
#if you don't have string Gen bot - use it my bot @SMD_StringBot

# Web
PORT = int(os.getenv("PORT", "8080")) 
URL = os.getenv("URL", "") # Heroku or Koyeb Or Render Base Url 

# MongoDB
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Ramkumar2:l2wWk2tGYIbs1V6j@cluster0.3vh2aiz.mongodb.net/?appName=Cluster0") #Mongodb Url 
DATABASE_NAME = os.getenv("DATABASE_NAME", "AUTOLEEX") # example Cluster0

# TamilMV settings
TMV_URL = os.getenv("TMV_URL", "https://www.1tamilmv.gripe/")
TMV_TORRENT = int(os.getenv("TMV_TORRENT", ""))
TMV_LEECH_GRP = int(os.getenv("TMV_LEECH_GRP", ""))
TMV_MIRROR_GRP = int(os.getenv("TMV_MIRROR_GRP", ""))
TMV_TORRENT_THUMB = os.getenv("TMV_TORRENT_THUMB", "https://i.ibb.co/7dq7mMLp/photo-2025-10-18-16-42-28-7562603128038621216.jpg") #torrant Pic
BOT_TAG = os.getenv("BOT_TAG", "@SMD_BOTz") # File Prefix

# Internal
PING_INTERVAL = int(os.getenv("PING_INTERVAL", "120"))
SCRAPE_INTERVAL = int(os.getenv("SCRAPE_INTERVAL", "300"))  # 5 min
SIZE_LIMIT_GB = int(os.getenv("SIZE_LIMIT_GB", 50))  # Default: 50 GB
