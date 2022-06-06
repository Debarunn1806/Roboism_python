arr=[]
for i in range (1,100):
    arr.append(i)
import random
r=random.randint(1,100)
arr.append(r)

for i in range(0,100):
    for j in range(i+1,100):
        if (arr[i]==arr[j]):
            print("Duplicate element is :",arr[j])



