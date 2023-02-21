# write a program that ask for the name of a patient and also asks the age, then it will calculate the age of a person
from datetime import date

# Ask for patient's name and birth year
name = input("Enter patient's name: ")
birth_year = int(input("Enter patient's birth year (YYYY): "))

# Calculate age in years
today = date.today()
age = today.year - birth_year

# Print the result
print(f"{name} is {age} years old.")
