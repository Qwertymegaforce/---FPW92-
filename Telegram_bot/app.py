from config import token, values, count, convert_start, shedule_start
import telebot
from telebot import types
import requests
import time
import json
from exceptions import BotError



bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, f"""Привет {message.chat.first_name}""")
    time.sleep(1)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    help = types.KeyboardButton('/help')
    shedule = types.KeyboardButton('/shedule')
    convert = types.KeyboardButton('/convert')
    markup.add(help, shedule, convert)
    bot.send_message(message.chat.id, """Я MultiToolBotBot
Я умею:
    
▶️Конвертировать валюту 💵💵💵
▶️Выводить расписание для университетской группы моего создателя
    
/help - увидеть все команды

Ну или можно просто воспользоваться кнопками ниже 💁‍♂️
        
    """, reply_markup=markup)
    time.sleep(0.5)

    bot.send_message(message.chat.id, 'А еще у моего создателя плохое чувство юмора 🤡🤡🤡')


@bot.message_handler(commands=['help'])
def help_em(message):
    global count
    if count == 0:
        bot.reply_to(message, f'Бог поможет')
        with open ('man_meme.webp', 'rb') as meme:
            bot.send_document(message.chat.id, meme)
        count += 1
        time.sleep(3.5)
        bot.send_message(message.chat.id, 'Ладно, это шутка!')

    bot.send_message(message.chat.id, """

▶️ Командой /help можно вызвать это окно 😑

▶️ Командой /shedule можно вызвать окно с расписанием 🕔

▶️ Командой /convert вызывается конвертор валют - туда надо передать данные следующим образом: 

    ↘️ "биткоин доллар  2" 🔜 получите цену биткоина в долларе
    
    ↘️ Доступные валюты:
        ✔️Доллар
        ✔️Биткоин
        ✔️Эфир
    
    """ )

@bot.message_handler(commands=['shedule'])
def show_info(message):
    global convert_start
    convert_start = False
    bot.reply_to(message, f"""Ваша группа?
    
↪️Можете поробовать мою - 720811.

⚠️Сайт очень часто не работает))

""")
    global shedule_start
    shedule_start = True


@bot.message_handler(commands=['convert'])
def start(message):
    global shedule_start
    shedule_start = False
    bot.reply_to(message, 'Конвертор запущен ✅')
    global convert_start
    convert_start = True


@bot.message_handler(func=lambda x: convert_start == True)
def convertation(sms):
    try:
        check_input = sms.text.split(' ')

        if len(check_input) != 3:
            raise BotError('Неверное количество элементов ⁉️')
    except BotError as b:
        bot.send_message(sms.chat.id, f'{b}')

    try:
        fsym, tsym, multiplier = sms.text.lower().split(' ')

    except ValueError:
        pass

    try:
        global convert_start
        BotError.check(fsym, tsym, multiplier)
        request = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={values[fsym]}&tsyms={values[tsym]}')
        total_base = json.loads(request.content)
        answer = total_base[values[tsym]] * float(multiplier)
        final = f' 📌 Цена {multiplier} {values[fsym]} в {values[tsym]} = {answer}'
        bot.reply_to(sms, f'{final}')
        convert_start = False

    except BotError as e:
        bot.send_message(sms.chat.id, f'{e}')

    except UnboundLocalError:
        pass





@bot.message_handler(func=lambda x: shedule_start == True)
def show_shedule(sms):
    try:
        global shedule_start
        BotError.check_schedule(sms.text)
        url = f'https://schedule.tsu.tula.ru/?group={sms.text}'
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('📎 Сайт', url=url))
        bot.send_message(sms.chat.id, 'Сайт с расписанием', reply_markup=markup)
        shedule_start = False

    except BotError as f:
        bot.send_message(sms.chat.id, f'{f}')

@bot.message_handler(content_types=['text'])
def respond(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Жми сюда 🤌', url='https://allcalc.ru/node/1977'))
    bot.send_message(message.chat.id, f' 11010000 10101111 00100000 11010000 10111101 11010000 10110101 00100000 11010000 10111111 11010000 10111110 11010000 10111101 11010000 10111000 11010000 10111100 11010000 10110000 11010001 10001110 00101100 00100000 11010001 10000111 11010001 10000010 11010000 10111110 00100000 11010001 10000010 11010001 10001011 00100000 11010000 10110011 11010000 10111110 11010000 10110010 11010000 10111110 11010001 10000000 11010000 10111000 11010001 10001000 11010001 10001100 00101100 00100000 11010000 10111010 11010000 10110000 11010000 10111010 00100000 11010001 10000010 11010001 10001011 00100000 11010001 10000001 11010000 10110101 11010000 10111001 11010001 10000111 11010000 10110000 11010001 10000001 00100000 11010000 10111101 11010000 10110101 00100000 11010000 10111111 11010000 10111110 11010000 10111101 11010000 10111000 11010000 10111100 11010000 10110000 11010000 10110101 11010001 10001000 11010001 10001100 00101100 00100000 11010001 10000111 11010001 10000010 11010000 10111110 00100000 11010000 10110011 11010000 10111110 11010000 10110010 11010000 10111110 11010001 10000000 11010001 10001110 00100000 11010001 10001111 00101110 00100000 11010000 10011000 11010001 10000001 11010000 10111111 11010000 10111110 11010000 10111011 11010001 10001100 11010000 10110111 11010001 10000011 11010000 10111001 00100000 11010000 10111010 11010000 10111110 11010000 10111100 11010000 10110000 11010000 10111101 11010000 10110100 11010001 10001011 00100001', reply_markup=markup)

@bot.message_handler(content_types=['photo'])
def respond(message):
    with open('random.jpg', 'rb') as XD:
        bot.reply_to(message, f'Я не понимаю, что на этой картинке, также как ты не поймешь, что на этой 👇')
        bot.send_document(message.chat.id, XD)




bot.polling(none_stop=True)











