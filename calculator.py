# 7. Create a calculator function
# Write a Python function that accepts three parameters. 
# The first parameter is an integer. 
# The second is one of the following mathematical operators: +, -, /, or . 
# The third parameter will also be an integer.
# The function should perform a calculation and return the results. 
# For example, if the function is passed 6 and 4, it should return 24.


def calc_function(num_1, operator, num_2):
    if operator == "+":
        return int(num_1) + int(num_2)
    elif operator == "-":
        return int(num_1) - int(num_2)
    elif operator == "*":
        return int(num_1) * int(num_2)
    elif operator == "/":
        if num_2 == "0":
            return "division durch 0 machen wir hier nicht"
        else:
            return int(num_1) / int(num_2)
    else:
        print("Falsche Eingabe!")


while 1:
    num_1 = input("\nNummer 1: ")
    operator = input("Operand : ")
    num_2 = input("Nummer 2: ")
    print(f"\nDas Ergebnis von {num_1} {operator} {num_2} = " + str(calc_function(num_1, operator, num_2)))
    #print("\nDas Ergebnis von " + num_1 + " " + operator + " " + num_2 +  " = " + str(calc_function(num_1, operator, num_2)))
   

    
# print(str(calc_function(4, "+", 2)))
