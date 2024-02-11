def add(a,b):
    x=a+b
    return x
def dev(a,b):
    y=a*b
    return y
def sub(a,b):
    z=a//b
    return z
def garter(a,b):
    if a>b:
        print('a is garter')
    else:
        print('b is garter')
print("--------------------")
k=int(input("f :"))
j=int(input("s :"))
print("--------------------")
l=add(k,j)
print("sub :",l)
print("--------------------")
m=dev(k,j)
print("dev :",m)
print("--------------------")
n=sub(k,j)
print("sub :",n)
print("--------------------")
q=garter(k,j)
print(q)