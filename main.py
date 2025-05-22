import telebot
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Yo G, this bot is live on Render 24/7. Let’s print 💵.")

bot.polling(non_stop=True)
