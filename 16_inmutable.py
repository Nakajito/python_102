items = [
    {
    'product' : 'camisa',
    'price' : 100
    },
    {
    'product' : 'pantalon',
    'price' : 300
    },
    {
    'product' : 'gorra',
    'price' : 50
    }
]

prices = list(map(lambda item : item['price'], items))
product = list(map(lambda item : item['product'], items))

print(prices)
print(product)

def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * 0.19
    return new_item

new_items = list(map(add_taxes, items))

print('New List')
print(new_items)

print('old list')
print(items)