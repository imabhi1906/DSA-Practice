# def decorator_divide(func):
#     def wrapper(a,b):
#         if a < b:
#             a , b = b , a
#         return func(a,b)
#     return wrapper

# @decorator_divide
# def divide(a,b):
#     return a/b


# print(divide(2, 10))
        
        

def wrapper(a,b):
    if a < b:
        a , b = b , a
    return (a,b)


def divide(a,b):
    a, b = wrapper(a, b)
    return a/b


print(divide(2, 10))        