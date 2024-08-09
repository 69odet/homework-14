def print_params(a = 1, b = 'строчка', c = True):
    print(a, b, c)

print_params(2)
print_params(2, 3)
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])


values_list = [54.32, 'Строка']
values_dict = {'a': 5, 'b': 'Число', 'c': True}
print()
print_params(*values_list)
print_params(**values_dict)


values_list2 = [12.24, True]
print()
print_params(*values_list2, 42)