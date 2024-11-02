from dotenv import load_dotenv
import os

load_dotenv()

# Токены и ключи API
BOT_TOKEN = os.getenv('BOT_TOKEN')
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

# Базовые настройки
WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"
LANGUAGE = "ru"
UNITS = "metric"  # Для отображения температуры в Цельсиях