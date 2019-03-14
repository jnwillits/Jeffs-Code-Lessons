# Examples of list comprehension, map, and the lambda function:

celsius = [0, 10, 20.1, 34.5]

def convert_c_to_f(temp):
    return (9/5)*temp + 32

# Simple and clean...
print([(9/5)*temp + 32 for temp in celsius ])

# More complicated...
print(list(map(lambda temp: (9/5)*temp + 32, celsius)))

# Useful if you need a function to reuse elsewhere...
print(list(map(convert_c_to_f, celsius)))
