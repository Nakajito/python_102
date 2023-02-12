import random
countries = ['col', 'mex', 'bol', 'pe']
population = {}

population_v2 = {country : random.randint(1, 100) for country in countries}
print(population_v2)

#genera un valor aleatorio de population e imprime los valores que cumplan la condición
result = { country : population for (country, population) in population_v2.items() if population > 20 }
print(result) # {'col': 65, 'pe': 91}

#genera un dicionario con las vocales de un string
text = 'Hola, soy Nakajito'
unique = { c : c.upper() for c in text if c in 'aeiou' }
print(unique) # {'o': 'O', 'a': 'A', 'i': 'I'}