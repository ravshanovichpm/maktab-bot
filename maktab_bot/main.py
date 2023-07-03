import logging
import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = '5992006176:AAE-uprtVKllQKDLbi-2BDuf420C5GC7-ZM'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['maktab', 'urok'])
async def send_welcome(message: types.Message):
    await message.reply("Assalamu aleykum")

bosh_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Fizra"),
            KeyboardButton(text="O'zbekiston tarixi"),
            KeyboardButton(text="Geografiya"),
        ],
        [
            KeyboardButton(text="Ingliz tili"),
            KeyboardButton(text="Jahon tarixi"),
            KeyboardButton(text="Matematika")
        ],
    ],
    resize_keyboard=True
)

@dp.message_handler(text="Matematika")
async def echo(message: types.Message):
        # 1 - savol
    await message.answer_poll(
        question="2x2",
        options=["3", "4", "5"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz"
    )

    # 2 - savol
    await message.answer_poll(
        question="2x3",
        options=["6", "4", "5"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )





# @dp.message_handler(text="Fizra")
# async def send_welcome(message: types.Message):
#     await message.answer_poll(
#                               question="Какой самый известный вид спорта?",
#                               options=["Баскетбол", "Футбол", "Хоккей"],
#                               is_anonymous=False,
#                               correct_option_id=1,
#                               type="quiz"
#         )
#     await message.answer_poll(
#                               question="У кого больше всех кубка Лиги Чемпионов?",
#                               options=["Милан", "Ливерпуль", "Реал Мадрид"],
#                               is_anonymous=False,
#                               correct_option_id=2,
#                               type="quiz"
#         )
#     await message.answer_poll(
#                               question="В каком году Майкл Джордон закончил карьеру?",
#                               options=["2001/2002", "2005/2006", "2002/2003"],
#                               is_anonymous=False,
#                               correct_option_id=2,
#                               type="quiz"
#         )
#     await message.answer_poll(
#                               question="В каком году умер известный баскетболист Коби Брайнт?",
#                               options=["2020", "2021", "2019"],
#                               is_anonymous=False,
#                               correct_option_id=0,
#                               type="quiz"
#         )
#     await message.answer_poll(
#                               question="В каком году ввели уроки физкультуры в Узб?",
#                               options=["27 мая 1998 г.", " 27 мая 1999 г.", "27 мая 2000 г."],
#                               is_anonymous=False,
#                               correct_option_id=1,
#                               type="quiz"
#         )









@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)