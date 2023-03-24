def get_population():
    keys = ['mex', 'col']
    values = [400, 500]
    return keys, values

def population_by_country(data, country):
    result = list(filter(lambda item: item['Country'] == country, data))
    return result