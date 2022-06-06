def func(a,b,char):
    if (char=="+"):
        return a+b
    elif (char=="-"):
        return a-b 
    elif (char=="*"):
        return a*b 
    elif (char=="/"):
        return a/b     

a=int(input("enter first number"))
b=int(input("enter the second number"))
char=input("enter the operation to be performed")

ans=func(a,b,char)
print(ans)
