# Python Program to find the L.C.M. of two input number

def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
        #    print(greater)
           lcm = greater
           break
       greater += 1

   return lcm

num1 = int(input("Enter first No : "))
num2 = int(input("Enter second No : "))

print("The L.C.M. is", compute_lcm(num1, num2))
