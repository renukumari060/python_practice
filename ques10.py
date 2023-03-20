#Write a function that given a list of numbers, it will generate two new lists of numbers, one with the odd numbers and one with the even numbers.

def separate_odd_even(input_list):
    odd_list = []
    even_list = []
    for elem in input_list:
        if elem % 2 == 0:
            even_list.append(elem)
        else:
            odd_list.append(elem)
    return odd_list, even_list

input_list = [1, 2, 3, 4, 5, 6]
odd_list, even_list = separate_odd_even(input_list)
print(odd_list)
print(even_list)
