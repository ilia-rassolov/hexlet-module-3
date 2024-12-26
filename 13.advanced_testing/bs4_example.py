from bs4 import BeautifulSoup
import requests

# Загрузка веб-страницы
url = 'https://www.rbc.ru/society/24/12/2024/676abaaf9a79473f0e4ef271?from=from_main_3'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Извлечение текста элемента
title = soup.find('h1').text
paragraph = soup.find('p').text

print(title)  # Выводит: Заголовок
print(paragraph)  # Выводит: Текст абзаца.
