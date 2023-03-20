# write a function that will fin the minimum of 3 numbers and display the following message "The smallest number is: " + maxNumber.

def find_smallest_num(num1, num2, num3):
    min_num = min(num1, num2, num3)
    print("The smallest number is:", min_num)

find_smallest_num(4, 7, 2)   # Output: The smallest number is: 2
find_smallest_num(9, 2, 5)   # Output: The smallest number is: 2
find_smallest_num(1, 1, 1)   # Output: The smallest number is: 1
