# Write a function that given a list of numbers, it will return new list of numbers only displaying one time each element. Example: list (1,1,1,2,2,3,3,5,6) new list (1,2,3,5,6)

def unique_elements(input_list):
    unique_list = []
    for elem in input_list:
        if elem not in unique_list:
            unique_list.append(elem)
    return unique_list

input_list = [1, 1, 1, 2, 2, 3, 3, 5, 6]
new_list = unique_elements(input_list)
print(new_list)
