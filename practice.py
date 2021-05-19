# Question 1
for i in range(1500,2701 ):
    if i%7 and i%5:
        print(i)

# Question 2

e = int(input("enter a number: "))
c=0
for i in range(e):
    if i%2==0:
        c+=1
print("total even's are:",c)
print("total odd's are:",e-c)

# Question 3

n1, n2 = 0, 1
print(n1)
while(n2<51):
    n3= n1
    n1= n2
    n2 = n3+n1
    print(n2)

# Question 4

i ,k = [], []
i= input("input a string: ")
k = i[::-1]
print(k)
        

    
