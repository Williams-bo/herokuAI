
import openai
import telegram
from flask import Flask, request

app = Flask(__name__)
telegram_bot_token = "5745387931:AAHMqhho8Qz6PZkRE_K-qPs6F5gmZPE-y8U"
openai.api_key = "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"

bot = telegram.Bot(token=telegram_bot_token)

def generate_response(message):
    # Use OpenAI to generate a response
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message,
        temperature=0.6,
        max_tokens=50,
        n=1,
        stop=None,
    )
    response_text = response.choices[0].text.strip()
    return response_text

@app.route('/', methods=['GET', 'POST'])
def telegram_webhook():
    if request.method == 'POST':
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat_id
        message = update.message.text
        response = generate_response(message)
        bot.send_message(chat_id=chat_id, text=response)
        return 'OK'
    else:
        return 'This is the root route of the Flask app.'



if __name__ == '__main__':
    app.run()





# import telebot

# bot = telebot.TeleBot('5745387931:AAHMqhho8Qz6PZkRE_K-qPs6F5gmZPE-y8U')

# #Define a function that will be called when a message is received
# @bot.message_handler(commands=['start', 'help', 'info', 'status'])
# def handle_command(message):
#     if message.text == '/start':
#         bot.send_message(message.chat.id, "Hell! I'm a bot. Please type /help to see my commands")
#     elif message.text == '/help':
#         bot.send_message(message.chat.id, "Commands: \n /start - Start the bot \n /help - Show this message \n /info - Show information about the bot \n /status - Show the status of the bot")
#     elif message.text == '/info':
#         bot.send_message(message.chat.id, "I am a simple telegram bot created to demonstrate how to respond to commands")
#     elif message.text == '/status':
#         bot.send_message(message.chat.id, "I am currently online and ready to receive commands!")

# # Start the bot

# bot.polling()