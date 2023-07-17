#how to reverse a string

# Syntax of slice notation str[start:stop:step]
def reverse(str):
    return str[::-1]

x = input('Word to be reversed: ')

print(reverse(x))
