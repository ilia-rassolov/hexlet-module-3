'''
Дано целое число x, вернуть, trueесли xэто
палиндром
, и falseв противном случае .
'''

def is_polindrom(num):
    if not isinstance(num, int) or num < 0:
        return False
    num_str = str(num)
    left = 0
    right = -1
    while left < len(num_str) // 2:
        if num_str[left] != num_str[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_polindrom(5))



