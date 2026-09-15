name= int(input('Enter your name'))
n= int(input('Enter your age'))
if n>=18:
  print(f'{name},you can vote)
elif n>=0:
  print(f'{name},you cannot vote)
else:
  print('invalid age')

