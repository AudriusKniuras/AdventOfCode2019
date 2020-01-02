def multiply(n, multiplier):
    return n*multiplier

numbers = (1,2,3,4)
result = map(multiply, numbers, (2,2,2,2))
print(result)
print(list(result))