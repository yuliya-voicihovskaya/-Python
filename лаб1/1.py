numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
#Находим индекс пропущеного
none_index = numbers.index(None)

#Создаем новый список без None
new_numbers = [num for num in numbers if num is not None]

#Вычисляем среднее арифметическое
average = sum(new_numbers) / len(numbers)

#Заменяем пропущенный элемент вычисленным средним арифметическим
numbers[none_index] = average

# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
