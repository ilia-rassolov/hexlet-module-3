from dataclasses import dataclass


@dataclass
class Klass:
    pass

def to_Klass(data):
    klass = Klass()
    print(klass)
    for key, value in data.items():
        setattr(klass, key, value)
    return klass



data_ = {
    'key': 'value',
    'key2': 'value2',
}
config = to_Klass(data_)

print(config)
print(config.key2)
