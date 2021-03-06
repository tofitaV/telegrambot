import telebot
import pyowm

bot = telebot.TeleBot("880701337:AAH6bJfTuwXsQOzcslFa9i96XoDWEeffopo")
owm = pyowm.OWM("87702129b76743e1bfb5888dfbe53682", language="ru")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = owm.weather_at_places(message.text)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')["temp"]

    answer = "В городе " + message.text +" сейчас " + w.get_detailed_status() + '\n'
    answer += "Температура сейчас"+str(temp) + '\n'

    bot.send_message(message.chat.id, answer )

bot.polling(none_stop=True)