def increment(x):
    return x + 1

def high_ord_func(x, func):
    return x + func(x)

result = high_ord_func(2, increment)
print(result)

# con lambda
increment_v2 = lambda x : x + 1
high_ord_func_v2 = lambda x, func : x + func(x)
result_v2 = high_ord_func_v2(3, increment_v2)
print(result_v2)

result_v3 = high_ord_func_v2(6, lambda x : x * 2)
print(result_v3)