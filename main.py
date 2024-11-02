# a = input("Введіть рядок: ")
# b = a[::-1]
# print("Поворот рядка:", b)


# a = input("Введіть рядок: ")
# b = sum(i.isalpha() for i in a)
# c = sum(i.isdigit() for i in a)
# print("Кількість букв:", b)
# print("Кількість цифр:", c)


# a = input("Введіть рядок: ")
# b = input("Введіть символ для пошуку: ")
# c = a.count(b)
# print(f"Символ '{b}' зустрічається {c} разів")


# a = input("Введіть рядок: ")
# b = input("Введіть слово для пошуку: ")
# c = a.count(b)
# print(f"Слово '{b}' зустрічається {c} разів")


# a = input("Введіть рядок: ")
# b = input("Введіть слово для пошуку: ")
# c = input("Введіть слово для заміни: ")
# n = a.replace(b, c)
# print("Рядок після заміни:", n)



# viraz = input("Введіть вираз (наприклад, 23+12): ")
#
# if '+' in viraz:                            #
#     num1, num2 = viraz.split('+')           #  Це для додавання
#     resultat = float(num1) + float(num2)    #
# elif '-' in viraz:                          #
#     num1, num2 = viraz.split('-')           # Це для Віднімання
#     resultat = float(num1) - float(num2)    #
# elif '*' in viraz:                          #
#     num1, num2 = viraz.split('*')           # Це для умножения
#     resultat = float(num1) * float(num2)    #
# elif '/' in viraz:                          #
#     num1, num2 = viraz.split('/')           # Це для ділення
#     if float(num2) != 0:                    # заборона діленнЯ на нуль
#         resultat = float(num1) / float(num2)#
#     else:                                   #
#         print("Помилка: Ділення на нуль")   # помилка на нуль кроли ділять
#         exit()
# else:
#     print("Невірний формат виразу")        # не обовязковий рядок але він напише коли неправильно напимсаний вираз коли там не ці сиволи а наприклад &
#     exit()
#
# print("Результат виразу:  ", resultat)


# import random # бібліотека створена для рандомних числ щоб працювало random.randint
#
# chislo = [random.randint(-10, 10) for _ in range(20)]  #  це для випадкових чисол
# print("Список чисел:", chislo)
#
# min = min(chislo)
# max = max(chislo)
# Negat = sum(1 for n in chislo if n < 0)
# dod = sum(1 for n in chislo if n > 0)
# zero = sum(1 for n in chislo if n == 0)
#
# print("Мінімальний елемент:", min)
# print("Максимальний елемент:", max)
# print("Кількість від'ємних елементів:", Negat)
# print("Кількість додатних елементів:", dod)
# print("Кількість нулів:", zero)







