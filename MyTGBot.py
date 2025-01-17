
import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

API_TOKEN = '6594700995:AAFLXikhb3-1-kGgB9HZB9nfyrBxOaB0xMg'

bot = telebot.TeleBot(API_TOKEN)

cities = ['Вінниця', 'Дніпро', 'Житомир', 'Івано-Франківськ', 'Київ', 'Кропивницький', 'Луцьк', 'Львів', 'Миколаїв',
          'Одеса', 'Полтава', 'Рівне', 'Суми', 'Тернопіль', 'Ужгород', 'Харків', 'Хмельницький', 'Чернівці', 'Черкаси',
          'Чернігів']

excursion = {
    'Вінниця': {
        'Подорож двоповерховим автобусом Bus Pass': {
            'price': '1200',
            'data': 'Щосуботи та неділі',
            'time': 'Початок о 6:00',
            'meeting': 'Центральний автовокзал',
            'description': 'Маршрут екскурсії прямує через всі визначні точки міста — фонтан Roshen, головну вулицю '
                           'Вінниці — Соборну до Національного музею-садиби М. Пирогова, а потім повертається назад, '
                           'до Центрального автовокзалу.',
        },
        'Шляхетна Вінниччина. Матриця (проєкт-трилогія': {
            'price': '2000',
            'data': 'Щоп\'ятниці',
            'time': 'Початок о 6:00',
            'meeting': 'Центральний автовокзал',
            'description': 'Маршрут пролягає через Вороновицю з палацом Ґрохольських і Музеєм повітроплавання та '
                           'Немирів з паровим млином-електростанцією, палацом княгині Щербатової і таємничими '
                           '“Скіфськими Валами”. Також ви побуваєте у столиці “Щедрика” Тульчині, де розташований '
                           'найвеличніший у Європі 18 ст. палац графа Станіслава Щенсного Потоцького та Музей '
                           'аптечної справи, завітаєте у село Печера з парком і мавзолеєм Потоцьких, і побачите '
                           'заворожуючий млин у Сокільці. А родзинкою екскурсії стане обід в найкращих подільських '
                           'традиціях.',
        },
        'Два полюси одного міста': {
            'price': '250',
            'data': 'Щонеділі',
            'time': 'Початок о 7:00',
            'meeting': 'Центральний автовокзал',
            'description': 'Під час екскурсії ми побуваємо на Старому місті, де розташовувався один із перших замків на'
                           'території міста ― на Замковій горі, зайдемо у старовинну Миколаївську церкву, збудовану у '
                           'стилі козацького бароко, почуємо історію міста від започаткування до сучасності, проїдемо '
                           'вузькими вуличками Нового міста повз величні Мури, особняки кінця 19 ― початку 20 '
                           'сторіччя.',
        },
        'Вінниця: подорож у часі': {
            'price': '250',
            'data': 'Щосереди та п\'ятниці',
            'time': 'Початок о 16:00 та 18:00',
            'meeting': 'Центральний автовокзал',
            'description': 'Історія вулиці невід’ємна від історії українського народу. Прогулюючись вулицею Оводова, '
                           'можна відтворити у пам’яті найяскравіші сторінки минулого: від стародавніх язичницьких '
                           'капищ на схилі річки Бог та вінницького замку, збудованого Костянтином Острозьким, до '
                           'складного періоду боротьби за державність УНР, коли Вінниця тимчасово стає столицею '
                           'України, за утвердження радянської влади у місті. Далі — боротьба з нацистами, повоєнна '
                           'відбудова та сьогодення затишного міста над Бугом.',
        },
    },
    'Дніпро': {
        'Легенди вечірнього Дніпра': {
            'price': '300',
            'data': 'Щоп\'ятниці',
            'time': 'Початок о 18:00',
            'meeting': 'пам\'ятник Аксельроду',
            'description': 'Ми відправимось у мандрівку у минуле нашого міста. Побачимо старі будівлі, які ще '
                           'пам’ятають Катеринослав та його мешканців. Дізнаємось їх історію та цікаві легенди. '
                           'Знайдемо « катеринославську» цеглу та річку у центрі міста. Побачимо « плаский» будинок з '
                           'однією стіною, зазирнемо у таємні дворики та знайдемо « казковий будиночок». Відчуємо '
                           'енергетику старого та ритм сучасного міста.',
        },
        'Поїздка до Петриківки, Миколин хутір та кінна ферма': {
            'price': '810',
            'data': '20 липня',
            'time': 'Початок о 9:00',
            'meeting': 'Виїзд від пам\'ятника Маргелову, вул. Січеславська Набережн',
            'description': 'Ми завітаємо до музею-садиби "Миколин хутір". Микола та Валентина Деки, подружжя-художників'
                           '– створили у своєму будинку казковий та різнокольоровий світ. Це не проста українська хата,'
                           'це картина, в якій поєдналися квіти різноманітних форм та відтінків, краєвиди українського '
                           'села, зображення тварин та різні орнаменти. Господарі будинку гостинно приймають гостей і '
                           'проводять для них майстер-класи з Петриківського розпису.'
                           'Також, у садибі ви познайомитесь з традиціями та побутом Запорізьких козаків, побачите '
                           'старовинні деталі інтер\'єру, такі як ткацький верстат та українська піч, зможете приміряти' 
                           'та сфотографуватися на згадку у національних костюмах.',
        },
        'До Петриківки на Купала: музей Петриківського розпису, етно-хутір "Козацька Січ"': {
            'price': '720',
            'data': '6 липня',
            'time': 'Початок 9:00',
            'meeting': 'Виїзд групи від турцентру "Риба Андрій" (пам\'ятник Маргелова, вул.Січеславська Набережна,15а)',
            'description': 'За старовинним українським звичаєм святкуємо Івана Купала на колоритному етно-хуторі!'
                           'Тут ви дізнаєтесь щось нове про своє коріння, а може, просто згадаєте забуте.'
                           'Вже біля самих воріт вас гостинно зустрітимуть господарі та запропонують хліба з сіллю та '
                           'чарочку горілки з козацької шаблюки. Після екскурсії хутором вас чекають виступ '
                           'фольклорного ансамблю, традиції та легенди, майстер-класи, обрядові пісні та танці, '
                           'традиційні ігри та розваги. Будь весело та колоритно, приєднуйтесь!',
        },
    },
    'Житомир': {
        'Вулиця Михайлівська': {
            'price': '220',
            'data': 'Щочетверга',
            'time': '14:00',
            'meeting': 'Пам’ятний знак з нагоди 1100 річчя заснування м. Житомира',
            'description': 'Вулиця Михайлівська – одна із центральних вулиць міста Житомира. Бере початок від майдану '
                           'Сергія Корольова, вулиці Великої Бердичівської і з’єднує його з вулицею Київською біля '
                           'Свято-Михайлівського кафедрального собору. Її довжина 370 метрів, що дозволило тут '
                           'розмістити сучасну інсталяцію «Парасолька», яка стала інстаграмним місцем для містян та '
                           'гостей міста Житомир.',
        },
        'Житомир - місто древнє': {
            'data': 'Щопонеділка та п\'ятниці',
            'time': 'Початок о 15:00',
            'meeting': 'Житомирський замок',
            'description': 'У нашому Місті безліч дивних місць, які ми не помічаємо в щоденній метушні.'
                           'Зупиніться на хвилину, прислухайтеся до музики міста. Помилуйтеся його унікальним '
                           'ландшафтом, доторкніться до його вічної краси. Ми хочемо запропонувати Вам цікаву пішохідну'
                           'екскурсію по Житомиру з тими, хто любить і знає це місто, для кого кожна вулиця, кожен '
                           'будинок Міста.',
        },
        '"Український" Житомир - "українськими" очима': {
            'data': 'Щодня',
            'time': 'Початок о 13:00 та 16:00',
            'meeting': '',
            'description': 'Тема цієї екскурсії, на перший погляд, викликає подив: а, яким же іще має бути місто в '
                           'самому центрі України? Насправді Житомир відомий як історично багатонаціональне місто. Та '
                           'ніхто ніколи не переймався метою побачити роль в його історії титульної нації, з’ясувати '
                           'саме «українські» адреси, постаті, події…Їх виявляється чимало. На запланованому маршруті, '
                           'екскурсанти «Патріота», як завжди, зроблять для себе багато відкриттів і побачать '
                           '«український Житомир» – «українськими очима».',
        },
    },
    'Івано-Франківськ': {
        'Підземелля ратуші': {
            'price': '200',
            'data': 'Щодня',
            'time': 'Початок о 16:00',
            'meeting': 'Ратуша',
            'description': 'Запрошуємо вас у саме серце історії нашого міста! Відтепер у нас є неймовірна можливість '
                           'розгадати таємниці минулого, оглядаючи підземелля Ратуші, котрі колись служили в\'язницею. '
                           'Старовинні підвали стали осередком тематичної експозиції, яку оживляють вражаючі звукові '
                           'та світлові ефекти.',
        },
        'Івано-Франківськ - місто, що завжди з тобою': {
            'price': '700',
            'data': 'Щодня',
            'time': 'Початок о 16:00',
            'meeting': 'Початок від пам’ятника Івана-Франка',
            'description': 'Захоплююча пішохідна екскурсія історичною частиною Івано-Франківська. Початок від '
                           'пам’ятника Івана-Франка - Драматичний театр -  вул. Незалежності, кам’яниця Басcа – Вічевий'
                           'майдан – Катедральний собор -  площа Шептицького – Бастіон -  вул. Низова – Ратуша – '
                           'Вірменська церква – пам’ятник на Валах –  палац Потоцьких - Синагога – Філармонія – сквер '
                           'А.Міцкевича – товариство Сокіл - вул. Незалежності.',
        },
        'Романтичний Франківськ': {
            'price': '700',
            'data': 'Щодня',
            'time': 'під запит',
            'meeting': 'Початок від пам’ятника Івана-Франка',
            'description': 'Івано-Франківськ - це місто романтичних прогулянок та побачень, де "кожна вуличка, мов'
                           'карамелька - коротка, солодка й твоя" ... Запрошуємо на прогулянку вуличками, скверами та '
                           'площами міста, які відкриють Вам свої романтичні історії та легенди.',
        },
    },
    'Київ': {
        'Екскурсія "Літописні місця Печерська"': {
            'price': '300',
            'data': '27 липня',
            'time': 'Початок о 17:00',
            'meeting': ' біля гармати, метро Арсенальна',
            'description': 'Запрошуємо на променад однією з найстаріших і найкрасивіших місцевостей Печерська. Ми '
                           'побуваємо там, де відбувся перший державний переворот, згадаємо князів-християн, з\'ясуємо,'
                           'які історії можуть розповісти нам пам\'ятники.',
        },
        'Екскурсія "Вечерня прогулянка Подолом"': {
            'price': '300',
            'data': 'Щодня',
            'time': 'Початок о 17:00',
            'meeting': 'на перетині вулиць Андріївський узвіз і Боричів Тік,поруч пам\'ятника Вертинському',
            'description': 'Запрошуємо вас на легку прогулянку атмосферним Подолом. Ми з вами простежимо, як змінився '
                           'цей своєрідний район за останні 20 років, які з цих змін його прикрасили, а які навпаки – '
                           'стали його монстрами.',
        },
        'Екскурсія "Містика і язичництво київських гір"': {
            'price': '400',
            'data': 'Щодня',
            'time': 'Початок о 18:00',
            'meeting': 'Контрактова площа, біля пам\'ятника Сковороді',
            'description': 'Ми піднімемося на один з найдавніших і найзагадковіших київських пагорбів - Замкову гору, '
                           'відшукаємо сучасні капища в центрі міста, де щотижня проводять свої обряди і '
                           'жертвоприношення неоязичники-рідновіри, пройдемо через закинуте кладовище, щоб побачити '
                           'мальовничі краєвиди, від яких перехоплює подих, і почути не менш захоплюючі історії, '
                           'міські перекази і байки (а десь і подільські базарні плітки) та містичні легенди про '
                           'красунь-відьом і перевертнів-вовкулак.',
        },
    },
    'Кропивницький': {
        'Тюльпанова казка дендропарку': {
            'price': '500',
            'data': 'Щодня',
            'time': 'Початок о 12:00',
            'meeting': 'Дендропарк',
            'description': 'Під час екскурсії гості знайомляться з «тюльпановим дивом», «українською Голандією» - '
                           'Кропивницьким Дендропарком в період цвітіння більш ніж трьох мільйонів ...',
        },
        'Театральний калейдоскоп': {
            'price': '500',
            'data': 'Щосереди',
            'time': 'Початок о 19:00',
            'meeting': 'Дендропарк',
            'description': 'Театральний калейдоскоп (пішохідна, 2 год, з екскурсією у театрі – 3 год)',
        },
        'Історична скарбниця міста': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
    },
    'Луцьк': {
        'Гастрономічний Луцьк': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
        'Середньовічний Лучеськ + підземелля': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
        'Гастрономічна екскурсія для дітей': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
    },
    'Львів': {
        'Оглядова екскурсія по історичному центру Львова': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
        'Автобусна оглядова екскурсія по Львову на мікроавтобусі': {
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
        'Екскурсія Львів для школярів + шоколадний майстер-клас і квест, або замки, на 1-3 дні': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
        'Екскурсія “Підземелля Львова” та підземні дегустації для дорослих й ігри для дітей': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
    },
    'Миколаїв': {
        'Храми Миколаєва': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
        'Історія  однієї вулиці (гуляємо по Наваринській )': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
        'Архітектура старого міста': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
    },
    'Одеса': {
        'Одеські дворики': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
        'Палаці Одеси та їхні мешканці': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
        'Історія міста у мініатюрі. Вулиця Маразлієвська': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
    },
    'Полтава': {
        'Швидкий бліц Полтавою': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
        'Знайомство з Полтавою': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
        'Полтава та околиці': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
    },
    'Рівне': {
        'Подорож вузькоколійною залізницею Антонівка-Біле': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
        'Історичний Городок': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
        'Дубно – княжа столиця на Волині': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
    },
    'Суми': {
        'ЦІКАВИНКИ РІДНОГО МІСТА АБО КОНТАКТНІ СКУЛЬПТУРИ СУМ': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
        '"КАЗКОВЕ" МІСТО СУМИ': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
        'ОГЛЯДОВА ЕКСКУРСІЯ МІСТОМ СУМИ': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
    },
    'Тернопіль': {
        'ТУНЕЛЬ КОХАННЯ + ТЕРНОПІЛЬЩИНА': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
        'Свято-Успенська Почаївська лавра': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
        'Тунель Кохання в Клевані': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
    },
    'Ужгород': {
        'Еко-екскурсія по Закарпаттю': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
        'Індивідуальна екскурсія по Ужгороду': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
        'Одноденний тур: сходження на Говерлу': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
    },
    'Харків': {
        'Індивідуальна екскурсія Харковом на авто': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
        'Таємниці міста: подорож з Харківським Домовиком': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
        'Як харківці Новий рік святкували: подорож з харківським домовиком': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
        'Екскурсія по місцях, де збуваються бажання: цікавий Харків': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
        'Добра магія. Містична екскурсія по Харкову': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
        'Харків під градусом. Алко-екскурсія містом': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        }

    },
    'Хмельницький': {
        'Атмосферна екскурсія «Романтика Проскурівського модерну»': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
        '«У пошуках середньовічної Плоскирівської фортеці»': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
        'Атмосферна екскурсія пам’ятниками міста «Хмельницький монументальний: від Богдана до Богдана»': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
    },
    'Чернівці': {
        '"А НА ТОМУ БОЦІ, ТАМ ЖИВЕ МАРІЧКА..."': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
        'ТРАНСФАГАРАШСЬКЕ ШОСЕ, ОЗЕРО БАЛЕА + ЗАМКИ ДРАКУЛИ': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
        'НА ЯХТІ ДО БАКОТИ + ШИШКОВІ ГОРБИ': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
        '5 ЗАМКІВ ПОДІЛЛЯ - БУЧАЧ, ЧОРТКІВ, ЯЗЛОВЕЦЬ, РУКОМИШ': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
    },
    'Черкаси': {
        'ГІРСЬКОЛИЖНИЙ КОМПЛЕКС “ВОДЯНИКИ”': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
        'БУКИ + КІННО-СПОРТИВНИЙ КОМПЛЕКС «PARADE ALLURE» В ЖАШКОВІ': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
        'ЕКСКУРСІЯ «ЧИГИРИН – СУБОТІВ – ХОЛОДНИЙ ЯР»': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
        'ЕКСКУРСІЯ В КАНІВ': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
    },
    'Чернігів': {
        'Місто-фортеця: Екскурсія до Чернігова + Седнів': {
            'price': '',
            'data': '',
            'time': '',
            'meeting': '',
            'description': '',
        },
    },
}


