def func(string):
    sum=0
    for i in string:
        if i.isdigit()==True:
            m=int(i)
            sum+=m

    return sum

str=input("enter the string")
print(func(str))