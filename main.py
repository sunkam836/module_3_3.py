def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()

print_params(5, 'столбец', False)
print_params(35, 'None')
print_params(a='шесть', b='правда', c='истина')
print_params(a='восемь', b='правда')
print_params(b='правда', c='истина')
print_params(a='восемь', c='истина')
print_params(a='восемь')
print_params(b='правда')
print_params(c='триста тридцать три')
print_params()

#print_params(b = 25)
#print_params(c = [1, 2, 3])

values_list = [65, 'Moskau', 5]
values_dict = {'a': 99, 'b': '"истина где-то рядом"', 'c': 68}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']

print_params(*values_list_2, 42)