markup = InlineKeyboardMarkup()

for city in cities:
    button = InlineKeyboardButton(city, callback_data=f'city{city}')
    markup.add(button)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        'Привіт. Я бот, який надає інформацію про наявні екскурсії в містах України.\n'
        'Виберіть місто:',
        reply_markup=markup
    )


# def additional_buttons(city, text):
#     markup = InlineKeyboardMarkup(row_width=2)
#     markup.add(
#         InlineKeyboardButton('Повернутися до розділу з містами', callback_data='back_to_cities'),
#         InlineKeyboardButton('Повернутися до розділу з екскурсіями', callback_data=f'{city}_excursions'),
#         InlineKeyboardButton('Зберегти екскурсію', callback_data=f'save{city}{text}'),
#         InlineKeyboardButton('Переглянути збережені екскурсії', callback_data='view_saved')
#     )
#     return markup


@bot.callback_query_handler(func=lambda call: call.data.startswith('city'))
def han(call):
    city = call.data[len('city'):]
    excursion_markup = InlineKeyboardMarkup()

    for text, excursion_name in enumerate(excursion.get(city, {})):
        button = InlineKeyboardButton(excursion_name, callback_data=f'{city}exc{text}')
        excursion_markup.add(button)

    bot.send_message(call.message.chat.id, f'Екскурсії в місті {city}:', reply_markup=excursion_markup)
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: any(call.data.startswith(f'{city}exc') for city in cities))
def sit(call):
    for city in cities:
        if call.data.startswith(f'{city}exc'):
            text = int(call.data[len(city) + len('exc'):])
            excursion_name = list(excursion[city].keys())[text]
            excursion_info = excursion[city][excursion_name]
            info_text = (
                f'Екскурсія: {excursion_name}\n'
                f'Ціна: {excursion_info['price']}\n'
                f'Дата: {excursion_info['data']}\n'
                f'Час: {excursion_info['time']}\n'
                f'Місце зустрічі: {excursion_info['meeting']}\n'
                f'Опис: {excursion_info['description']}'
            )

            bot.send_message(call.message.chat.id, info_text)
            bot.answer_callback_query(call.id)


bot.polling()
