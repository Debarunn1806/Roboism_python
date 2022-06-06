n=int(input("enter the number of elements in the array"))
lst=[]
for i in range(0,n):
    arr=int(input())
    lst.append(arr)

max = 0
num = lst[0]
for i in lst:
    f = lst.count(i)
    if f > max:
        max = f
        num = i

print("the most frequent element is " + str(num))
