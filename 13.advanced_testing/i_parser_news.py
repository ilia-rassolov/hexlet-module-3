'''
Большинство программ можно представить в виде слоев, где внешние слои отвечают за ввод-вывод данных, а внутренние
 слои реализуют основную логику программы. При этом тестировать лишь внутренние слои не всегда эффективно, ведь
  работоспособность отдельных модулей не гарантирует работоспособность программы в целом.

tests/test_solution.py
В этом упражнении вам предстоит протестировать класс NewsParser, который загружает HTML-страницу, извлекает из
 неё заголовки новостей и сохраняет их в файл.
У класса есть следующие методы:
__init__(self, url) — конструктор, принимает URL страницы с новостями.
fetch_html() — метод, который загружает HTML-страницу и возвращает её содержимое.
parse_news(html) — метод, который извлекает заголовки новостей из HTML-страницы.
save_news(headlines, filename) — метод, который сохраняет заголовки новостей в файл.
process(output_file) - метод, который собирает всю логику вместе: загружает страницу, извлекает
                       заголовки и сохраняет их в файл.
news_parser = NewsParser("https://example.com")
news_parser.fetch_html()
# <html>
#     <body>
#         <h2 class="news-title">Новость 1</h2>
#         <h2 class="news-title">Новость 2</h2>
#         <h2 class="not-news">Это не новость</h2>
#         <h2 class="news-title">Новость 3</h2>
#     </body>
# </html>
headlines = news_parser.parse_news(html) # ['Новость 1', 'Новость 2', 'Новость 3']
news_parser.save_news(headlines, "headlines.txt")

# содержимое файла headlines.txt:
# Новость 1
# Новость 2
# Новость 3
Или все вместе:

news_parser = NewsParser("https://example.com")
news_parser.process("headlines.txt")
Подсказки
Используйте библиотеку responses для тестирования запросов. https://github.com/getsentry/responses
Используйте фикстуры для создания HTML-страницы.
Используйте работу со временными директориями для сохранения файлов.
Помните, что помимо тестирования отдельных модулей, важно протестировать их совместную работу.
'''

import pytest
import responses
from i_implementations import get_class

# парсер новостей, который нужно протестировать
NewsParser = get_class()


# BEGIN (write your solution here)
def test_news_parser_process():


# END