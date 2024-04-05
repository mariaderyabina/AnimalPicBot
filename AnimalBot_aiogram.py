import requests
import config
from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
# Для картинок с медведями
import random

BOT_TOKEN = config.TOKEN
ERROR_TEXT_CAT = 'тут должен быть котик :('
ERROR_TEXT_FOX = 'тут должна быть лисичка :('
ERROR_TEXT_DOG = 'тут должна быть собака :('
ERROR_TEXT_BIRD = 'тут должна быть птичка :('
ERROR_TEXT_BEAR = 'тут должен быть медведь :('
API_URL_CAT = 'https://api.thecatapi.com/v1/images/search'
API_URL_FOX = 'https://randomfox.ca/floof/'
API_URL_DOG = 'https://random.dog/woof.json'
API_URL_BIRD = 'https://shibe.online/api/birds'
API_URL_BEAR = 'https://placebear.com/'

animal_response: requests.Response
animal_link: str
animal_link_format: str

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        'Привет!\nЯ - бот, который бесконено может показывать картинки разных животных\n'
        'Выбери животное в списке команд и получишь картинку :)'
    )

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

# Обработка команды /bird
@dp.message(Command(commands=['bird']))
async def process_bird(message: Message):
    animal_response = requests.get(API_URL_BIRD)
    if animal_response.status_code == 200:
        animal_link = animal_response.json()[0]
        animal_link_format = animal_link.split('.')[-1]
        if animal_link_format == 'mp4' or animal_link_format == 'gif':
            await message.answer_video(animal_link)
        else:
            await message.answer_photo(animal_link)
    else:
        await message.answer(ERROR_TEXT_FOX)

# Обработка команды /bear
@dp.message(Command(commands=['bear']))
async def process_bear(message: Message):
    animal_link = API_URL_BEAR + str(random.randint(300, 500)) + '/' + str(random.randint(300, 500))
    animal_response = requests.get(animal_link)
    if animal_response.status_code == 200:
        await message.answer_photo(animal_link)
    else:
        await message.answer(ERROR_TEXT_BEAR)


# Запускаем поллинг
if __name__ == '__main__':
    dp.run_polling(bot)    