
def calculate_total_ticket_cost(no_of_adults, no_of_children):
    rate_of_adult=37550
    rate_of_child = rate_of_adult/3
    total_ticket_cost=no_of_adults*rate_of_adult+no_of_children*rate_of_child
    total_ticket_cost+=total_ticket_cost*0.07
    total_ticket_cost-=total_ticket_cost*0.10
    
    return total_ticket_cost

#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(5,2)
print("Total Ticket Cost:",total_ticket_cost)