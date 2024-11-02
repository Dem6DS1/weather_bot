import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import *

def start(update, context):
    """Обработчик команды /start"""
    welcome_text = """
    👋 Привет! Я бот погоды.
    Просто отправь мне название города, и я пришлю информацию о погоде.
    """
    update.message.reply_text(welcome_text)

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

def handle_message(update, context):
    """Обработчик текстовых сообщений"""
    city = update.message.text
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
    else:
        message = "😢 Город не найден. Проверьте правильность написания."
    
    update.message.reply_text(message)

def main():
    """Основная функция"""
    # Создаем Updater и передаем ему токен бота
    updater = Updater(BOT_TOKEN)

    # Получаем диспетчер для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрируем обработчики
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Запускаем бота
    print('Бот запущен...')
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()