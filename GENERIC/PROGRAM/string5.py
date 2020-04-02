def count_names(name_list):
    count1=0
    count2=0
    
    #start writing your code here
    for i in name_list:
        if(((i.find("at"))==1) and len(i)==3):# if((i.endswith("at")) and len(i)==3):
            count1+=1
        if(i.find("at"))>=0:
            count2+=1
    print("_at -> ",count1)
    print("%at% -> ",count2)

name_list=["Hat","Cat","rabbit","matter"]
# name_list=['Rat', 'saturday']
count_names(name_list)