import telebot

# Create a new bot.
bot = telebot.TeleBot("6490700108:AAHFyNyn-tMoihiiEk-rn5DFioPnLbL8by8")

# Handle '/start' command.
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Hello! I am a simple bot. What can I do for you?")

# Handle '/help' command.
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.reply_to(
        message,
        "I can help you with the following:\n"
        "- /start: Start the bot.\n"
        "- /help: Get help.\n"
        "- /echo: Echo back your message.\n"
        "- /time: Get the current time.\n",
    )

# Handle '/echo' command.
@bot.message_handler(commands=['echo'])
def echo_message(message):
    bot.reply_to(message, message.text)

# Handle '/time' command.
@bot.message_handler(commands=['time'])
def time_message(message):
    import datetime
    now = datetime.datetime.now()
    bot.reply_to(message, now.strftime("%H:%M:%S"))

# Handle all other messages.
@bot.message_handler(func=lambda message: True)
def default_message(message):
    bot.reply_to(message, "I don't understand you.")

# Start the bot.
bot.polling()
