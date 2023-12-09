# Algo_part3

# Лабораторні роботи з дисципліни "Алгоритмів і структур даних"

## Виконала: Фещин Іванна Іванівна (Група ІР-24)

### Лабораторна робота №1 (Варіант 2 Рівень 3)
'''Напишіть функцію, яка приймає невпорядкований масив цілих чисел і повертає діапазон індексів (початковий і кінцевий) найменшого підмасиву, який потрібно відсортувати для досягнення повного впорядкування всього масиву.
Наприклад, для вхідного масиву
1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19
Результат: (3, 9)
Підмасив, який потрібно відсортувати для впорядкування всього масиву, починається з індексу 3 (значення 7) і закінчується на індексі 9 (значення 7).
У випадку, якщо вхідний масив відсортований, слд повернути кортеж (-1, -1)
Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку `unittest` та перевірити сценарії коли: вхідний масив посортований, вхідний масив необхідно сортувати весь, масив містить лише 1 елемент. '''


### Лабораторна робота №2 (Варіант 2 Рівень 2)
Джоні працює менеджером в будівельній компанії. Сьогодні він отримав завдання зафарбувати N рекламних щитів,  довжина яких складає {A0, A1, A2, A3 ... AN-1}. В компанії Джоні доступно К малярів,  а також час, за який будь-який з малярів замальовує 1 метр погонний щита. Оскліьки замовлення надвичайно важливе, Джонні має виконати цю роботу якомога швидше. Слід врахувати, що малювати один щит може лише один маляр - який почав роботу з ним
Правила  
1. 2 малярі не можуть розділити щит, щоб малювати його одночасно, або частково. Тобто, не ситуація коли щит почав пофарбувати одн маляр, а завершив інший - неможлива.
2. 2. Маляр фарбує лише суміжні щити. Що означає, ситуація коли маляр А фарбує щити 1 і 3, але пропускає щит 2 -  неможлива.
Input
K - кількість малярів
Т - час, за який маляр замальовує 1 погонний метр щита (в хвилинах)
L - масив (цілочисельний) довжин щитів, які необхідно замалювати (в метрах)
Приклад
10
5
10 15 10 5 10 15 20 20 15 20
Результат
100 хвилин
Очевидно, що максимальна тривалість замальовування щитів в прикладі (коли кількість щитів рівна кількості малярів) відповідає часу малювання найдовшого щита
Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку `unittest` та перевірити роботу вашої функції на прикладах, наведених вище​


### Лабораторна робота №3 (Варіант 2 Рівень 2)
Для бінарного дерева знайдіть суму всіх глибин усіх вузлів. Глибина вузла - це кількість ребер, які потрібно пройти від кореня дерева, щоб досягти цього вузла.
Ваше завдання полягає в написанні функції, яка обчислює та повертає суми глибин для всіх вузлів у бінарному дереві
Приклад: Розглянемо таке бінарне дерево:
    1
   / \
  2   3
 / \
4   5
Глибина вузла 1 -0, глибина вузла 2 та 3 становить 1, а глибина вузлів 4 та 5 - 2. Сума глибин всіх вузлів дорівнює 0 + 1 + 1 + 2 + 2 = 6.
Функція отримує на вхід корінь бінарного дерева, який має наступний вигляд:
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
 Ваша функція має мати такий вигляд:  
def sum_of_depths(root: TreeNode) -> int:
    # ваш код

Реалізація даної задачі не вимагає написання коду вставки чи виділення елементів з бінарного дерева. У тесті ви можете створити достатню кількість елементів класу TreeNode наступним чином:
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)




### Лабораторна робота №4 (Варіант 4 Рівень 2)
Варіант 4 Перевірте, чи містить неорієнтований граф цикл
Дано зв’язний неорієнтований граф, перевірте, чи містить він цикл чи ні.
Наприклад, наступний графік містить цикл 2–5–10–6–2:
Для представлення графу слід використати список суміжності, який зчитується з файлу input.txt
Результат (True - якщо цикл присутній, False - якщо відсутній) слід вивести у файл output.txt




### Лабораторна робота №5 (Варіант 2 Рівень 3)
Пиво
Аутсорс компанія (один з лідерів ринку) готується до корпоративу.  HR відділ відправив опитувальник щодо видів пива, які можна буде роздавати на на святі.  Переважно працівники компанії люблять небагато видів пива, і будуть дуже ображені, якщо принаймні одного з пив, які вони люблять, не буде на вечірці.  Оскільки ви - лідер ринку, то вам не можна ображати працівників.
З іншої сторони, закупити усі можливі види пива - дорого.  Вашим завдання буде з’ясувати скільки різних видів пива потрібно буде привезти на корпоратив.
Вхідні дані:  Перший рядок містить числа N - кількість працівників та B - кількість доступних пив.  Другий рядок містить N*B літер N або Y.  Якщо літера i*N + j - Y, то працівнику i подобається пиво j
Вихідні дані:  Найменша кількість видів пива, яка повинна бути на святі
Обмеження:  Кожному працівнику подобається принаймні один вид пива
	        0 < N < 50
	        0 <B < 50
Приклади:
In:
2 2
YN NY
Out: 2	(Першому працівнику подобається тільки пиво 1, а другому тільки пиво 2, тому доведеться купляти два типи пива)
In:
6 3
YNN YNY YNY NYY NYY NYN
Out: 2  (Хоча більшості - чотирьом працівникам - подобається третє пиво, найоптимальніше буде купити 1 та 2 сорти)




### Лабораторна робота №6 (Варіант 2 Рівень 3)
Створити функцію на мові програмування Python, яка приймає дві стрічки: "haystack" (довільний текст) та "needle" (шукана стрічка). Програма повинна знайти індекси всіх входжень стрічки "needle"
в стрічці "haystack" та повернути цей індекс, використовуючи  метод Кнутта-Морріса-Прата для пошуку підстрічки у стрічці.
