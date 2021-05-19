d= [1,2,3,4,5,6,7,8,9,0]
h= [9,8,7,4,3,2]

g= []
for i, j in zip(d,h):
    g.append(i+j)


print(d)
print(h)
print(g)
 
print(d+h)