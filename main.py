
def function():
    nrOfLetters=0;
    frOfLetters = {}
    percentages = {}
    file = open("test.txt", "rt")
    data=file.read()
    for char in data:
        if char.isalpha():
            char=char.upper()
            if char in frOfLetters:
                frOfLetters[char]=frOfLetters[char]+1
                nrOfLetters+=1
            else:
                frOfLetters[char]=1
                nrOfLetters+=1
    words=data.split()
    for char in frOfLetters:
        if char.isalpha():
           percentages[char]=frOfLetters[char]/nrOfLetters*100
    for i in words:
        if i.isnumeric():
            words.remove(i)
    print(words)
    print("Cuvinte = ",len(words))
    print("Litere: ")
    for i in frOfLetters:
        print(i," = ",frOfLetters[i]," (",percentages[i],"%)")

function()