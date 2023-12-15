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




### Лабораторна робота №7 (Варіант 2 Рівень 2)
Електрики
Ваша компанія проводить електро-мережу в село Вільшанка.  Умовою тендеру було залучення місцевих майстрів, і Вам довелось на це погодитись.  Майстри ці своєрідні, і в результаті вам поставили/закопали N стовпів/електроопор, які знаходяться на відстані w одна від одної.  Проблема у тому, що точна висота кожної опори невідома - ви тільки знаєте, що висота опори i знаходиться у межах [1, heights[i]], і приєднати дріт ви можете тільки до вершини опори (там вже встановлене необхідне обладнання).
Електро-дріт для з’єднання стовпів ви замовляєте з Китаю, і він буде дооовго їхати/пливти.
Ви не знаєте, скільки саме дроту потрібно (це залежить від конкретних висот опор), тому хочете замовити рівно стільки, скільки треба буде для найгіршої ситуації.
(Іншими словами - потрібно знайти таку послідовність висот опор, що дріт, який з’єднує їхні вершини, буде найдовшим)
Вхідні дані: Перший рядок містить w - відстань між опорами. Другий рядок містить N чисел, що опиисують максимальну можливу висоту для кожної опори (тобто це масив heights).
Вихідні дані: Максимально можлива необхідна довжина дроту з точністю до 2 знаків після коми.
Обмеження:  w, heights[i] - цілі числа у діапазоні 1 … 100
            N < 50
	   Звісно, ви повинні ігнорувати різні фізичні обмеження аля просідання дроту чи витрати дроту на з’єднання
Приклади:
In:
2
3 3 3
Out: 5.65 (Наприклад, з висотами опор 3 1 3 довжина дроту це sqrt((3-1)**2 + (3-1)**2) + sqrt((3-1)**2 + (3-1)**2) == 5.65
In:
100
1 1 1 1
Out:300 (Усі опори однакової висоти)
In:
4
100 2 100 2 100
Out:396.32 (Нам потрібно буде найбільше дроту, якщо опори 1/3/5 матимуть висоту 100, а опори 2/4 - висоту 1)
In:
4
56 18 17 94 23 7 21 94 29 54 44 26 86 79 4 15 5 91 25 17 88 66 28 2 95 97 60 93 40 70 75 48 38 51 34 52 87 8 62 77 35 52 3 93 34 57 51 11 39 72
Out:2738.18

