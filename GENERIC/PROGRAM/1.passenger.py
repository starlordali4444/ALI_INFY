np=input("Enter No of Passenger:")
no_of_passenger =int(np)
while no_of_passenger!=0 :
    # print (no_of_passenger)
    nb=input("Enter No of Baggage:")
    no_of_baggage=int(nb)
    while no_of_baggage!=0:
        status=input("Enter Status of the baggage(Checked-C/Not Checked -N):")
        print("Passenger",no_of_passenger,"--Baggage",no_of_baggage,"is",status)
        no_of_baggage-=1
    no_of_passenger-=1