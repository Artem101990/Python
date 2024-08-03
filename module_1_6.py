my_dict={ 'Alex' : 1964, 'Sofia': 1863}
print('Мой словарь:' , my_dict)
print('Год рождения Алексея:',  my_dict.get('Alex'))
my_dict['Egor']=1963
print(' Год рождения Егора:', my_dict['Egor'])
my_dict.update({'Artur': 1992, 'Lesya': 1837 })
print(my_dict)
a = my_dict.pop('Alex')
print(my_dict)
print('Год рождения Алексея:' , a)

my_set = {'Polar', True,  (5, 7 ,23) , 1, 2,7,8,2}
print('Множество:', my_set)
my_set.update({'Kitchen' , '+' , 9 })
print(my_set)
my_set.discard('Kitchen')
print(my_set)

