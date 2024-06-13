class Truncater:

    OPTIONS = {
        'separator': '...',
        'length': 200,
    }

    def __init__(self, **options):
        self.options = Truncater.OPTIONS | options

    def truncate(self, text, **new_options):
        new_options = self.options | new_options
        self.text = text
        length = new_options['length']
        separator = new_options['separator']

        if len(text) > length:
            return f"{text[:length]}{separator}"
        return text


truncater = Truncater()
print(truncater.truncate('one two'))
print(truncater.truncate('one two', length=6))
truncater2 = Truncater(length=4, separator='*')
print(truncater2.truncate('one two'))
