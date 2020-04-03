'''
Immutable- as value (roughly said) integer tuple string we pass copy
Mutabble - as refereence list dictionary we pass reference
'''
#integer
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
# def change_no(num):
#     num.append(3)
#     print("Inside",num)

# num_val=[1,2]
# change_no(num_val)
# print("Outside",num_val)

def display4(passenger_name, *baggage_tuple,room='123'):
    print("Passenger name:",passenger_name)
    print("Room:",room)
    total_wt=0
    for baggage_wt in baggage_tuple:
        total_wt+=baggage_wt
    print("Total baggage weight in kg:", total_wt)

print("-------------------------------------------------")
print("code-4: variable argument count")
display4("Jack",12,8,5)
