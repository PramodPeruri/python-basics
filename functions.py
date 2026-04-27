# def func_name():
#     print("Hello")

# print(func_name()) # -> get none value after hello as we are not returning any value

# def mult(a, b):
#     return a * b # default is None
# res = mult(2, 3)
# print(res)

def mult(a, b, *args, **kwargs):
    # *args -> pass any no of position arguments
    # **kwargs -> pass any no of keyword arguments
    

    # print(a, b, args, kwargs)
    print(f"a:{a}, b:{b}, args: {args}, kwargs: {kwargs}") #formal string
    return a * b # default is None

# a=4, b=5 are keyword arguments, as they contain keys and values
# '3.0', 3 are called as postional arguments
res = mult('3.0', 3, 4, 5)
print(res)