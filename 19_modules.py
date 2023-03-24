import sys # permite interactuar con el SO
print(sys.path) #muestra la ruta del proyecto

import re # módulo para trabajar con expresiones regulares
text = " Mi número de teléfono es 44 55 77 88 22, el código de área es 74, el número de la suerte es 8"
resutl = re.findall('[0-9]+', text) # permmite buscar condiciones en strings
print(resutl)

import time #permite trabajar con fechas y tiempo
tiempo = time.localtime()
local = time.asctime(tiempo)
print(local)

import collections

numbers = [1, 2, 1, 4, 4, 3, 6, 6, 4, 3, 1, 3, 2]
counter = collections.Counter(numbers) #muetra la frecuencia de repetición de cada número
print(counter) #Counter({1: 3, 4: 3, 3: 3, 2: 2, 6: 2})