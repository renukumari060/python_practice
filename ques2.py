# //Write a function that adds minimum 2 numbers but can add more if needed, display the following message: "The total is: " + total. (use Variable-length Arguments)

def add_numbers(*args):
    if len(args) < 2:
        raise ValueError("At least two numbers are required.")
    total = sum(args)
    return f"The total is: {total}"

print(add_numbers( 2, 10))  
print(add_numbers(2, 3, 4, 5))  
