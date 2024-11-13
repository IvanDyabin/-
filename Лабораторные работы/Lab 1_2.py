# TODO Найдите количество книг, которое можно разместить на дискете
vol = 1.44 * 1024 * 1024
pages = 100
lines_per_page = 50
chars_in_line = 25
volume_for_char = 4
print("Количество книг, помещающихся на дискету:", int(vol // (pages*lines_per_page*chars_in_line*volume_for_char)))

