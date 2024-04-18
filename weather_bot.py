import telebot
import requests

TOKEN = '7055644404:AAFzHg1r3O1ms_Yfp_SOnnKELuYzjVxAMO0'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я чат-бот погоды. Просто напиши мне название города, и я скажу тебе погоду!")


@bot.message_handler(func=lambda message: True)
def get_weather(message):
    city = message.text
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=f238a2c0010d97eb574d97283bd77a66'
    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        bot.reply_to(message, f"Погода в городе {city}: {weather_description}, Температура: {temperature}K")
    else:
        bot.reply_to(message, "Извините, не удалось получить данные о погоде для этого города.")


bot.polling()

