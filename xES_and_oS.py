# 6. Are the Xs equal to the Os?
# Create a Python function that accepts a string. 
# This function should count the number of Xs and the number of Os in the string. 
# It should then return a boolean value of either True or False.
# If the count of Xs and Os are equal, then the function should return True. 
# If the count isn't the same, it should return False. 
# If there are no Xs or Os in the string, it should also return True because 0 equals 0. 
# The string can contain any type and number of characters.

def count_X_and_O(inputString):
    x = 0
    o = 0
    inputString = inputString.lower()
    listFromString = list(inputString)
    for i in range(0, len(listFromString)):
        if listFromString[i] == "x":
            x+=1
        elif listFromString[i] == "o":
            o+=1
        else:
            pass
    if int(x) == int(o):
        result = True
    else:
        result = False
        
    return result

inputString = input("Geben Sie einen String ein, der X und O enthält\nEingabe: ")
print(count_X_and_O(inputString))