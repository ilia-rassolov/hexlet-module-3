class Obj:
    def __init__(self, object):
        self.object = object

    def __getitem__(self, key):
        return self.object.get(key, None)

    def __setitem__(self, key, value):
        self.object[key] = value

    def __getattr__(self, name):
        self.value = self.object.get(name, None)
        # if isinstance(self.value, str):
        return self.value
        # else:
        #     return self.value.__getattr__(name)


items = {
    'key': 'value',
    'key2': {
        'key3': 'value3'
    }
}
obj = Obj(items)
print(obj.key) # 'value'
print(obj.key2.key3) # 'value3'
obj['key'] # 'value'
obj['key2']['key3'] # 'value3'

# также значения можно модифицировать
obj['key2'].key3 = 'value4'
obj.key2['key3'] # 'value4'

# в случае отсутствующего ключа должен возвращаться None
# obj['undefinedKey'] # None
# obj.undefinedKey # None