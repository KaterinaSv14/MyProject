
import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

API_TOKEN = '6594700995:AAFLXikhb3-1-kGgB9HZB9nfyrBxOaB0xMg'

bot = telebot.TeleBot(API_TOKEN)

cities = ['Вінниця', 'Дніпро', 'Житомир', 'Івано-Франківськ', 'Київ', 'Кропивницький', 'Луцьк', 'Львів', 'Миколаїв',
          'Одеса', 'Полтава', 'Рівне', 'Суми', 'Тернопіль', 'Ужгород', 'Харків', 'Хмельницький', 'Чернівці', 'Черкаси',
          'Чернінів']

markup = InlineKeyboardMarkup()

for city in cities:
    button = InlineKeyboardButton(city, callback_data=city)
    markup.add(button)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        'Привіт. Я бот, який надає інформацію про наявні екскурсії в містах України.\n'
        'Виберіть місто:',
        reply_markup=markup
    )


@bot.message_handler(func=lambda message: message.text in cities)
def send_tours(message):
    selected_city = message.text


excursion = {
    'Вінниця': ['Подорож двоповерховим автобусом Bus Pass', ''],
    'Дніпро': [],
    'Житомир': [],
    'Івано-Франківськ': [],
    'Київ': [],
    'Кропивницький': [],
    'Луцьк': [],
    'Львів': [],
    'Миколаїв': [],
    'Одеса': [],
    'Полтава': [],
    'Рівне': [],
    'Суми': [],
    'Тернопіль': [],
    'Ужгород': [],
    'Харків': [],
    'Хмельницький': [],
    'Чернівці': [],
    'Черкаси': [],
    'Чернінів': [],
}

bot.polling()
