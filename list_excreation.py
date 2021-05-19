nums = [1,2,3,4,5,5,5,6,7,8,9,0]
names = ['Anjali', 'deepak', 'vishal', 'ayush']
nest = [6, 'ashish', 8, 9 ,'varun']
nested = [['anju', 7,9,],['anjana',9,0]]

print(nums.remove(5))
#remove func. removes the item by is first occurance.
print(nested[1].remove('anjana'))

#pop func. removes last value by default.
# or we can give a indx as well.

print(names.pop())
print(names.pop(3))


#clear removes th entire list.

nest.clear()
print(nest)

