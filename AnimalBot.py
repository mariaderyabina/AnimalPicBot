import requests
import time
import config

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = config.TOKEN
MAX_COUNTER = 1000
ERROR_TEXT_CAT = 'тут должен быть котик :('
ERROR_TEXT_FOX = 'тут должна быть лисичка :('
ERROR_TEXT_DOG = 'тут должна быть собака :('
ERROR_TEXT_BIRD = 'тут должна быть птичка :('
API_URL_CAT = 'https://api.thecatapi.com/v1/images/search'
API_URL_FOX = 'https://randomfox.ca/floof/'
API_URL_DOG = 'https://random.dog/woof.json'
API_URL_BIRD = 'https://shibe.online/api/birds'

offset = -2
counter = 0
chat_id: int
animal_response: requests.Response
updates: requests.Response
animal_link: str
chat_text: str
animal_link_format: str



def sendPhotoOrVideo(animal_link, chat_id, API_URL, BOT_TOKEN):
    animal_link_format = animal_link.split('.')[-1]
    if animal_link_format == 'mp4' or animal_link_format == 'gif':
        print(f'{API_URL}{BOT_TOKEN}/sendVideo?chat_id={chat_id}&video={animal_link}')
        requests.get(f'{API_URL}{BOT_TOKEN}/sendVideo?chat_id={chat_id}&video={animal_link}')
    else:
        print(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={animal_link}')
        requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={animal_link}')


#while counter < MAX_COUNTER:
while True:
    
    print('attempt =', counter, 'offset =', offset + 1) # чтобы видеть в консоли

    # Забираем апдейты
    # Через offset + 1 берем следующий апдейт
    print(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}')
    updates_req = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}')
    print(updates_req.status_code)
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            chat_text = result['message']['text']
            if chat_text == '/cat':
                animal_response = requests.get(API_URL_CAT)
                if animal_response.status_code == 200:
                    animal_link = animal_response.json()[0]['url']
                    sendPhotoOrVideo(animal_link, chat_id, API_URL, BOT_TOKEN)
                else:
                    requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT_CAT}')
            elif chat_text == '/fox':
                animal_response = requests.get(API_URL_FOX)
                if animal_response.status_code == 200:
                    animal_link = animal_response.json()['image']
                    sendPhotoOrVideo(animal_link, chat_id, API_URL, BOT_TOKEN)
                else:
                    requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT_FOX}')
            elif chat_text == '/dog':
                animal_response = requests.get(API_URL_DOG)
                if animal_response.status_code == 200:
                    animal_link = animal_response.json()['url']
                    sendPhotoOrVideo(animal_link, chat_id, API_URL, BOT_TOKEN)
                else:
                    requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT_DOG}' )   
            elif chat_text == '/bird':
                animal_response = requests.get(API_URL_BIRD)
                if animal_response.status_code == 200:
                    animal_link = animal_response.json()[0]
                    sendPhotoOrVideo(animal_link, chat_id, API_URL, BOT_TOKEN)
                else:
                    requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT_BIRD}' )                             
    #time.sleep(1)
    counter += 1