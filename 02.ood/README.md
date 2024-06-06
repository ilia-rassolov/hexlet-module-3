### 00_pattern

Реализуйте функцию to_Klass(), которая принимает на вход словарь и возвращает объект типа Klass такой же структуры.

data = {
    'key': 'value',
    'key2': 'value2',
}
config = to_Klass(data)

config.key ## value
config.key2 ## value2
Подсказки
Вам понадобится функция setattr
user = User()
setattr(user, 'f', 'foo')
print(user.f) #=> foo
В пайтоне классы созданные лишь для хранения значений принято оборачивать в декоратор @dataclass
А чтобы не конфликтовать с зарезервированным именем class принято именовать через k

# 01.validation

Валидация - процесс проверки корректности данных. В вебе происходит всегда при отправке форм, например, регистрация на 
многих сайтах проверяет корректность введенного емейла, его уникальность (что такого пользователя ещё нет).

Каждый тип валидации в таких системах обычно представлен классом-валидатором, который принимает на вход опции и 
предоставляет интерфейс в виде функции validate. Эта функция принимает на вход то что проверяется (валидируется) 
и возвращает словарь с ошибками. Если словарь пустой, значит ошибок нет.

solution.py
Реализуйте класс PasswordValidator ориентируясь на тесты.

Этот валидатор поддерживает следующие опции:

min_len (по умолчанию 8) — минимальная длина пароля
contain_numbers (по умолчанию False) — требование содержать хотя бы одну цифру
Словарь ошибок в ключах содержит название опции, а в значении текст указывающий на ошибку

validator = PasswordValidator()
errors = validator.validate('qwerty1')
print(errors)  # => {'min_len': 'too small'}

options = {'contain_numbers': True}
validator = PasswordValidator(**options)
errors = validator.validate('qwerty')
print(errors)  # => {'min_len': 'too small', 'contain_numbers': 'should contain at least one number'}

# валидатор должен игнорировать несуществующие опции
validator = PasswordValidator(numberz=None)
errors = validator.validate('qwertya3sdf')
print(errors) # => {}

class PasswordValidator():
    OPTIONS = {
        'min_len': 8,
        'contain_numbers': False,
        }
    # BEGIN (write your solution here)

    
    # END

    def _has_number(self, password):
        return any(char.isdigit() for char in password)







