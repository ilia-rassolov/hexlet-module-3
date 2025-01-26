'''
Дан массив целых чисел nums и целое число target, вернуть индексы двух чисел, чтобы их сумма давала target.
Вы можете предположить, что каждый вход будет иметь ровно одно решение , и вы не можете использовать один
и тот же элемент дважды.

Вы можете возвращать ответ в любом порядке.
'''
nums = [2,7,11,15,22,34,11,2,5]
target = 36


def two_sum(nums, target):
    for i, num in enumerate(nums):
        for i_2, num_2 in enumerate(nums):
            if num + num_2 == target and i != i_2:
                return [i, i_2]

print(two_sum(nums, target))

def two_sum_2(nums, target):
    i = 0
    for num in nums:
        i_2 = 0
        for num_2 in nums:
            if num + num_2 == target and i != i_2:
                return [i, i_2]
            i_2 += 1
        i += 1

print(two_sum_2(nums, target))

class Solution:
    def twoSum(self, nums, target):
        i = 0
        for num in nums:
            i_2 = 0
            for num_2 in nums:
                if num + num_2 == target and i != i_2:
                    return [i, i_2]
                i_2 += 1
            i += 1

solution = Solution()
print(solution.twoSum(nums, target))




