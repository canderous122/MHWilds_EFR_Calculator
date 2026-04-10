def sum(a,b):
    return a + b

def prod(a, b):
    return a * b

dict = {'sum': sum, 'prod':prod}

print(dict['sum'](1,1))
print(dict['prod'](2,5))