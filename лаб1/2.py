# TODO Найдите количество книг, которое можно разместить на дискете

disk_V_mb = 1.44
pages_in_book = 100
lines_in_page= 50
simbols_in_line = 25
bytes_char = 4

#Переводим объем дискеты в байты
disk_V_b = disk_V_mb * 1024 * 1024

#Вычисляем количество символов в книге
chars_in_book = pages_in_book * lines_in_page * simbols_in_line

#Вычисляем сколько весит одна книга в байтах
book_V = chars_in_book * bytes_char

#Вычисляем количество книг, которые можно разместить на дискете
numbers_book = disk_V_b // book_V

print("Количество книг, помещающихся на дискету:", int(numbers_book))

