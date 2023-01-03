#los conjuntos (set) se inicializan entre llave {}, no confundir con los diccionarios (llevan key & value), los set unicamente se declaran entre las llaves.
# Se pueden modificar
# No tienen un orden
# No se permiten duplicados
set_countries = {'mex', 'col', 'arg'}
print(set_countries) #{'arg', 'mex', 'col'}
print(type(set_countries)) #<class 'set'>

set_numbers = {1, 4, 9.8, -7}
print(set_numbers) #{1, 4, -7, 9.8}

set_types = {7, True, 9.2, 'Hola'}
print(set_types) #{True, 'Hola', 9.2, 7}

set_from_string = set("hola")
print(set_from_string) #{'o', 'a', 'l', 'h'}

#si existen valores duplicados los elimina
set_from_tuple = set(
    ('abc', 'hes', 'yhg', 'hes', 'abc')
)
print(set_from_tuple) #{'abc', 'yhg', 'hes'}

#se puede transformar una lista de numeros repetidos en un conjunto con valores unicos
numbers = [1,2,3,1,2,3,4,5,5,]
set_numbers2 = set(numbers)
print(set_numbers2) #{1, 2, 3, 4, 5}

#se puede convertir nuevamente a lista (entre corchetes[])con los valores unicos
unique_numbers = list(set_numbers2)
print(unique_numbers) #[1, 2, 3, 4, 5]