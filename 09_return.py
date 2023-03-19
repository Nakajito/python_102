def find_volume(length=1, width=1, depth=1):
    return length * width * depth, length * width, 'Resultados'

result, perimetro, text = find_volume(width=10)
print(result)
print(perimetro)
print(text)