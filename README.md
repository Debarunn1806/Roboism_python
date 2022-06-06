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
![q1screenshot](https://user-images.githubusercontent.com/106834322/172206246-372fe31d-1fd0-4ddf-bfa7-e92b6aa02d8a.png)

