# 8. Give me the discount
# Create a function in Python that accepts two parameters. 
# The first should be the full price of an item as an integer. 
# The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. 
# For example, if the price is 100 and the discount is 20, the function should return 80.

#alter_preis------rabatt-------neuer_preis

alter_preis = int(input("Bitte geben Sie den ursprünglichen Preis ein: "))
rabatt = int(input("Bitte geben Sie den Rabatt ein: "))

def rabatt_Funktion(alter_preis, rabatt):
    return alter_preis - alter_preis * rabatt / 100

print(rabatt_Funktion(alter_preis, rabatt))