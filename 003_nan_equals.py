import numpy as np

a = np.nan

print(a)

if a <= 1:
  print('You cannot just do nothing!')
elif a > 1:
  print('Make a choice and do something!')

# turns out nan is not equal to anything...even itself!

def blowuptheworld():
  print('BOOM')

if a == a:
  print('This will always execute because a==a is a tautology')
else:
  print('Put whatever you want here, it will never run.')
  blowuptheworld()

# OOOPS!


# also note nan is viral
# it's a "special" float and any interaction with it turns the result into nan

print(a)
b = 1
print(b)
b = b*a
print(b)
