my_name = ('Leyla', 'Galiullina', 19)
people = []
people.append(my_name)
friend_1 = ('Kira', 'Knightley', 35)
friend_2 = ('Eric', 'Kross', 20)
friend_3 = ('Arslan', 'Safin', 10)
people.append(friend_1)
people.append(friend_2)
people.append(friend_3)
print('Несортированный список:')
print(people)
print('Сортировка по имени:')
people.sort(key = lambda x: x[0])
print(people)
print('Сортировка по фамилии:')
people.sort(key = lambda x: x[1])
print(people)
print('Сортировка по возрасту:')
people.sort(key = lambda x: x[2])
print(people)
