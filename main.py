import logging
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Установите свой токен бота и ключ API TMDb
TOKEN = 'import logging
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Установите свой токен бота и ключ API TMDb
TOKEN = '6913570831:AAEA_SIHdVZ77d_dqOY59_PG1BJDXE8thUk'
TMDB_API_KEY = 'b2a93a559c217ccddcf537717645577b'

# Настройка журнала
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

# Обработчик команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот, который рекомендует фильмы. Используй /recommend, чтобы получить рекомендацию.')

# Обработчик команды /recommend
def recommend(update: Update, context: CallbackContext) -> None:
    # Получение рекомендации фильма с использованием API TMDb
    url = f'https://api.themoviedb.org/3/movie/top_rated?api_key={TMDB_API_KEY}&language=ru-RU'
    response = requests.get(url)
    data = response.json()

    if 'results' in data:
        # Выбираем случайный фильм из топа
        random_movie = data['results'][0]
        title = random_movie['title']
        overview = random_movie['overview']

        update.message.reply_text(f'Рекомендация на вечер:\n\nНазвание: {title}\nОписание: {overview}')
    else:
        update.message.reply_text('Извините, не удалось получить рекомендацию. Попробуйте позже.')

# Основная функция
def main() -> None:
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("recommend", recommend))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
'
TMDB_API_KEY = 'b2a93a559c217ccddcf537717645577b'

# Настройка журнала
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

# Обработчик команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот, который рекомендует фильмы. Используй /recommend, чтобы получить рекомендацию.')

# Обработчик команды /recommend
def recommend(update: Update, context: CallbackContext) -> None:
    # Получение рекомендации фильма с использованием API TMDb
    url = f'https://api.themoviedb.org/3/movie/top_rated?api_key={TMDB_API_KEY}&language=ru-RU'
    response = requests.get(url)
    data = response.json()

    if 'results' in data:
        # Выбираем случайный фильм из топа
        random_movie = data['results'][0]
        title = random_movie['title']
        overview = random_movie['overview']

        update.message.reply_text(f'Рекомендация на вечер:\n\nНазвание: {title}\nОписание: {overview}')
    else:
        update.message.reply_text('Извините, не удалось получить рекомендацию. Попробуйте позже.')

# Основная функция
def main() -> None:
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("recommend", recommend))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
