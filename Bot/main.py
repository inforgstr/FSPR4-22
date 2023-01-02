from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
from data import buttons
from aiogram.dispatcher.filters import Text


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

merger = types.InlineKeyboardMarkup(row_width=1).add(buttons.btn1, buttons.btn2)

@dp.message_handler(commands=["start"])
async def start(message: types.Message) -> None:
    await message.answer("Tilni tanlang\nВыберите язык", reply_markup=merger)


@dp.callback_query_handler(text="2")
async def uz_lang(callback: types.CallbackQuery):
    back = types.InlineKeyboardButton("<< Назад", callback_data="back2")
    markup = types.InlineKeyboardMarkup(row_width=2).add(
        buttons.r1, buttons.r2, buttons.r3, buttons.r4, buttons.r5, buttons.r6, buttons.r7, buttons.r8, buttons.r9, buttons.r10, buttons.r11, back
    )
    await callback.message.edit_text("Выберите регион:", reply_markup=markup)




@dp.callback_query_handler(text="1")
async def ru_lang(callback: types.CallbackQuery):
    back = types.InlineKeyboardButton("<< ОРКАГА", callback_data="back1")
    markup = types.InlineKeyboardMarkup(row_width=2).add(
        buttons.u1, buttons.u2, buttons.u3, buttons.u4, buttons.u5, buttons.u6, buttons.u7, buttons.u8, buttons.u9, buttons.u10, buttons.u11, back
    )
    await callback.message.edit_text("Туманни танланг", reply_markup=markup)

@dp.callback_query_handler(text="back1")
async def call(name: types.CallbackQuery):
    await name.message.edit_text("Тилни танланг\nВыберите язык", reply_markup=merger)

@dp.callback_query_handler(text="back2")
async def callv(name: types.CallbackQuery):
    await name.message.edit_text("Тилни танланг\nВыберите язык", reply_markup=merger)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
