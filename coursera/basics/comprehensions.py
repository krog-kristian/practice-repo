#list comprehensions syntax
# [ <expression> for x in <sequence> if <condition>]

data = [2, 3, 5 , 7, 11, 13, 17, 19, 23, 29, 31]

#updates a list by adding three to each value
data = [x+3 for x in data]
print('updated data ', data)

#creates a new list multiplying each value by 2
new_data = [x*2 for x in data]
print('Created a new list', new_data)

#creating a new list with a condtional statement.
four_time = [x for x in new_data if x%4 == 0]
print('only divisible by four ', four_time)

#Using a range function to create a list
#range syntax is range(start, stop, step)
#start and step are option and if one number given
#will start at 0 and step by one that amount
divisible_by_5 = [x for x in range(51) if x%5 == 0]
print('divisible by five ', divisible_by_5)
