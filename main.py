import os
from decouple import config
import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types
# from iexfinance.refdata import get_symbols
# from iexfinance.stocks import Stock

# SECRET_KEY    = config('SECRET_KEY')
# PUBLIC_KEY    = config('PUBLIC_KEY')
TELEGRAM_KEY  = config('TELE_API')

print(TELEGRAM_KEY)

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TELEGRAM_KEY)
dp = Dispatcher(bot)
# stock_symbols = get_symbols(token=SECRET_KEY, output_format='json')

# print(stock_symbols[0])

# a = Stock("TLK", output_format="json", token=SECRET_KEY)
# price = a.get_quote()['delayedPrice']

watch_list = dict()

def input_func(input):
    return len(input.text.split()) == 2


# @bot.message_handler(func=input_func)
@dp.message_handler()
async def add_watch_list(message: types.Message):

    item, count = message.text.split()
    await message.answer('Your number is: ' + item + ' ' + count)

    watch_list[item] = int(count)
    # print(watch_list)
    await alert_watch_list(len(watch_list))

async def alert_watch_list(size):

    n = size

    while watch_list:
        print(watch_list)

        if n != len(watch_list):
            break

        # if size != size:
        #   break

        for item, count in watch_list.items():
            if count < 2:
                # bot.send_message(message, item + ' is less than $2')
                print(item + " is less than 2")
                del watch_list[item]
                break
            watch_list[item] -= 1

        await asyncio.sleep(5)

        if n != len(watch_list):
            break

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)