#Algorithm for Palindrome

str = 'racecar'

def is_palindrome(str):
    end_index = len(str) - 1

#how to access index in python for loops
    for i, x in enumerate(str):

        if x != str[end_index]:
            return False

        if i == end_index:
            break

        end_index -= 1

    return True





print(is_palindrome('teet'))
