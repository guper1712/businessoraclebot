from flask import Flask, request
import requests
import os

TOKEN = os.environ.get("TELEGRAM_TOKEN")
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    chat_id = data["message"]["chat"]["id"]
    text = data["message"]["text"].lower()

    if "buffett" in text:
        reply = "Buffett: Focus on long-term value."
    elif "musk" in text:
        reply = "Musk: Move fast. Reinvent the future."
    elif "dalio" in text:
        reply = "Dalio: Think in systems. Embrace reality."
    else:
        reply = "Mention Buffett, Musk, or Dalio to get advice."

    requests.post(URL, json={"chat_id": chat_id, "text": reply})
    return "ok"
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)
