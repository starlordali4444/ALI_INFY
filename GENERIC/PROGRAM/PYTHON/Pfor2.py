n1=input()
n2=input()
num1=int(n1)
num2=int(n2)

while num1>=2:
    if num1>num2:
        num1=num1/2
    else:
        print(num1)
        break