numbers_v1 = [1, 2, 3, 4]

numbers_v2 = []
for i in numbers_v1:
    numbers_v2.append( i * 2)

numbers_v3 = list(map(lambda i : i * 2, numbers_v1))

print(numbers_v1)
print(numbers_v2)
print(numbers_v3)

# Se puede iterar dos listas y hacer operaciones
result = list(map(lambda x, y : x + y, numbers_v1, numbers_v3))
print(result)