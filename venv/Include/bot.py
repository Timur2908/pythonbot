import telebot
import requests



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    id = message.from_user.id
    text = message.text.lower()
    if text == "привет":
        bot.send_message(id, "Привет, чем я могу тебе помочь?")
    elif text == "/help" or text == "/start":
        bot.send_message(id, "Напиши привет или спроси у меня погоду в Алуште или в Симферополе")
    elif "погода" in text or "погоду" in text:
        if "симферополь" in text or "симферополе" in text:
            s_city = "Simferopol,UA"
            city_id = 693805
            try:
                res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                                params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
                data = res.json()
                bot.send_message(id, "Сейчас в Симферополе "+data['weather'][0]['description'])
                bot.send_message(id, "Температура воздуха: " + str(data['main']['temp']) + " градусов цельсия")
            except Exception as e:
                bot.send_message(id, "Простите. Не удалось выяснить погоду. Попробуйте ещё раз")
                pass
        else:
            s_city = "Alushta,UA"
            city_id = 713513
            try:
                res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                               params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
                data = res.json()
                bot.send_message(id, "Сейчас в Алуште "+data['weather'][0]['description'])
                bot.send_message(id, "Температура воздуха: " + str(data['main']['temp']) + " градусов цельсия")
            except Exception as e:
                bot.send_message(id, "Простите. Не удалось выяснить погоду. Попробуйте ещё раз")
                pass
    else:
        bot.send_message(id, "Я тебя не понимаю. Попробуй уточнить запрос или напиши /help.")
bot.polling(none_stop=True, interval=0)