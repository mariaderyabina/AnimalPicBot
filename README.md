# Телеграм-бот, который показывает картинки животных
Алгоритм работы:
1. Бот ожидает команду от пользователя. Доступные команды приведены в выпадающем списке. Примеры команд: /cat, /dog, /fox, /bird, /bear.
2. После команды пользователя, бот отправляет GET-запрос к публичному API с картинками соответсвующего животного. 
3. В зависимости от формата данных, полученных по запросу, бот отправляет пользователю картинку, гифку или видео.

В репозитории находятся два варианта реализации: 
- AnimalBot.py - подключение напрямую к Telegram API. Обработка апдейтов происходит в цикле.
- AnimalBot_aiogram.py - с помощью библиотеки aiogram. Апдейты обрабатываются методами классов Dispatcher и Bot.