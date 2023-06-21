my_tuple = (1, 'strings', 4.5, True)
print(type(my_tuple[1]))

set_a = {1, 2, 3, 4, 5}

set_b = {4, 5, 6, 7, 8}

# set methods add, subtract, remove/discard
# more methods = union( | ), intersection( & ), difference( - ), symmetrical_difference( ^ )

print(set_a & set_b)

# Lists are ordered like and array but same data type, tuples are like lists and arrays with multiple data types.
# sets are like an array or list of items but are not indexed.
# dictionary like an object

#using args to pass multiple variables in a function
def sum_of(*args):
  sum = 0
  for x in args:
    sum += x
  return sum

print(sum_of(4, 5, 6))

#kwargs are key values arguments

def sum_of(**kwargs):
  sum = 0
  for key, value in kwargs.items():
    sum += value
  return round(sum, 2)

print(sum_of(coffee=2.99, cake=4.55, juice=2.99))
