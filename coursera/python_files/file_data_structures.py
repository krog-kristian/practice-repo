import random
try:
  with open('petnames.txt', 'r') as file:
    content = file.read().split('\n')
    print(random.choice(content))
except Exception as e:
  print('Somehting went wrong', e)
