# 5. Hide the credit card number Write a function in Python that accepts a credit card number. 
# It should return a string where all the characters are hidden with an asterisk except the last four. 
# For example, if the function gets sent "4444444444444444", then it should return "4444".

def hideDigits(cardNumb3r):
    cardNumb3r_list = list(cardNumb3r)              #convert string to List
    
    for i in range(0,len(cardNumb3r_list)-4):       #iterate within range(start,stop,step) step is optional: default(1)
        cardNumb3r_list[int(i)] = "*"               #change char
        
    new_cardNumb3r = "".join(cardNumb3r_list)       #convert list into string
    return new_cardNumb3r                           #return string

cardNumb3r = input("Bitte Kreditkartennummer angeben (16-stellig)\nEingabe: ")
print(hideDigits(cardNumb3r))