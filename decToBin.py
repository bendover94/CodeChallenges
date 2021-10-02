# 3. Convert a decimal number into binary
# Write a function in Python that accepts a decimal number and returns the equivalent binary number. 
# To make this simple, the decimal number will always be less than 1,024, 
# so the binary number returned will always be less than ten digits long.

def getInput():
    return input("\nBitte geben Sie eine Dezimalzahl ein die zu binär konvertiert werden soll.\nEingabe: ")
    
def convert_dec_to_bin(dec_input):
    if dec_input > 1024:
        print("\nBitte wählen Sie eine Dezimalzahl kleiner als 1024,\ndamit die konvertierte binäre Zahl maximal 10 Stellen hat.\n")
        getInput()
    else:
        print("Ihre dezimale Zahl wurde zu binär konvertiert.\n")
        return bin(dec_input)

while 1:
    print(convert_dec_to_bin(int(getInput())))