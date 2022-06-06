def func(str):
    n=len(str)
    for i in range(0,n):
        print(2*str[i],end="")

str=input("enter string")    
print(func(str))    