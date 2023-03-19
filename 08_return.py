def sum_with_range(a,b):
    sum = 0
    print(f'El valor mínimo es: {a} y el valor máximo es {b}')
    for x in range(a,b):
        sum += x
    return sum

result = sum_with_range(1,10)
print(result)

result_2 = sum_with_range(result, result +10)
print(result_2)