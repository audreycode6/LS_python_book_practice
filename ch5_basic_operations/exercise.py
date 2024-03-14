# Concatenate two strings, one with your first name and one with your last, 
# to create a new string with your full name as its value. 
# For example, if your name is John Doe, you should combine 'John' and 'Doe' to get 'John Doe'.

print('Audrey' + ' ' + 'Theriault')

first_name = 'Audrey'
last_name = 'Theriault-Allaire'
print(first_name + ' ' + last_name)

# Use the REPL and the arithmetic operators to extract the individual digits of 4936:
number = 1234
#print("original number:", number)

# extract ones place
ones = number % 10
print('ones:',ones)

# 10's place
number = number // 10
#print("number no 1's:", number)
tens = number % 10
print('tens:', tens)


# 100's place
number = number // 10
#print("number no 10's:", number)
hundreds = number % 10
print("hundreds:", hundreds)

# 1000's place
thousands = number // 10
print("thousands:", thousands)


number1 = int('5')
number2 = int('10')

print(number1 + number2)

print(int('5')+ int('10'))

number = float('3.1415')
number = int(number)
print(number)