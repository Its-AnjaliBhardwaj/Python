cir = lambda r: 2*r*3.14

data = [78,6,5,67,45,33,54,78]


#comprehension
results = [cir(radius) for radius in data]
print(results)

# map func :  a func or lambda expression is always required 
results =  list(map(cir, data))
print(results)