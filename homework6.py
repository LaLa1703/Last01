my_dict = {'Ilya': 2003, 'Alina': 2001, 'Vasya': 1999}
print("Dict:", my_dict)
my_dict['Vasya']
print("Existing value:", my_dict['Vasya'])
print('Not existing value:', my_dict.get('Andrey'))
print('Deleted value:', my_dict.pop('Alina'))
my_dict.update({'Alexey': 2005, 'Artem': 1995})
print('Modified dictionary:', my_dict)

my_set = {6, "Gold", 84.48, "Silver", 6, "Silver", 84.48, 9}
print('Set:', my_set)
my_set.add("Bronze")
my_set.add(3)
my_set.discard(9)
print('Modified set:', my_set)

