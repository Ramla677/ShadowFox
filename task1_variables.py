
# Task 1 - Variables

# 1. Create a variable named pi and store the value 22/7 in it.
pi = 22 / 7
print("Value of pi:", pi)
print("Data type of pi:", type(pi))  # Should be float

# 2. Create a variable called 'for' and assign it a value 4. See what happens and why.
# for = 4  # This line will raise a SyntaxError because 'for' is a reserved keyword in Python.

# Explanation:
print("You cannot use 'for' as a variable name because it is a reserved keyword used in loops.")

# 3. Store principal, rate of interest, and time in different variables
P = 10000  # principal amount
R = 5      # rate of interest
T = 3      # time in years

# Calculate Simple Interest
simple_interest = (P * R * T) / 100
print("Simple Interest for 3 years:", simple_interest)
