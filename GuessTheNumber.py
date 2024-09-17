from random import *

n = randint(1, 101)
count_tries = 0
print('Добро пожаловать в числовую угадайку')
def isvalid(s):
    return s.isdigit() and 1 <= int(s) <= 100

def newinput():
    while True:
        s = input("Введи число от 1 до 100: ")
        if isvalid(s):
            return int(s)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')

s = newinput()
count_tries += 1

while True:
    if s == n:
        print('Вы угадали, поздравляем!')
        break
    elif s > n:
        print('Ваше число больше загаданного, попробуйте еще разок')
    elif s < n:
        print('Ваше число меньше загаданного, попробуйте еще разок')

    s = newinput()
    count_tries += 1


print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
print("Количество попыток:", count_tries)