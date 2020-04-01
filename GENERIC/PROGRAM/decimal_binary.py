# WAP to convert decimal to binary
for i in range(1,10001):
    b_no=s=""
    temp=i
    while i>0:
        rem=str(i%2)
        b_no=b_no+rem
        i//=2
    for j in b_no: 
        s = j + s    
    print("Decimal value of ",temp,":",s)