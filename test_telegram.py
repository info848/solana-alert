import requests

BOT_TOKEN = "8269639504:AAGrGq-U6WuXRFYNJ-pcOOKTwnqgmWP-cBo"
CHAT_ID = "6104505218"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
data = {"chat_id": CHAT_ID, "text": "🚀 Test Telegram funzionante dal cloud!"}

resp = requests.post(url, data=data)
print(resp.text)
