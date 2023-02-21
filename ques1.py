#  write a function that finds maximum out of 3 different numbers
def find_max(num1, num2, num3):
    max_num = num1
    if num2 > max_num:
        max_num = num2
    if num3 > max_num:
        max_num = num3
    return max_num

a = 10
b = 20
c = 15

max_num = find_max(a, b, c)
print("Greater number is",max_num) 
