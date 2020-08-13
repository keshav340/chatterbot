
from flask import Flask, render_template, request
from chatterbot.trainers import ChatterBotCorpusTrainer

from chatterbot import ChatBot

app = Flask(__name__)
Keshav_bot = ChatBot(
    'KeshavBot',
     filters=["chatterbot.filters.RepetitiveResponseFilter"]
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    try:
        return str(Keshav_bot.get_response(userText))
    except Exception:
        return str("I didn't get you")
if __name__ =='__main__':
    app.run(debug=False,host='127.0.0.1',port =8060)