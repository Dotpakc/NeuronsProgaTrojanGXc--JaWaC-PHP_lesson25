# Створити математичний бот з використанням  клавіатури
# То есть теперь бот выводит в сообщении 
# ответ и предлагает ниже в кнопках варианты примеров,
# которые предположительно могут в 
# результате дать ответ, который указан выше

# Например:

# 45
# Далее 4е кнопки с вариантами примеров:
# 4 + 7 * 12
# 9 * 5
# 10 - 1 * 7
# 135 / 6
# Собственно пользователь нажимает на кнопку
# и бот проверяет правильный ли ответ, 
# то есть даст ли такой пример указанный ответ в результате)

# str 

# 4 
# +-/* 4  
# +-* 12
# +-* 12
# +-* 12


# 1lvl 80%
# 2lvl 60%
# 3lvl 40%
# 4lvl 20%

# 153

# 4-2
# 1*2
# 4/2


import random

import asyncio

from aiogram import Bot, Dispatcher, types,F
from aiogram.filters import CommandStart, Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from decouple import config

API_TOKEN = 'Token'
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

def generate_problems(minNumber=1, maxNumber=10, lvl=1, count=4):
    list_of_problems = {}
    list_znakiv = ['+', '-', '*']
    while len(list_of_problems) < count:
        probleb = f'{random.randint(minNumber, maxNumber)}'
        
        hard_lvl = random.randint(1, lvl)
        for i in range(hard_lvl):
            znak = random.choice(list_znakiv)
            second_number = random.randint(minNumber, maxNumber)
            probleb += f' {znak} {second_number}'
        
        answer = int(eval(probleb))
        if answer not in list_of_problems:
            list_of_problems[answer] = probleb
    
    return list_of_problems

def generator_markup(list_of_problems, corect_answer):
    builder = InlineKeyboardBuilder()
    for answer, problem in list_of_problems.items():
        if corect_answer == answer:
            builder.row(types.InlineKeyboardButton(text=problem, callback_data='corect'))
        else:
            builder.row(types.InlineKeyboardButton(text=problem, callback_data='wrong'))
    return builder

@dp.message(CommandStart())
async def command_start(message: types.Message):
    markup = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='Почати виклик', callback_data='start')
            ]
        ]
    )    
    await message.answer("Привіт, я бот для твоеї розумової діяльності. Якщо ти готовий до виклику, натисни кнопку 'Почати виклик'"
                         , reply_markup=markup)
    
@dp.callback_query(F.data == 'start')
async def start_game(call: types.CallbackQuery):
    problebs = generate_problems()
    corect_answer = random.choice(list(problebs.keys()))
    markup = generator_markup(problebs, corect_answer)
    await call.message.answer(f'Спробуйте відгадати:{corect_answer}', reply_markup=markup.as_markup())
    

@dp.callback_query(F.data == 'corect')
async def corect_answer(call: types.CallbackQuery):
    problebs = generate_problems()
    corect_answer = random.choice(list(problebs.keys()))
    markup = generator_markup(problebs, corect_answer)
    await call.message.edit_text(f'Молодець! Спробуй ще:{corect_answer}', reply_markup=markup.as_markup())

@dp.callback_query(F.data == 'wrong')
async def wrong_answer(call: types.CallbackQuery):
    problebs = generate_problems()
    corect_answer = random.choice(list(problebs.keys()))
    markup = generator_markup(problebs, corect_answer)
    await call.message.edit_text(f'Нажаль неправильно. Спробуй ще:{corect_answer}', reply_markup=markup.as_markup())


if __name__ == '__main__':
    asyncio.run(dp.start_polling(bot))