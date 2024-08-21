print("______________________Work with tuple______________________")

example = (5, 'Taras', 'Man')
print('Packing tuple: ', example)

(var1, var2, var3) = example
print(f'Unpacking tuple: {var1}, {var2}, {var3}')

#Розпакування великого кортежу(змінних менше, ніж елементів)

print('\n\t__________unpacking big tuple__________\n')

numbers = (1,2,3,4,5,6,7)
(vari1, *vari2, vari3) = numbers
print(f"Unpacked: {vari1}, {vari2}, {vari3}")

#Перетворення кортежу в список і навпаки

print('\n\t__________convert tuple to list__________\n')

new_list = list(numbers)
print("List from tuple: ", new_list)

print('\n\t__________convert list to tuple__________\n')

new_tuple = tuple(new_list)
print("Tuple from list: ", new_tuple)

#Цикли і tuple

