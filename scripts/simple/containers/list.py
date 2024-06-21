

# 1. create
b = [1,2,3]
print(type(b))
# list comprehension
d = [x * x for x in range(0,5) ]
print(d)

# 2. update
b.append(5)
print(b)

# 3. sort
c = [8,6,2]
c.sort()
print(c)

# 4. add list
print("4 point")
d = [1,2,3]
f = [4,5,6]
f= d + f
print(f)