from urllib import parse

class Url:
    def __init__(self, http_address):
        self.http_address = http_address
        self.elements = parse.urlparse(self.http_address)
        self.query = self.elements.query

    def get_scheme(self):
        return self.elements.scheme

    def get_hostname(self):
        return self.elements.hostname

    def get_query_params(self):
        params = parse.parse_qs(self.query)
        return params

    def get_query_param(self, key, value=None):
        params = parse.parse_qs(self.query)
        try:
            if params[key]:
                return params[key][0]
        except KeyError:
            return value

    def __eq__(self, other):
        return self.http_address == other


url = Url('http://hexlet.io:80?key=value&key2=value2')
print(url.get_scheme())
print(url.get_hostname())
print(url.get_query_params())
print(url.get_query_param('key')) # value
# второй параметр — значение по умолчанию
print(url.get_query_param('key2', 'lala')) # value2
print(url.get_query_param('new', 'ehu')) # ehu
print(url.get_query_param('new')) # None
print(url.__eq__('http://hexlet.io:80?key=value&key2=value2'))