immutable_var = 1, 2, 'a', 'b'
print(immutable_var)
print(immutable_var[1])
#immutable_var[1] = 'd' - Ошибка! Нельзя заменить, т.к. кортеж по природе неизменяем
#immutable_var = immutable_var + [3, 'd'] - Ошибка! Нельзя конкатенировать (наверное верно написал) , другие
#                                             элементы (числа, текст, списки), если это не кортеж + кортеж
mutable_list = [1, 2, 'apple', True]
print(mutable_list)
mutable_list[1] = 'pepper'
print(mutable_list)
