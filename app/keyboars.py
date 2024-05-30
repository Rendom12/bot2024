from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Первая")],
                                     [KeyboardButton(text="Вторая")],
                                     [KeyboardButton(text="Третья"),
                                      KeyboardButton(text="Четвертая")]],
                           resize_keyboard=True,
                           input_field_placeholder="ля-ля Тополя"
                           )