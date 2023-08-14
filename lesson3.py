# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику

def same_by(characteristic, objects):
   el = len(list(filter(characteristic, objects)))
   print(el)
   return not el or el == len(objects)

values = [0, 2, 10, 6]
values2 = [1, 3, 7, 6]

if same_by(lambda x: x % 2, values2):
    print('same')
else:
    print('different')