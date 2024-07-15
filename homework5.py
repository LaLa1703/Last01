immutable_var = (66, 'D', 7.77, True)
print(immutable_var)
try:
    immutable_var[0] = 222
except TypeError as e:
    print('Ошибка:', e)
    print('Элементы кортежа нельзя изменить, потому что кортежи являются неизменяемыми объектами.')
mutable_list = [66, 777, 'DDD', 'ff']
mutable_list[2] = "Gg"
mutable_list.append('Modified')
mutable_list.remove(66)
mutable_list.extend("Gold")
print(mutable_list)