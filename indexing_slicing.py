nums = [1,2,3,4,5,6,7,8,9,0]
names = ['Anjali', 'deepak', 'vishal', 'ayush']
nest = [6, 'ashish', 8, 9 ,'varun']
nested = [['anju', 7,9,],['anjana',9,0]]
primes = [2,3, 5, 7,9,11,13,17,19,23,29]

#indexing
x = nums[6]
print (x)

win = names[2]
print(win)

print(nest[-1])
print(nested[-1][-1])
z = nest[-2]
print(z)

#slicing

first_2 = nums[:2]
last_2 = nums[-2:]
even_idx = names[::2]
first_2_nested = nested[0][:2]
last_2_nested = nested[-1][-2:]
print(first_2)
print(last_2)
print(even_idx)
print(first_2_nested)
print(last_2_nested)