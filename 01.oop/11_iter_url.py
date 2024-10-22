"""
Реализовать класс-итератор, конструктор которого принимает список строк с URL-адресами.

Итератор должен последовательно запрашивать каждый из URL'ов и возвращать строку с телом страниц (либо None в случае,
если запрос завершился с кодом, отличным от 200).
"""

import requests

class IterUrls:

    def __init__(self, urls):
        self.urls = urls
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.urls):
            raise StopIteration
        result = requests.get(self.urls[self.index])
        self.index += 1
        if result.status_code == 200:
            return result.text

urls = ["https://example.com", "https://clojure.org", "https://google.com/inexistent"]
response_body_iterator = IterUrls(urls)
responses = list(b for b in response_body_iterator)
print(responses)
