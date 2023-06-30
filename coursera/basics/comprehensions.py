#list comprehensions syntax
# [ <expression> for x in <sequence> if <condition>]

data = [2, 3, 5 , 7, 11, 13, 17, 19, 23, 29, 31]

data_1 = [x+3 for x in data]
print('updated data to data_1 ', data_1)
