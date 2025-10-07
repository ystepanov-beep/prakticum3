stroka = int(input())
stolbec = int(input())
number = int(input())
records_per_page = stroka * stolbec
page = (number - 1) // records_per_page + 1
position_on_page = (number - 1) % records_per_page
column = position_on_page // stroka + 1
row = position_on_page % stroka + 1
print(f"страница {page} столбец {column} строка {row}")