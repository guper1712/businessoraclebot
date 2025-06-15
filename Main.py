from flask import Flask, request
import telegram
import os

app = Flask(__name__)
bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])

@app.route("/webhook", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text

    if "buffett" in text.lower():
        reply = "Buffett: Focus on value, not hype."
    elif "musk" in text.lower():
        reply = "Musk: Take risks. Fail fast. Move on."
    elif "dalio" in text.lower():
        reply = "Dalio: Understand reality and deal with it."
    else:
        reply = "Choose your Oracle: Buffett / Musk / Dalio"

    bot.send_message(chat_id=chat_id, text=reply)
    return "ok"
if __name__ == "__main__":
    app.run(debug=True, port=5000)
