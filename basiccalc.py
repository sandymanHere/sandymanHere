def getnumber():
    operation=int(input("enter the operation \n 1-addition \n 2 - substraction \n 3 - multiplication \n 4 - division \n"))
    num1=int(input("enter the first number\n"))
    num2=int(input("enter the second number\n"))
    info={"number1":num1,"number2":num2,"operator":operation}
    return info



def cacl(n1,n2,o):
    if o==1:
        return n1+n2
    elif o==2:
        return n1-n2
    elif o==3:
        return n1*n2
    elif 0==4:
        return n1/n2
    else:
        return "invalid operation"


values=getnumber()
result=cacl(values["number1"],values["number2"],values["operator"])
print(f"thr result is {result}")



