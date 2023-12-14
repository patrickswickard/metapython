import numpy as np

a = np.empty(100)
b = np.empty(100)

# SURPRISE it is filled with garbage values!
print(a)

# and it will let you try to do awful things with those garbage values

print(np.sum(a))
print(np.sum(b))

# if you're lucky there will be a nan in there to remind you things are wrong
# but if you're dumb and unlucky you'll do something like this, expecting zeroes in other places

b[0] = 5.0
b[1] = 10.0
b[2] = 15.0

print(np.min(b))
print(np.max(b))


# golly, i don't remember putting those numbers in there!
