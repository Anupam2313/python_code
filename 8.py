def operation(x,y):
    if op=='+':
        print(x+y)
    elif op=="*":
        print(x*y)
    elif op=="-":
        print(x-y)
        return x,y
print("menu driven program")
a=int(input("f :"))
b=int(input("s :"))
op=input("operation :")
z=operation(a,b)
print(z)