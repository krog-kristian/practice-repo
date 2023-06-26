#creating a pure function to not modify global variables.

# not pure

my_list = [1, 2, 3]

def add_to_list(lst, item):
    lst.append(item)
    return lst
new_list = add_to_list(my_list, 4)


print(my_list)
print(new_list)

#pure

your_list = ['a', 'b', 'c']

def make_list(lst, item):
    some_list = lst.copy()
    some_list.append(item)
    return some_list

this_list = make_list(your_list, 'd')

print(your_list)
print(this_list)