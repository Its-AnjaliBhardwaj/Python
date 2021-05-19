num = []
print("Please enter 10 values")
for i in range(11):
    val = int(input(f'enter{1} >>'))
    num.append(val)


print("length ", len(num))
print("sum", sum(num))
print("mean", sum(num)/len(num))