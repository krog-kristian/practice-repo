#Invalid Index
items = [1, 2, 3, 4, 5]

try:
  print(items[6])
except IndexError as e:
  print('Item does not exist')


def divide_by(a, b):
    return a / b

try:
  ans = divide_by(40, 0)
except:
  print(0)

try:
  with open('file_does_not_exist.txt', 'r') as file:

    print(file.read())
except Exception as e:
    print(e.__class__)
    print('File not found.')
