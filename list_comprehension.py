x  = [1,2,3,4,5,6,7,8,9,0]
c = []
for i in x:
    sqr = i**2
    c.append(sqr)

print(x)
print(c)

#list comprehension

r = [1,2,3,4,5,6,7,89,9]
g = [i**2 for i in r]

print(r)
print(g)