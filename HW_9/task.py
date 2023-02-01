# 1) Напишите Бота, удаляющего из текста все слова, содержащие "абв". (Ввод от пользователя)
# Пример:
# привет приабвет ограбпв
# Ответ:
# привет ограбпв

from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

token = ''

updater = Updater(token)
bot = Bot(token)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Введи текст, \
а я удалю из текста все слова, содержащие "абв"')

def edit_text(update, context):
    text_lst = update.message.text.split()
    text_lst_filtered = list(filter(lambda el: ('абв' not in el.lower()), text_lst))
    new_text = ' '.join(text_lst_filtered)
    
    if new_text != '':
        context.bot.send_message(update.effective_chat.id, new_text)
    else:
        context.bot.send_message(update.effective_chat.id, 'пришлось всё удалить')

start_handler = CommandHandler('start', start)
edit_text_handler = MessageHandler(Filters.text, edit_text)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(edit_text_handler)

updater.start_polling()
updater.idle() 