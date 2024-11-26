# 1 task
my_dict = {'Dead Space Remake': "January 2023", 'Hogwarts Legacy': "February 2023", 'Resident Evil 4 Remake': "March 2023"}
print(my_dict)
print(my_dict ['Dead Space Remake'])
print(my_dict.get('AC: Shadows', 'Comming soon'))
my_dict ['Dead Island'] = "April 2023"
my_dict.update({'Redfal': 'May 2023',
                'Diablo 4': 'June 2023'})
del my_dict['Hogwarts Legacy']
a = my_dict.pop ('Dead Space Remake')
print(my_dict)
print(a)
# 2 task
my_set = {1, 2 ,3, 1, 2, 3, 'a', 'b', 'c', 'a', 'b', 'c'}
print(my_set)
print(my_set.add(6))
print(my_set.add('f'))
print(my_set.discard(2))
print(my_set)
