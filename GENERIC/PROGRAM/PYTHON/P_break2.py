for num in 23,45,50,65,76,90:
    if num%5!=0:
        continue
    if num%10==0:
        print(num, end=" ")
        continue
    if num%3==0:
        print(num,end=" ")
