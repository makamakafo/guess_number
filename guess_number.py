import random as rnd

print('Угадайте число от 1 до 100')
random_number = rnd.randint(1, 100)
while True:
    # Получаем число от пользователя и сохраняем его в переменную.
    person_number = int(input())
    
    # Если число меньше загаданного...
    if person_number < random_number:
        # ...выводим сообщение.
        print('Ваше число меньше того, что загадано.')
    
    # Если число больше загаданного...
    elif person_number > random_number:
        # ...выводим сообщение.
        print('Ваше число больше того, что загадано.')
    
    # Если число угадано...
    elif person_number == random_number:
        # ...прерываем выполнение программы и...
        break
# ...выводим сообщение.
print('Отличная интуиция! Вы угадали число :)')