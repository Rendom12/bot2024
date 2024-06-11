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



available = ["Что-то планируете продать из сельхозтехники?", "Что планируете покупать из сельхозтехники б/У?"]
start_keyboards = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=available[0])], [KeyboardButton(text= available[1])]], resize_keyboard=True)