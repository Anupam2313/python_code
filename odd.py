def even(num):
    if num%2==0:
        return 'even'
    else:
        return 'odd'
for i in range(1,10):
    x=even(i)
    print(x)