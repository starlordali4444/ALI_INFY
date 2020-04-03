'''
Immutable- as value (roughly said) integer tuple string we pass copy
Mutabble - as refereence list dictionary we pass reference
'''
def change_no(num):
    num+=10

num_val=20
change_no(num_val)
print(num_val)

def change_no(num):
    num+=10

num_val=20
change_no(num_val)
print(num_val)
