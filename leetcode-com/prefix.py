'''
Напишите функцию для поиска самой длинной общей строки префикса среди массива строк.
Если общего префикса нет, вернуть пустую строку "".

Пример 1:
Ввод: strs = ["flower","flow","flight"]
 Вывод: "fl"

Пример 2:
Ввод: strs = ["dog","racecar","car"]
 Вывод: ""
 Пояснение: Среди входных строк нет общего префикса.

Ограничения:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i]состоит только из строчных английских букв, если он непустой.
'''

def find_prefix(strs):
    prefix = ''
    i = 0
    while True:
        try:
            etalon = strs[0][i]
        except IndexError:
            return prefix
        for str_ in strs:
            try:
                if str_[i] != etalon:
                    return prefix
            except IndexError:
                return prefix
        prefix = f"{prefix}{etalon}"
        i += 1


strs = ["flower","flow","flight"]
print(find_prefix(strs))


