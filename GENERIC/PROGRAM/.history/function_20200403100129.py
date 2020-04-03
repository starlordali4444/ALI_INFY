'''
Immutable- as value (roughly said) integer tuple string we pass copy
Mutabble - as refereence list dictionary we pass reference
'''

# def change_no(num):
#     num+=10

# num_val=20
# change_no(num_val)
# print(num_val)

#string
# def change_no(num):
#     num+="word"
#     print("Inside",num)

# num_val="sample"
# change_no(num_val)
# print("Outside",num_val)

# list
def change_no(num):
    num.append(3)
    print("Inside",num)

num_val=[1,2]
change_no(num_val)
print("Outside",num_val)
