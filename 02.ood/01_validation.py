class PasswordValidator():
    OPTIONS = {
        'min_len': 8,
        'contain_numbers': False,
    }

    def __init__(self, **options):
        self.options = PasswordValidator.OPTIONS | options

    def validate(self, password):
        self.password = password
        result = {}

        def has_number(self, password):
            return any(char.isdigit() for char in password)

        if len(password) < self.options['min_len']:
            result['min_len'] = 'too small'
        if not has_number(self, password) and self.options['contain_numbers']:
            result['contain_numbers'] = 'should contain at least one number'

        return result

opt = {'contain_numbers': True}
validator = PasswordValidator(numberz=None)
errors = validator.validate('qtyui7')
print(errors)

