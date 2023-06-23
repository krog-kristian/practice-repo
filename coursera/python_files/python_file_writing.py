try:
  with open('newfile.txt', 'w') as file:
    file.writelines(['\nCreated my first file!', '\nMultiline writing and writing over!'])
except FileNotFoundError as e:
  print('Error', e)
