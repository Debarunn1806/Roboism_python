def func(arr,str):
    if (str=="asce"):
     arr.sort()
     return arr
    elif (str=="desc"):
     arr.sort(reverse=True)
     return arr
    elif(str=="none"):
        return arr 


n=int(input("enter the number of elements"))
lst=[]

for i in range(n):
    arr=int(input())

    lst.append(arr)

str=input("enter the string")

ans_list=func(lst,str)

print(ans_list)
