import unittest
from os import name


# K - кількість малярів
# Т - час, за який маляр замальовує 1 погонний метр щита (в хвилинах)
# L - масив (цілочисельний) довжин щитів, які необхідно замалювати (в метрах)


def can_paint(L, K, T, max_time):
    painters = 0
    current_time = 0

    for l in L:
        if l * T > max_time:
            return False
        if current_time + l * T <= max_time:
            current_time = current_time + l * T
        else:
            painters += 1
            current_time = l * T
            if painters >= K:
                return False  # Закінчилися маляри

    return True  # Всі щити були замальовані в час, не перевищуючи max_time


def time_to_paint(K, T, L):
    left = max(L) * T
    right = sum(L) * T
    selected_elements = None

    while left < right:
        mid = (left + right) // 2
        if can_paint(L, K, T, mid):
            right = mid
            selected_elements = L[:]
        else:
            left = mid + 1

    return left, selected_elements


K = 10
T = 5
L = [10, 15, 10, 5, 10, 15, 20, 20, 15, 20]

result = time_to_paint(K, T, L)
print(f"Результат: {result} хвилин")

K = 2
T = 10
L = [15, 10, 10]
result = time_to_paint(K, T, L)
print(f"Результат: {result} хвилин")

K = 2
T = 10
L = [10, 15, 10]
result = time_to_paint(K, T, L)
print(f"Результат: {result} хвилин")


K = 3
T = 10
L = [10, 15, 10, 20, 25, 15]
#result = time_to_paint(K, T, L)
result, selected_elements = time_to_paint(K, T, L)
print(f"Результат: {result} хвилин")
print(f"Числа: {selected_elements[-2:]}")


class TestTimeToPaint(unittest.TestCase):

    def test_1(self):
        K = 10
        T = 5
        L = [10, 15, 10, 5, 10, 15, 20, 20, 15, 20]
        result = time_to_paint(K, T, L)
        self.assertEqual(result, 100)

    def test_2(self):
        K = 1
        T = 1
        L = [10]
        result = time_to_paint(K, T, L)
        self.assertEqual(result, 10)

    def test_3(self):
        K = 2
        T = 10
        L = [15, 10, 10]
        result = time_to_paint(K, T, L)
        self.assertEqual(result, 200)

    def test_4(self, excepted=250):
        K = 2
        T = 10
        L = [10, 15, 10]
        result = time_to_paint(K, T, L)
        self.assertEqual(excepted, 250)

if name == 'main':
   unittest.main()