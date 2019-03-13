# Example: List Comprehension
# Iterate through a list, process with a function, and output to a list.

celsius = [0,10,20.1,34.5]
fahrenheit = [print(((9/5)*temp + 32)) for temp in celsius]
