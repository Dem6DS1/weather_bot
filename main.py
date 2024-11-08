import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import *

def get_weather(city):
    """Получение погоды через OpenWeatherMap"""
    params = {
        'q': city,
        'appid': WEATHER_API_KEY,
        'lang': LANGUAGE,
        'units': UNITS
    }
    
    try:
        response = requests.get(WEATHER_API_URL, params=params)
        return response.json()
    except:
        return None

def send_weather_updates(bot):
    """Отправка погоды для обоих городов"""
    chat_id = "-1002403261441"  # Используем число вместо строки
    cities = ["Ростов-на-Дону", "Азов"]
    
    try:
        for city in cities:
            weather_data = get_weather(city)
            if weather_data and weather_data.get('cod') == 200:
                temp = weather_data['main']['temp']
                feels_like = weather_data['main']['feels_like']
                description = weather_data['weather'][0]['description']
                humidity = weather_data['main']['humidity']
                wind_speed = weather_data['wind']['speed']
                
                message = f"""
                🌍 Погода в городе {city}:
                🌡 Температура: {temp}°C
                🤔 Ощущается как: {feels_like}°C
                ☁️ {description.capitalize()}
                💨 Ветер: {wind_speed} м/с
                💧 Влажность: {humidity}%
                """
                bot.send_message(chat_id=chat_id, text=message)
    except Exception as e:
        print(f"Ошибка при отправке погоды: {e}")

def main():
    """Основная функция"""
    try:
        updater = Updater(BOT_TOKEN)
        
        # Отправляем погоду
        send_weather_updates(updater.bot)
        
        # Завершаем работу бота
        updater.stop()
    except Exception as e:
        print(f"Ошибка в main: {e}")

if __name__ == '__main__':
    main()