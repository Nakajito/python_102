'''dict = {}
for i in range (1, 11):
    dict[i] = i * 2
print(dict) #{1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18, 10: 20}

#se reducen las lineas de codigo
dict_v2 = { i: i * 2 for i in range(1, 5)}
print(dict_v2) #{1: 2, 2: 4, 3: 6, 4: 8}
'''
import random
countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
    population[country] = random.randint(1, 100)
print(population) #{'col': 34, 'mex': 92, 'bol': 90, 'pe': 9}

#comprehension
population_v2 = {country : random.randint(1, 100) for country in countries}
print(population_v2) # {'col': 68, 'mex': 77, 'bol': 93, 'pe': 52}

names = ['nakajito', 'kurosaki', 'nk11']
ages = [30, 28, 43]
print(list(zip(names, ages))) #[('nakajito', 30), ('kurosaki', 28), ('nk11', 43)]

new_dict = {names : age for (names, age) in zip(names, ages)}
print(new_dict) # {'nakajito': 30, 'kurosaki': 28, 'nk11': 43}