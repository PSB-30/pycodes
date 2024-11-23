def outer_fun(a,b):

    # inner function
    def addition(a, b):
        return a + b

    #calling Inner fun
    add = addition(a, b)
    return add + 2

final = outer_fun(5, 10)
print(final)