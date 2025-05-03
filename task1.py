 Task 1
1. Variables

# 1. Create a variable named pi and store the value 22/7 in it.
pi = 22 / 7
print("Value of pi:", pi)
print("Data type of pi:", type(pi))  

# 2. Create a variable called 'for' and assign it a value 4. See what happens and why.
for = 4 

# Explanation:
print("You cannot use 'for' as a variable name because it is a reserved keyword used in loops.")

# 3. Store principal, rate of interest, and time in different variables
P = 10000  
R = 5      
T = 3      

# Calculate Simple Interest
simple_interest = (P * R * T) / 100
print("Simple Interest for 3 years:", simple_interest)

2.Numbers

# 1. Write a function that takes two arguments, 145 and 'o', and uses the format function to return a formatted string. Print the result.
def format_number(num, fmt_char):
    result = format(num, fmt_char)
    print("Formatted:", result)

format_number(145, 'o')

# 2. In a village, there is a circular pond with a radius of 84 meters. Calculate the area of the pond.
radius = 84
pi = 3.14
pond_area = pi * radius ** 2
print("Area of the pond:", pond_area)

# Bonus: If there is exactly 1.4 liters of water in a square meter, calculate the total amount of water.
water_per_sqm = 1.4
total_water = pond_area * water_per_sqm
print("Total water in the pond (liters):", int(total_water))

# 3. If you cross a 490 meter long street in 7 minutes, calculate your speed in meters per second.
distance = 490
time_minutes = 7
time_seconds = time_minutes * 60
speed = distance / time_seconds
print("Speed (m/s):", int(speed))

3.List

# 1. Initial Justice League list
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Initial Justice League:", justice_league)

# 1.1 Calculate the number of members
print("Number of members:", len(justice_league))

# 2 Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("After adding Batgirl and Nightwing:", justice_league)

# 3 Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After making Wonder Woman the leader:", justice_league)

# 4 Separate Aquaman and Flash by inserting Superman between them
justice_league.remove("Superman")  # Remove Superman to reinsert him later
flash_index = justice_league.index("Flash")
aquaman_index = justice_league.index("Aquaman")

# Ensure correct order: insert between Aquaman and Flash
# Place Superman after Aquaman
insert_index = max(flash_index, aquaman_index)
justice_league.insert(insert_index, "Superman")
print("After separating Aquaman and Flash with Superman:", justice_league)

# 5 Replace the list with new members
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New Justice League team:", justice_league)

# 6 Sort alphabetically and show the new leader
justice_league.sort()
print("Sorted Justice League:", justice_league)
print("New leader (0th index):", justice_league[0])
# BONUS Prediction: The new leader will be "Cyborg" after sorting.

4. If Condition

# 1. BMI Category Checker

height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))
bmi = weight / (height ** 2)

if bmi >= 30:
    print("Obesity")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal")
else:
    print("Underweight")

# 2. Determine which country a city belongs to

australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("Enter a city name: ")

if city in australia:
    print(f"{city} is in Australia")
elif city in uae:
    print(f"{city} is in UAE")
elif city in india:
    print(f"{city} is in India")
else:
    print("City not found in our list")

# 3. Check if two cities belong to the same country

city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

def get_country(city_name):
    if city_name in australia:
        return "Australia"
    elif city_name in uae:
        return "UAE"
    elif city_name in india:
        return "India"
    else:
        return None

country1 = get_country(city1)
country2 = get_country(city2)

if country1 and country2:
    if country1 == country2:
        print(f"Both cities are in {country1}")
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities are not in our list")
  
5.For Loop

# 1. Simulate rolling a six-sided die at least 20 times
import random

rolls = 30  # Number of times to roll
count_six = 0
count_one = 0
count_double_six = 0
previous_roll = 0

for i in range(rolls):
    roll = random.randint(1, 6)
    print(f"Roll {i + 1}: {roll}")
    
    if roll == 6:
        count_six += 1
        if previous_roll == 6:
            count_double_six += 1
    if roll == 1:
        count_one += 1

    previous_roll = roll

print("Number of times rolled a 6:", count_six)
print("Number of times rolled a 1:", count_one)
print("Number of times rolled two 6s in a row:", count_double_six)

# 2. Jumping jacks workout program

completed = 0
total = 100
set_size = 10

while completed < total:
    completed += set_size
    print(f"You have completed {completed} jumping jacks.")
    
    if completed >= total:
        print("Congratulations! You completed the workout.")
        break
    
    tired = input("Are you tired? (yes/y or no/n): ").strip().lower()
    
    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").strip().lower()
        if skip in ["yes", "y"]:
            print(f"You completed a total of {completed} jumping jacks.")
            break
    else:
        print(f"{total - completed} jumping jacks remaining.")


