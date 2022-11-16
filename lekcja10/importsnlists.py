from datetime import datetime, timedelta
from internal_lib import my_split
from utils.something import a

print(a)

b = timedelta()
a = datetime(year=2020, month=10, day=1)
print(a)
# print(my_split("abc, def, ghi", ","))

list_a = [1, 2, 3, 4, 5, 6]
list_b = [f"{i+1} małpek skacze po tapczanie" for i in list_a]
list_c = [i+1 for i in list_a if i % 2 == 0]
print(list_a, list_b)
print(list_c)