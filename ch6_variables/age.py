# Write a program named age.py that includes someone's age and 
# then calculates and reports the future age 10, 20, 30, and 40 years from now. 
  # Here's the output for someone who is 22 years old:
  # You are 22 years old.
  # In 10 years, you will be 32 years old.
  # In 20 years, you will be 42 years old.
  # In 30 years, you will be 52 years old.
  # In 40 years, you will be 62 years old.
age = int(input())

print(f'You are {age} years old.')
age = age + 10
print(f'In 10 years, you will be {age} years old.')
age = age + 10
print(f'In 20 years, you will be {age} years old.')
age = age + 10
print(f'In 30 years, you will be {age} years old.')
age = age + 10
print(f'In 40 years, you will be {age} years old.')

# OR

#age_10 = age + 10
#age_20 = age + 20
#age_30 = age + 30
#age_40 = age + 40

# OR

# print(f'In 10 years, you will be {age + 10} years old.')