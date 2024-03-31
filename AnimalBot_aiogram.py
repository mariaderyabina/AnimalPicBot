import requests
import config
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN = config.TOKEN
ERROR_TEXT_CAT = 'тут должен быть котик :('
ERROR_TEXT_FOX = 'тут должна быть лисичка :('
ERROR_TEXT_DOG = 'тут должна быть собака :('
API_URL_CAT = 'https://api.thecatapi.com/v1/images/search'
API_URL_FOX = 'https://randomfox.ca/floof/'
API_URL_DOG = 'https://random.dog/woof.json'

animal_response: requests.Response
animal_link: str
animal_link_format: str

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Обработка команды /cat
@dp.message(Command(commands=['cat']))
async def process_cat(message: Message):
    animal_response = requests.get(API_URL_CAT)
    if animal_response.status_code == 200:
        animal_link = animal_response.json()[0]['url']
        animal_link_format = animal_link.split('.')[-1]
        if animal_link_format == 'mp4' or animal_link_format == 'gif':
            await message.answer_video(animal_link)
        else:
            await message.answer_photo(animal_link)
    else:
        await message.answer(ERROR_TEXT_CAT)

# Обработка команды /dog
@dp.message(Command(commands=['dog']))
async def process_dog(message: Message):
    animal_response = requests.get(API_URL_DOG)
    if animal_response.status_code == 200:
        animal_link = animal_response.json()['url']
        animal_link_format = animal_link.split('.')[-1]
        if animal_link_format == 'mp4' or animal_link_format == 'gif':
            await message.answer_video(animal_link)
        else:
            await message.answer_photo(animal_link)
    else:
        await message.answer(ERROR_TEXT_DOG)

# Обработка команды /fox
@dp.message(Command(commands=['fox']))
async def process_fox(message: Message):
    animal_response = requests.get(API_URL_FOX)
    if animal_response.status_code == 200:
        animal_link = animal_response.json()['image']
        animal_link_format = animal_link.split('.')[-1]
        if animal_link_format == 'mp4' or animal_link_format == 'gif':
            await message.answer_video(animal_link)
        else:
            await message.answer_photo(animal_link)
    else:
        await message.answer(ERROR_TEXT_FOX)


# Запускаем поллинг
if __name__ == '__main__':
    dp.run_polling(bot)    