'''
Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding. Repetition of character has to be replaced by storing the length of that run.

Write a python function which performs the run length encoding for a given String and returns the run length encoded String.

'''

def encode(message):
    count=1
    res_msg=""
    message=list(message)
    print(message)
    for i in message:
        j=i+1
        if i==:
            count+=1
        else:
            count=1
        res_msg+=str(count)+i
    return res_msg

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
 