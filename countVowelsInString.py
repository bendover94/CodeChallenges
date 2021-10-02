# 4. Count the vowels in a string
# Create a function in Python that accepts a single word 
# and returns the number of vowels in that word. In this function, 
# only a, e, i, o, and u will be counted as vowels — not y.

def countVowels(word):
    kleinBuchstaben_word = word.lower()
    vowel = 0

    for letters in kleinBuchstaben_word:
        if letters == "a" or letters == "e" or letters == "i" or letters == "o" or letters == "u":
            vowel+=1
        else:
            pass
    print(vowel)

while 1:
    word = input("Bitte geben Sie ein Wort ein\nEingabe: ")
    countVowels(word)
