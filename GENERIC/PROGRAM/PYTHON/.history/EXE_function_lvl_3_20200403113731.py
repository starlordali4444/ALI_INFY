'''Write a Python function to find all the Strong numbers in a given list of numbers.
Write another function to find and return the factorial of a number. Use it to solve the problem.

Example:
A number is considered to be a Strong number if sum of the factorial of its digits is equal to the number itself. 
145 is a Strong number as 1! + 4! + 5! = 145. 

Sample Input

num_list = [145,375,0,100,2]

Expected Output

[145, 2]

Note: 0!=1

 '''

def factorial(number):
    if number==0:
        return 1
    elif number==1:
        return number
    else:
        return number*factorial(number-1)

print(factorial(4))


# def find_strong_numbers(num_list):
#     s_no_list=[]
#     sum=0
#     for i in num_list:
#         temp=i
#         while temp>0:
#             rem=temp%10
#             sum+=factorial(rem)
#             temp//=10
#         if i==sum:
#             s_no_list.append(i)
#     return s_no_list

# num_list=[145,375,100,2,10]
# strong_num_list=find_strong_numbers(num_list)
# print(strong_num_list)