def home(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
    return num
num=int(input("enter first"))
b=home(num)
print(b)