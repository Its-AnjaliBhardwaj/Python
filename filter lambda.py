x = [1,2,2,3,3,4,4,5,5,6,70,7,8,8,9]
#normal
d = []
for i in x:
    d.append(i)


k = lambda i : i*i%3==0
output = list(filter(k,x))

print(x)
print(d)
print(k)
