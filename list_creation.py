one_crore = list(range(10000000))
#print(one_crore)


evens =list(range(2, 222, 2))
print(evens)

#adding values

x=[]
y = [1,2,3]

z= [1,2,2,3,4,5,6,7,8,9]
z.insert(1,3)
y.insert(10,4)

#insert adds a item at a particular position.

x.append(19)
y.append(8)
print(x)
print(y)
print(z)

 # append adds an item .
x.extend([22, 34, 45])
y.extend(x)
z.extend(y)

print(x)
print(y)
print(z)

#extend adds multiple items in one go.