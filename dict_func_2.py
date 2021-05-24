fruits = {'apple':100, 'banana':40, 'kiwi':90, 'dragonfruit':400}

print('looping in dict')

for i in fruits:
    print(i)

print('=> get only values')
for i in fruits.values():
    print(i)
#another method
for i in fruits:
    print(fruits[i])

print('=> get keys and values')
for k, v in fruits.items():
    print(k,'-->',v)
#another method
for i in fruits:
    print(i ,'-->',fruits[i])