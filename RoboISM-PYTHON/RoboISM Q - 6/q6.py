lower_value=int(input("enter the lower value of range"))
upper_value=int(input("enter the upper value of range"))

for x in range(lower_value, upper_value+1):
    if x>1:
        for i in range(2,x):
            if(x%i)==0:
                break
        else:
            print(x)

           