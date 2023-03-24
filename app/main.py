import utils

keys, values = utils.get_population()
print(keys, values)

data = [
    {
    'Country' : 'Mexico',
    'Population' : 600
    },
    {
    'Country' : 'Colombia',
    'Population' : 200
    }
]
country = input('Type country => ')
result = utils.population_by_country(data, country)
print(result) #[{'Country': 'Mexico', 'Population': 600}]