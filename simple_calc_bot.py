
import logging

import operator

import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)

PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}

operations = {'+': operator.add, '-': operator.sub,
              '*': operator.mul, '/': operator.truediv,
              '^': operator.pow}

def calc(bot, update):

    if len( update.message.text.split() ) < 2:
        update.message.reply_text('Error: no expression provided!')
        return None

    input = update.message.text.split()[1]

    operator_found = False
    for op_key in operations.keys():
        if op_key in input:
            operator_found = True
            arg1, arg2 = input.split(op_key)
            if arg1=='' or arg2=='':
                update.message.reply_text('Error: two operands must be provided!')
                return None
            if float(arg2) == 0 and op_key == '/':
                update.message.reply_text('Error: attempting division by 0!')
                return None
            result = operations[op_key](float(arg1), float(arg2))
            update.message.reply_text(result)
            break

    if not operator_found:
        update.message.reply_text('Error: no known arithmetical operator found!')

def main():
    # mybot = Updater("1050767852:AAGJLxpdMCIB3q_m3TtHrWaMUTj15-Nvfps", request_kwargs=PROXY)
    mybot = Updater("1050767852:AAGJLxpdMCIB3q_m3TtHrWaMUTj15-Nvfps")

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("calc", calc))

    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
