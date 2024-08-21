print("______________________Work with list______________________")

#extend() - розширює list елементами іншого list
print('\n\t__________extend() function__________\n')

group_one = ['Taras', 'Max', 'Nazar']
group_two = ['Nastya', 'Solomia', 'Bohdan']
print(group_one)
group_one.extend(group_two)
print(group_one)

#insert() - вставляє елемент в конкретне вказане місце
print('\n\t__________insert() function__________\n')

new_group = ['Nelya', 'Margaryta', 'Joseph']
print("Just created list: ", new_group)

new_group.insert(0, 'Svyat')
print("List after insert: ", new_group)

#append() - додає елемент в кінець списку
print('\n\t__________append() function__________\n')

new_group.append('Kolya')
print("List after append: ", new_group)

#remove() - видаляє конкретний елемент
print('\n\t__________remove() function__________\n')
new_group.remove('Margaryta')
print("List after remove: ", new_group)

#pop() - видаляє останній елемент або по індексу, наприклад pop(1)
print('\n\t__________pop() function__________\n')
new_group.pop()
print("List after pop: ", new_group)

#clear() - очищає список
print('\n\t__________clear() function__________\n')
new_group.clear()
print("List after clear(): ", new_group)

#reverse() - обертає список
print('\n\t__________reverse() function__________\n')

numbers = [1, -2, 15, 7, 18, 10]
print("Just created list: ", numbers)
numbers.reverse()
print("List after reverse(): ", numbers)

#index() - повертає індекс першого входження вказаного елемента у списку.
print('\n\t__________index() function__________\n')
print("Index of '15': ", numbers.index(15))


