def convert_temp(temp, unit):
    if unit=='C':
        res_temp=temp*9/5+32
    elif unit=='F':
        res_temp=(temp-32)*5/9
    else:
        res_temp="Incorrect Unit"
    return res_temp
    
print("Temp - ",convert_temp(104,'A'))