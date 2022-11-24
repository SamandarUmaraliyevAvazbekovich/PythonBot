from aiogram import Bot, Dispatcher, executor, types
from doc import API_key

bot = Bot(API_key)
dp = Dispatcher(bot)

START_text = 'Botimizga hush kelibsiz!!! /help -> help'

Help_text = '''
/ - bu kamanda
/start - botni ishga tushirish
/help - Hamma komandalar
va echo agar comanda bolmasa
'''

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
	await message.answer(text=START_text)
	await message.delete()

@dp.message_handler(commands=['help'])
async def hel(message : types.Message):
	await message.reply(text=Help_text)

@dp.message_handler()
async def echo(message:types.Message):
	await message.answer(text=message.text)


if __name__ == '__main__':
	executor.start_polling(dp)





