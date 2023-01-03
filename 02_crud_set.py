set_countries = {'mex', 'col', 'bol'}

#se utiliza el método len() para conocer la cantidad de valores que tiene el set
size = len(set_countries)
print(size) #3

print('mex' in set_countries) #True
print('arg' in set_countries) #False

#agregar mas elementos al set con el método add()
set_countries.add('arg')
print(set_countries) #{'bol', 'arg', 'col', 'mex'}

#agregar otro conjunto o subconjunto
set_countries.update(
    {'pe', 'ecua'}
)
print(set_countries) #{'pe', 'ecua', 'mex', 'bol', 'arg', 'col'}

#remove() se utiiza para eliminar datos del conjunto.
# Con este método si no encentra el valor, el programa se detiene, para evirar que se detenga se utiliza el método discard()

set_countries.discard('mx')
set_countries.remove('arg')
print(set_countries) #{'col', 'mex', 'pe', 'ecua', 'bol'}

#clear() elimina todos los datos del conjunto
set_countries.clear()
print(set_countries) #set()