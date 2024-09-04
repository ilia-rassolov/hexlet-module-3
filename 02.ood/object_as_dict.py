class Obj:
    def __init__(self, object):
        self.object = Obj(object)


    def __getitem__(self, key):
        return self.dict_['key']











items = {
    'key': 'value',
    'key2': {
        'key3': 'value3'
    }
}
obj = Obj(items)
print(obj.key) # 'value'
obj.key2.key3 # 'value3'
obj['key'] # 'value'
obj['key2']['key3'] # 'value3'

# также значения можно модифицировать
obj['key2'].key3 = 'value4'
obj.key2['key3'] # 'value4'

# в случае отсутствующего ключа должен возвращаться None
obj['undefinedKey'] # None
obj.undefinedKey # None