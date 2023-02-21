# Write a function that will show the inverse version of a given string. Example: given string "hola" reverse string "aloh".

def inverse_string(string):
    return string[::-1]

my_string = "hola"
result = inverse_string(my_string)
print(result)  # Output: "aloh"
