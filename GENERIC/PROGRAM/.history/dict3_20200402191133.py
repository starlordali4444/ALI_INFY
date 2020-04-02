'''
Care hospital wants to know the medical speciality visited by the maximum number of patients. Assume that the patient id of the patient along with the medical speciality visited by the patient is stored in a list. The details of the medical specialities are stored in a dictionary as follows:
{
"P":"Pediatrics",
"O":"Orthopedics",
"E":"ENT
} 
Write a function to find the medical speciality visited by the maximum number of patients and return the name of the speciality.

Note: 

Assume that there is always only one medical speciality which is visited by maximum number of patients.

a_dictionary = {"a": 1, "b": 2, "c": 3}

max_key = max(a_dictionary, key=a_dictionary.get)   get key with max value


print(max_key)

all_values = a_dictionary.values()
max_value = max(all_values)     all_values is a list


print(max_value)
'''

def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    patient_medical_speciality_list= Convert(patient_medical_speciality_list)
    # print(patient_medical_speciality_list)
    s_list={}
    for i in medical_speciality:
        s_list[i]=0
    for key,val in patient_medical_speciality_list.items():
        s_list[val]+=key
    speciality=medical_speciality[(max(s_list,key=s_list.get))]
    return speciality

# def Convert(lst): 
#     res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)} 
#     return res_dct 

def Convert(lst): 
    it = iter(lst) 
    res_dct = dict(zip(it, it)) 
    return res_dct 

#provide different values in the list and test your program

patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,1656, 'E']

medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}


speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)