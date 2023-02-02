# Прикрутить бота к задачам с предыдущего семинара:
# Создать калькулятор для работы с рациональными, организовать меню, 
# добавив в неё систему логирования(Содержит: id.Пользователь, ввод, результат)
# 12 + 3 * 3
# Ваш ответ: 21

from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler
from operations import add_space, symb_to_res
from logger import logger

token = ''

updater = Updater(token)
bot = Bot(token)
dispatcher = updater.dispatcher

A = 0
B = 1

def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Привет! Посчитаем?\n(да/нет)')
    logger(update.effective_chat.id, 'start', '  -')
    return A

def answer(update, context):
    text = update.message.text
    if 'да' in text.lower():
        context.bot.send_message(update.effective_chat.id, '''Введи выражение без пробелов
десятичные дроби - с точкой
используй знаки *  /  +  -
не используй скобки

Пример записи выражения:
-0.8*2-1/2*3-0.3*3+4''')
        return B

    elif 'нет' in text.lower():
        context.bot.send_message(update.effective_chat.id, 'Обращайся, если что. Пока!')
        logger(update.effective_chat.id, 'end', '  -')
        return ConversationHandler.END

    else:
        context.bot.send_message(update.effective_chat.id, 'Не понимаю тебя. Давай еще раз:\nПосчитаем?\n(да/нет)')
        return A
    
def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'Ой, что-то пошло не так')
    logger(update.effective_chat.id, 'ERROR', '  -')

def result(update, context):
    s = update.message.text
    lst = add_space(s).split()
    lst = symb_to_res(lst, '/')
    # res1 = ''.join(lst)
    lst = symb_to_res(lst, '*')
    # res2 = ''.join(lst)
    lst = symb_to_res(lst, '-')
    # res3 = ''.join(lst)
    lst = symb_to_res(lst, '+')
    res = ''.join(lst)
    # context.bot.send_message(update.effective_chat.id, s + ' =\n' + \
    #                                                 '= ' + res1 + ' =\n' + \
    #                                                 '= ' + res2 + ' =\n' + \
    #                                                 '= ' + res3 + ' =\n' + \
    #                                                 '= ' + res)
    context.bot.send_message(update.effective_chat.id, s + ' = ' + res)
    logger(update.effective_chat.id, s, res)

    context.bot.send_message(update.effective_chat.id, 'Посчитаем ещё?\n(да/нет)')
    return A

start_handler = CommandHandler('start', start)
answer_handler = MessageHandler(Filters.text, answer)
cancel_handler = MessageHandler(Filters.text, cancel)
result_handler = MessageHandler(Filters.text, result)


conv_handler = ConversationHandler(entry_points=[start_handler],
                                    states={A: [answer_handler],
                                            B: [result_handler]},
                                    fallbacks=[cancel_handler])


dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle() 

    
