# Write a function that will add all numbers greater or equal to 10 from a list of numbers
def sum_greater_than_10(numbers):
    sum = 0
    for num in numbers:
        if num >= 10:
            sum += num
    return sum
my_list = [3, 8, 10, 15, 20, 5]
result = sum_greater_than_10(my_list)
print(result)  # Output: 45 (10 + 15 + 20)
