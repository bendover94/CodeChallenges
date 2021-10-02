# 2. Sort a list
# Create a function in Python that accepts two parameters. The first will be a list of numbers. 
# The second parameter will be a string that can be one of the following values: asc, desc, and none.
# If the second parameter is "asc," then the function should return a list with the numbers in ascending order. 
# If it's "desc," then the list should be in descending order, and if it's "none," it should return the original list unaltered.

list_1 = [7,5,3,8,12,1,2,9,6,4,11,10]
input_arg = "asc"

def arrangeList(list, input_arg):
    if input_arg == "asc":
        list.sort()
        print("Die Liste wurde aufsteigend sortiert\n", list)
    elif input_arg == "desc":
        list.sort(reverse=True)
        print("Die Liste wurde absteigend sortiert\n", list)
    else:
        print("\nkein gültiger Sortierstil\n")


while input_arg != "q":
    print("\nDas ist die ungeordnete Liste\n", list_1)

    input_arg = input("\nBitte wählen Sie 'asc' oder 'desc' um festzulegen wie die Liste sortiert werden soll.\nEingabe: ")
    arrangeList(list_1, input_arg)
