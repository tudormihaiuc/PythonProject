import nltk
#nltk.download('punkt')
from nltk.tokenize import sent_tokenize

def function():
    nrOfLetters=0
    frOfLetters = {}
    percentages = {}
    phoneNumbers=[]
    cnp={}
    file = open("test.txt", "rt")
    data=file.read()
    nrOfSentences=sent_tokenize(data)
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
        x = len(words)
        i = 0
        while (i < x):
            if words[i].isnumeric():
                if words[i][0] == "0" and words[i][1] == "7" and len(words[i]) == 10:
                        phoneNumbers.append(words[i])
                words.remove(words[i])
                x = len(words)
            else:
                i += 1
    print("Cuvinte = ",len(words))
    print("Propozitii: ",len(nrOfSentences))
    print("Litere: ")
    for i in frOfLetters:
        print(i," = ",frOfLetters[i]," (",percentages[i],"%)")
    resList = list(dict.fromkeys(phoneNumbers))
    print("Telefoane= ", len(resList),resList)

function()
