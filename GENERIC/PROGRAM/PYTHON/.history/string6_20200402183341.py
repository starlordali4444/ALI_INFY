'''
Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding. Repetition of character has to be replaced by storing the length of that run.

Write a python function which performs the run length encoding for a given String and returns the run length encoded String.

'''

def encode(string):
    counter = 1
    result = ""
    previousLetter = message[0]
    if len(message)==1:
      return str(1) + message[0]
    for i in range(1,len(message),1):
        if not message[i] == previousLetter:
            result += str(counter) + message[i-1]
            previousLetter = message[i]
            counter = 1

        else:
            counter += 1
        if i == len(message)-1:
                result += str(counter) + string[i]

    return result

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
