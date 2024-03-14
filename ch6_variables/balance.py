# Assume you have $1,000.00 in the bank, 
# and you've somehow managed to find a bank that pays you 5% 
# compounded interest every year. 
# After one year, you will have $1,050 ($1,000 times 1.05). 
# After two years, you will have $1,050 times 1.05, or $1102.50. 
# Create a variable named balance that contains the amount of money you will have after 5 years, 
# then print the result.
# Use a single expression if you can to set balance to the correct value.

MONEY = 1000.0

# * .05 each year for 5 years
year1 = MONEY * .05
balance = MONEY + year1

year2 = balance * .05
balance = year2 + balance

year3 = balance * .05
balance = year3 + balance

year4 = balance * .05
balance = year4 + balance

year5 = balance * .05
balance = year5 + balance
print(f'After 5 years your balance is {balance}!')

# OR more efficient solution
balance = (MONEY * 1.05 * 1.05 * 1.05 * 1.05 * 1.05)
print(f'Another solution to 5 years of balance: {balance}!')