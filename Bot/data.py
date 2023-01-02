from aiogram import types


class Buttons:
    def __init__(self):
        # Языки
        self.btn1 = types.InlineKeyboardButton("🇺🇿 Uzbek", callback_data="1")
        self.btn2 = types.InlineKeyboardButton("🇷🇺 Русский", callback_data="2")

        # lang - uz:
        # Туманлар

        self.u1 = types.InlineKeyboardButton("Бектемир тумани", callback_data="1_1")
        self.u2 = types.InlineKeyboardButton("Миробод тумани", callback_data="1_2")
        self.u3 = types.InlineKeyboardButton("Мирзо Улуғбек тумани", callback_data="1_3")
        self.u4 = types.InlineKeyboardButton("Сергели тумани", callback_data="1_4")
        self.u5 = types.InlineKeyboardButton("Олмазор тумани", callback_data="1_5")
        self.u6 = types.InlineKeyboardButton("Учтепа тумани", callback_data="1_6")
        self.u7 = types.InlineKeyboardButton("Шайхонтоҳур тумани", callback_data="1_7")
        self.u8 = types.InlineKeyboardButton("Яшнобод тумани", callback_data="1_8")
        self.u9 = types.InlineKeyboardButton("Чилонзор тумани", callback_data="1_9")
        self.u10 = types.InlineKeyboardButton("Юнусобод тумани", callback_data="1_10")
        self.u11 = types.InlineKeyboardButton("Яккасарой тумани", callback_data="1_11")

        # lang - ru:
        # Регионы

        self.r1 = types.InlineKeyboardButton("Чиланзарский", callback_data="2_1")
        self.r2 = types.InlineKeyboardButton("Яшнабадский", callback_data="2_2")
        self.r3 = types.InlineKeyboardButton("Бектемирский", callback_data="2_3")
        self.r4 = types.InlineKeyboardButton("Сергелийский", callback_data="2_4")
        self.r5 = types.InlineKeyboardButton("Учтепинский", callback_data="2_5")
        self.r6 = types.InlineKeyboardButton("Мирабадский", callback_data="2_6")
        self.r7 = types.InlineKeyboardButton("Яккасарайский", callback_data="2_7")
        self.r8 = types.InlineKeyboardButton("Алмазарский", callback_data="2_8")
        self.r9 = types.InlineKeyboardButton("Шайхантахурский", callback_data="2_9")
        self.r10 = types.InlineKeyboardButton("Мирзо-Улугбекский", callback_data="2_10")
        self.r11 = types.InlineKeyboardButton("Юнусабадский", callback_data="2_11")


buttons = Buttons()


