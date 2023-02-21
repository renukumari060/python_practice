# write a function that will divide 2 numbers, use an anonymous function for this. And display a message with the result. num1/num2.

def divide(num1, num2):
    result = (lambda x, y: x / y)(num1, num2)
    print(f"{num1} / {num2} = {result}")

divide(10, 2)  # Output: "10 / 2 = 5.0"
