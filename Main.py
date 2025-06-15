from flask import Flask, request
import telegram
import os

TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

@app.route("/webhook", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text

    if "buffett" in text.lower():
        response = "Buffett: Focus on long-term value and fundamentals."
    elif "musk" in text.lower():
        response = "Musk: Move fast. Take risks. Reinvent the future."
    elif "dalio" in text.lower():
        response = "Dalio: Embrace reality. Use principles. Think in systems."
    else:
        response = "Please type 'Buffett', 'Musk' or 'Dalio' in your message."

    bot.send_message(chat_id=chat_id, text=response)
    return "ok"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
