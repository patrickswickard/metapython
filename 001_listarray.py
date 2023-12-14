import numpy as np

# basically python has both lists and arrays
# with lists being more flexible and arrays being more efficient
# lists can contain objects of different types
# whereas arrays MUST contain all objects of the same type
# for small case stuff it may not matter much and coding for clarity may be fine
# but for large cases, like millions of operations, it makes a huge difference
# in efficiency

# start with a list of integers
a1 = [1,2,3,4,5]

a1_np = np.array(a1)
print(a1)
print(a1_np)
print(a1_np.dtype)

# funky case - the integers get turned into floats since python isn't that much of a prick
l1 = [1, 2.0, 3,4,5]
l1_np = np.array(l1)
print(l1)
print(l1_np)
print(l1_np.dtype)

l2 = [1, 2.0, 'three', 4.4, 5.0]
l2_np = np.array(l2)
print(l2)
print(l2_np)
print(l2_np.dtype)
# SURPRISE!!!!!!!  LOL HAVE FUN DOING SOMETHING WITH THIS
for thisthing in l2_np:
    print(thisthing + thisthing)
# i.e. OOPS WE ARE ALL STRINGS NOW BECAUSE YOU LET IN SOME STRAY "NOT AVAILABLE" OR "EMPTY" CRAP

l3 = [1,2.0,'',4.4,5.0]
l3_np = np.array(l3)
print(l3)
print(l3_np)
for thisthing in l3_np:
    print(thisthing + thisthing)

# so a huge gotcha for importing lists and then trying to use efficient numpy code is making sure
# everything is the same type
