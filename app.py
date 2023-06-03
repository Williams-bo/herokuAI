
import os
from flask import Flask, request
import telebot
import openai

# Set up OpenAI
openai.api_key = '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'

# Set up Telegram bot
bot_token = '5745387931:AAHMqhho8Qz6PZkRE_K-qPs6F5gmZPE-y8U'
bot = telebot.TeleBot(bot_token)

# Set up Flask
app = Flask(__name__)

# Set up Telegram bot handlers
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello! I am your AI bot. How can I assist you?')

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_message = message.text

    # Send message to OpenAI for processing
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=user_message,
        max_tokens=50
    )
    generated_text = response.choices[0].text.strip()

    # Send the generated response back to the user
    bot.reply_to(message, generated_text)

# Set up webhook endpoint
@app.route('/webhook', methods=['POST'])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "OK"

@app.route('/')
def index():
    return "Hello, this is your AI bot!"

# Start the Flask server
def start():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

if __name__ == '__main__':
    start()






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