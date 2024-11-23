immutable_var = 1, 2, 'a', 'b', 'world', True, [10, 20, 30]
print(immutable_var)
# immutable_var[3] = 'c'
error_var = ('Кортежи в Python являются неизменяемыми (immutable) структурами данных. Это означает, что после '
          'создания кортежа его элементы не могут быть изменены. Попытка изменить элемент кортежа приводит к ошибке')
print(error_var)

mutable_list = [1, 2, 'a', 'b', False] +['Football']
print(mutable_list)
mutable_list[3] = 'boll'
mutable_list[5] = 'Soccer'
print(mutable_list)
