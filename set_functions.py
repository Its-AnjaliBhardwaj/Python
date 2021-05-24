f= {1,3,44,4,5,7}
p = {'apple','apple','kiwi','mango'}
z= {1,2,3,3,8,0,9,0,9,0,7,6,4,3,2,2,1}

f.add(78)
p.add("banana")
z.remove(1)
f.update([89,87,67,56,34])
print(f)
print(p)
print(z)


f.pop()
print(f)



print(z.issuperset(f), 'z is supersetof f')
print(p.issuperset(z), 'p is supersetof z')

if f.issubset(p):
    print('f is subset of p')
else:
    print('f is not a subset of p')

if p.isdisjoint(z):
    print('p is disjoint of z ')
else:
    print('p is not disjoint of z')

#set maths
print('union')
print(z.union(p))
print(f|p)


print('difference')
print(z.difference(f))
print(z-f)

print('intersection')
print(p.intersection(f))
print(p&f)

print('symmetric_difference')
print(f.symmetric_difference(z))
print(f^z)
