# program named greeter.py that greets 'Victor' three times. 
# Your program should use a variable and not hard code the string value 'Victor' in each greeting. 
# Here's an example run of the program: 
# Good Morning, Victor.
# Good Afternoon, Victor.
# Good Evening, Victor.

# greet with f-string interpolation
name = 'Victor'

print(f'Good morning, {name}.')
print(f'Good Afternoon, {name}.')
print(f'Good Evening, {name}.')


# can also do concatentation:
print('Good Night, '+ name + '.')
