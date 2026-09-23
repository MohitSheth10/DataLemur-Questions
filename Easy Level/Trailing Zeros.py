num=int(input())
value=1
for i in range(1,num+1):
    value=value*i
#print("Factorial of num is", value)
length=len(str(value))
for i in range(length-1,0,-1):
    if value%(10**i)==0:
        print(i)
        break
else:
    print(0)  # factorials below 5! have no trailing zeros
