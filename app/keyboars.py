from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Первая")],
                                     [KeyboardButton(text="Вторая")],
                                     [KeyboardButton(text="Третья"),
                                      KeyboardButton(text="Четвертая")]],
                           resize_keyboard=True,
                           input_field_placeholder="ля-ля Тополя"
                           )

get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Отправить номер",
                                                           request_contact=True)]],
                                                           resize_keyboard=True)