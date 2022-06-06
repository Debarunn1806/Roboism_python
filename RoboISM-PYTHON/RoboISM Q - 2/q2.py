lst=[]
n=int(input("enter the number of digits in the card number"))
for i in range(0,n):
    arr=input()
    lst.append(arr)

for i in range(0,n-4):
    lst[i]="*"    

for i in range(0,n):    
    print(lst[i],end="")


    
    