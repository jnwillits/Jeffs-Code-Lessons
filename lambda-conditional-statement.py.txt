# Example: lamda function with a conditional statement to tweak string output

# You could adjust text based on inputs this way...
num = 1
if num > 1:
    is_are = 'are'
else:
    is_are = 'is'
print(f'There {is_are} {num}.')


# A lambda function does this with less code:
num = 2
is_are = lambda n: 'are' if n > 1 else 'is'
print(f'There {is_are(num)} {num}.')
