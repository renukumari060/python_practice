# write a program that will count the number of letters "a" in a string, after show the following message "The number of iterations of letter A is: " + counterA.

string = input("Enter a string: ")
counterA = 0

for letter in string:
    if letter == "a" or letter == "A":
        counterA += 1

print("The number of iterations of letter A is:", counterA)
