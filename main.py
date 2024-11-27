import telebot

# Получение корректного токена бота
TOKEN = '8149796529:AAFLmeDPUKxYLsRLxO_gB3pdwG6TFL1l2l4'

# Создание экземпляра бота
bot = telebot.TeleBot(TOKEN)

# Функция для пересылки сообщения в группу
@bot.message_handler(commands=['forward'])
def forward_message(message):
 chat_id = -4516190331 # ID вашей группы
 message_id = message.message_id # ID сообщения
 bot.forward_message(chat_id=chat_id, from_chat_id=message.chat.id, message_id=message.message_id)

# Функция для обработки текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
 chat_id = -4516190331 # ID группы
 bot.forward_message(chat_id=chat_id, from_chat_id=message.chat.id, message_id=message.message_id)

# Запуск бота
bot.polling(none_stop=True)