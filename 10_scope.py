price = 100 # global scope

def increment():
    price = 200 # local scope
    price += 10
    return price

print(price) # variable global scope

price_2 = increment()
print(price_2)