# Write a function named format_number that takes a non-negative number as its only parameter.
# Your function should convert the number to a string and add commas as a thousands separator.
# For example, calling format_number(1000000) should return "1,000,000".

#print(1_000_000)

                                    # short Version
def format_number(inputNumb3r):
    return (f"{inputNumb3r:,}")

#output = format_number(int(input("Bitte geben Sie eine Zahl ein: ")))
#print(type(output))
#print(output)


                                    # long Version
stringy = input("Bitte geben Sie eine Zahl ein: ")                        #get string
backwards_stringy = stringy [::-1]                                        #reverse string

stringList = list(backwards_stringy)                                      # convert string to list
newString = []                                                            # initiate new list

for element in range(len(stringList)):                                    # bei %3 Rest != 0 nur element (außer bei element 0)
    if element % 3 != 0 or element == 0:
        newString.insert(element, stringList[element]) 
    else:
        newString.insert(element, "," + stringList[element])              # bei %3 Rest == 0 insert , + element
        

realString = "".join(newString)                                           # convert list to string
print(realString[::-1])                                                   # rearange string
