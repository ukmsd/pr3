n=5
a=0
b=1
ny=[]
if n<0:
    print("Incorrect input")
elif n==0:
    print(a)
elif n==1:
    print(b)
else:
    for i in range(2,n+2):
        ny.append(a)
        t=a+b
        a=b
        b=t
print(ny)