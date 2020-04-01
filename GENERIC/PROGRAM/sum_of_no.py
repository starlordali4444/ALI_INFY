#  WAP to find sum of digits of a no

def find_sum_of_digit(no):
    sum=0
    while no>0:
        rem=no%10
        sum+=rem
        no//=10
    return sum

num=int(input("Enter No to find sum of digits : "))
print("Sum of Digits of No",num," is : ", find_sum_of_digit(123))
    