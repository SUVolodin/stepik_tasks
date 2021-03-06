"""
Катя узнала, что ей для сна надо XX минут. В отличие от Коли, Катя ложится спать после полуночи в HH часов и MM минут.
Помогите Кате определить, на какое время ей поставить будильник, чтобы он прозвенел ровно через XX минут после того,
как она ляжет спать.

На стандартный ввод, каждое в своей строке, подаются значения XX, HH и MM. Гарантируется, что Катя должна проснуться в
тот же день, что и заснуть. Программа должна выводить время, на которое нужно поставить будильник: в первой строке
часы, во второй — минуты.
"""
X = int(input("Введите кол-во минут будильника: "))
H = int(input("Введите кол-во часов: "))
M = int(input("Введите кол-во минут: "))
print("Время в часах: ", (X + (H * 60) + M) // 60)
print("Время в минутах: ", (X + (H * 60) + M) % 60)
