def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_no=100  
    ticket_number_list=[]  
    while no_of_passengers>0:
        temp_ticket=airline+':'+source[:3]+':'+destination[:3]+':'+str((ticket_no+1))
        ticket_no+=1       
        ticket_number_list.append(temp_ticket)
        no_of_passengers-=1

    return ticket_number_list[-5:]

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",10))