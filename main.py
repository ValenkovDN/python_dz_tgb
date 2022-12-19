# 5794083644:AAGxADW1DOn-r_an-dnlhvyHvkzg6J9aE0s
# "Овен" or "Телец" or "Близнецы" or "Рак" or "Лев" or "Дева" or "Весы" or "Скорпион" or "Стрелец" or "Козерог" or "Водолей" or "Рыбы"

import telebot
from telebot import types
import random
token = '5794083644:AAGxADW1DOn-r_an-dnlhvyHvkzg6J9aE0s'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, " + message.from_user.first_name + "!")
    
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id, "Меня зоут Предсказамус! Я могу предсказать твое будущее в наступающем году!")
        bot.send_message(message.chat.id, "Ты хочешь получить от меня предсказание? Ответь 'Да' или 'Нет'")
    elif message.text == "Да":
        bot.send_message(message.chat.id, "Напиши свой знак зодиака")
    elif message.text == "Нет":
        bot.send_message(message.chat.id, "Не очень то и хотелось тебе предсказывать. бе-бе-бе")
    elif message.text == "Овен" or message.text == "Телец" or message.text == "Близнецы" or message.text == "Рак" or message.text == "Лев" or message.text == "Дева" or message.text == "Весы" or message.text == "Скорпион" or message.text == "Стрелец" or message.text == "Козерог" or message.text == "Водолей" or message.text == "Рыбы":
        message1 = "В наступающем году Ваша давняя мечта сбудится!"
        message2 = "Золотой шанс свалится на Вас в наступающем новом году!"
        message3 = "В новом году Вас ждет безграничное счастье!"
        message4 = "В новом году Вас ждет приятный сюрприз!"
        message5 = "В новом году Вас ждет долгое путешествие, которые оправдает ваши ожидания!"
        message6 = "Любое решение, которые вы примете в новом году, будет хорошим решением!"
        message7 = "В новом году Ваша жизнь станет намного интереснее!"
        message8 = "В новом году Вас ждет восхищение окружающих за ваши таланты и способности."
        message9 = "Куда бы вы не отправились в новом году, вас ждут приятные люди!"
        message10 = "В новом году Вас ждет обновление гардероба!"
        message11 = "В новом году Вы получите то, что хотите благодаря своему обаянию и личности"
        message12 = "Вас ожидает прибавление в семействе!"
        item = str(random.randint(1,12))
        if item == '1':
            bot.send_message(message.chat.id, message1)
        elif item == '2':
            bot.send_message(message.chat.id, message2)
        elif item == '3':
            bot.send_message(message.chat.id, message3)
        elif item == '4':
            bot.send_message(message.chat.id, message4)
        elif item == '5':
            bot.send_message(message.chat.id, message5)
        elif item == '6':
            bot.send_message(message.chat.id, message6)
        elif item == '7':
            bot.send_message(message.chat.id, message7)
        elif item == '8':
            bot.send_message(message.chat.id, message8)
        elif item == '9':
            bot.send_message(message.chat.id, message9)
        elif item == '10':
            bot.send_message(message.chat.id, message10)
        elif item == '11':
            bot.send_message(message.chat.id, message11)
        elif item == '12':
            bot.send_message(message.chat.id, message12)
    else:
        bot.send_message(message.chat.id, "Вы ввели не верную команду")

print('server start')
bot.infinity_polling()
