from aiogram import Bot, Dispatcher, executor, types



with open("token.txt",encoding='utf-8',mode='r') as token:
    API_TOKEN = token.read()


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start","help"])
async def send_welcome(msg: types.Message):
    await msg.reply("Я бот. Приятно познакомиться, {msg.from_user.first_name}")


@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
   if msg.text.lower() == 'привет':
       await msg.answer('Привет!')
   else:
       await msg.answer('Не понимаю, что это значит.')

if __name__ == '__main__':
    executor.start_polling(dp)
