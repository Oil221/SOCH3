import telebot
import random

TOKEN = "8431714204:AAGp8xzWHHKrZ-kWgD8L6ZOhh5tBd_9rQtM"

bot = telebot.TeleBot(TOKEN)

# команда /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот случайных чисел.\nКоманды:\n/random - случайное число\n/dice - бросить кубик")

# команда /random
@bot.message_handler(commands=['random'])
def random_number(message):
    number = random.randint(1, 100)
    bot.send_message(message.chat.id, f"Ваше число: {number}")

# команда /dice
@bot.message_handler(commands=['dice'])
def dice(message):
    roll = random.randint(1, 6)
    bot.send_message(message.chat.id, f"Выпало: {roll}")

bot.infinity_polling()