list_1 = ['a', 'b', 'c']
list_2 = list_1
list_3 = list(list_1)
print(list_1)
print(list_2)
print(list_3)
print(list_1 is list_2)
print(list_1 is list_3)
print(list_1 == list_2)
print(list_1 == list_3)
L = ['Hello', 'world']
M = L

print(M is L)

M=L.copy()
print(L)
print(M is L)

shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
list_id_before = id(shopping_center[-1])

shopping_center[-1].append("Uniqlo")
list_id_after = id(shopping_center[-1])

print( list_id_after is list_id_before )