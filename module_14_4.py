from aiogram import Bot, types, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import initiate_db, get_all_products

api = 'API_TOKEN'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

initiate_db()

kb = ReplyKeyboardMarkup(resize_keyboard=True)
calculate = KeyboardButton('Рассчитать')
info = KeyboardButton('Информация')
buy = KeyboardButton('Купить')
kb.add(calculate, info, buy)

inline_kb = InlineKeyboardMarkup()
inline_calculate = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
inline_formulas = InlineKeyboardButton('Формула расчета', callback_data='formulas')
inline_kb.add(inline_calculate, inline_formulas)

product_kb = InlineKeyboardMarkup()
product1 = InlineKeyboardButton('Product1', callback_data='product_buying')
product2 = InlineKeyboardButton('Product2', callback_data='product_buying')
product3 = InlineKeyboardButton('Product3', callback_data='product_buying')
product4 = InlineKeyboardButton('Product4', callback_data='product_buying')
product_kb.add(product1, product2, product3, product4)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью. Выберите действие:', reply_markup=kb)

@dp.message_handler(text='Рассчитать')
async def main_menu(message: types.Message):
     await message.answer('Выберите опцию:', reply_markup=inline_kb)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer('Формула Миффлина-Сан Жеора: 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(г) - 161')
    await call.answer()

@dp.callback_query_handler(text='calories')
async def set_age(call: types.CallbackQuery):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])


    calories = 10 * weight + 6.25 * growth - 5 * age - 161
    await message.answer(f'Ваша норма калорий: {calories} ккал в день')
    await state.finish()

@dp.message_handler(text='Купить')
async def get_buying_list(message: types.Message):
    for i in range(1, 5):
        await message.answer(f'Название: Product{i} | Описание: описание {i} | Цена: {i * 100}')
        await message.answer_photo(photo=open(f'product{i}.jpg', 'rb'))
    await message.answer('Выберите продукт для покупки:', reply_markup=product_kb)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@dp.message_handler()
async def all_messages(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



