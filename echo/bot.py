from aiogram import Bot,Dispatcher,executor,types
from doc import API_key


bot =Bot(API_key)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message : types.Message):
	await message.answer(text=message.text.upper())




if __name__ == '__main__':
	executor.start_polling(dp)