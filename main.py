# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 20:00:00 2023
Приручаем Python 12 ИИ пишем бот "диетолог и мониторинг здоровья" ч.1 ТЗ
@author: gorelyi
""" 




import telebot
import sqlite3
from telebot import types
from food_module import *
from meds_module import *
from tests_module import *

# Инициализация бота
bot = telebot.TeleBot(TOKEN)

# Создание базы данных питомцев
def create_pets_db():
    conn = sqlite3.connect("pets_db.db")
    cursor = conn.cursor()

    # Создание таблицы питомцев
    cursor.execute('''CREATE TABLE IF NOT EXISTS pets (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INT,
                        pet_name TEXT,
                        username TEXT,
                        token_api TEXT
                    )''')

    conn.commit()
    cursor.close()
    conn.close()

# Подключение к базе данных питомцев
def connect_to_pets_db():
    conn = sqlite3.connect("pets_db.db")
    cursor = conn.cursor()
    return conn, cursor

# Инициализация базы данных
def initialize_database():
    create_pets_db()

# Обработка ошибок
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_exceptions(callback_query):
    try:
        raise callback_query.exception
    except Exception as e:
        # Обработка ошибок
        print(f"Error occurred: {e}")

# Инициализация базы данных
initialize_database()

# Кнопки клавиатуры
def create_main_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    row_btn1 = types.InlineKeyboardButton("Выбрать питомца", callback_data='select_pet')
    row_btn2 = types.InlineKeyboardButton("Добавить питомца", callback_data='add_pet')
    row_btn3 = types.InlineKeyboardButton("Удалить питомца", callback_data='delete_pet')
    keyboard.add(row_btn1, row_btn2, row_btn3)
    return keyboard

@bot.message_handler(commands=['start'])
def start(message):
    # Обработка стартовой команды /start
    # Отображение стартового меню
    keyboard = create_main_keyboard()
    bot.send_message(message.chat.id, "Выберите одну из команд:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == 'select_pet':
        select_pet_handler(call)
    elif call.data == 'add_pet':
        add_pet_handler(call)
    elif call.data == 'delete_pet':
        delete_pet_handler(call)

def select_pet_handler(call):
    # Обработка выбора питомца
    pass

def add_pet_handler(call):
    # Обработка добавления питомца
    pass

def delete_pet_handler(call):
    # Обработка удаления питомца
    pass

# Запуск бота
bot.polling()