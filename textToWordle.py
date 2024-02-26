from typing import List

b = "⬛"
y = "🟨"



class consts:
    YELLOWROW = y+y+y + "\n"
    BLACKROW = b+b+b + "\n"
    BLACKCENTER = y+b+y + "\n"
    YELLOWCENTER = b+y+b + "\n"
    MISSINGEND = y+y+b + "\n"
    MISSINGSTART = b+y+y + "\n"
    LEFTYELLOW = y+b+b + "\n"
    RIGHTYELLOW = b+b+y + "\n"

    A = b+y+b+"\n"+y+b+y+"\n"+y+y+y+"\n"+y+b+y+"\n"+y+b+y+"\n"
    B = y+y+b+"\n" + BLACKCENTER + YELLOWROW + BLACKCENTER + y+y+b+"\n"
    C = YELLOWCENTER + BLACKCENTER + LEFTYELLOW + BLACKCENTER + YELLOWCENTER
    D = MISSINGEND + BLACKCENTER + BLACKCENTER + BLACKCENTER + MISSINGEND
    E = YELLOWROW + LEFTYELLOW + YELLOWROW + LEFTYELLOW + YELLOWROW
    F = YELLOWROW + LEFTYELLOW + YELLOWROW + LEFTYELLOW + LEFTYELLOW
    G = MISSINGSTART + LEFTYELLOW + y+b+y+"\n" + BLACKCENTER + MISSINGSTART
    H = BLACKCENTER + BLACKCENTER + YELLOWROW + BLACKCENTER + BLACKCENTER
    I = YELLOWROW + YELLOWCENTER + YELLOWCENTER + YELLOWCENTER + YELLOWROW
    J = YELLOWROW + YELLOWCENTER + YELLOWCENTER + YELLOWCENTER + MISSINGEND
    K = BLACKCENTER + MISSINGEND + LEFTYELLOW + MISSINGEND + BLACKCENTER
    L = LEFTYELLOW + LEFTYELLOW + LEFTYELLOW + LEFTYELLOW + YELLOWROW
    M = BLACKCENTER + YELLOWROW + YELLOWROW + BLACKCENTER + BLACKCENTER
    N = BLACKCENTER + YELLOWROW + YELLOWROW + YELLOWROW + BLACKCENTER
    O = YELLOWROW + BLACKCENTER + BLACKCENTER + BLACKCENTER + YELLOWROW
    P = YELLOWROW + BLACKCENTER + YELLOWROW + LEFTYELLOW + LEFTYELLOW
    Q = YELLOWROW + BLACKCENTER + YELLOWROW + RIGHTYELLOW + RIGHTYELLOW
    R = YELLOWROW + BLACKCENTER + YELLOWROW + MISSINGEND + BLACKCENTER
    S = YELLOWROW + LEFTYELLOW + YELLOWROW + RIGHTYELLOW + YELLOWROW
    T = YELLOWROW + YELLOWCENTER + YELLOWCENTER + YELLOWCENTER + YELLOWCENTER
    U = BLACKCENTER + BLACKCENTER + BLACKCENTER + BLACKCENTER + YELLOWROW
    V = BLACKCENTER + BLACKCENTER + BLACKCENTER + BLACKCENTER + YELLOWCENTER
    W = BLACKCENTER + BLACKCENTER + YELLOWROW + YELLOWROW + BLACKCENTER
    X = BLACKCENTER + BLACKCENTER + YELLOWCENTER + BLACKCENTER + BLACKCENTER
    Y = BLACKCENTER + BLACKCENTER + BLACKCENTER + YELLOWCENTER + YELLOWCENTER
    Z = YELLOWROW + RIGHTYELLOW + YELLOWCENTER + LEFTYELLOW + YELLOWROW
    SPACE = (b+b+b+"\n")*5

    @staticmethod
    def getLetter(letter : str):
        try:
            return getattr(consts, letter.upper()).split("\n")
        except:
            return consts.SPACE.split("\n")

def printMaxLength(test : str, width: int = 6):

    words = test.split(" ")

    i = 0
    toReturn = []

    while i < len(words):
        if len(words[i]) > width: # More cheracters then allowed
            word = words[i]
            toAdd = []
            j = 0 
            while j < len(word):
                textToConvert = word[j:j+5]
                textToConvert += " " * (5 - len(textToConvert))
                tmpStr = ""
                for x in range(5):
                    for letter in textToConvert:
                        tmpStr += letterToSymbols(letter).split("\n")[x]
                    tmpStr += "\n"
                toAdd.append(tmpStr)
                j += 5
            
            toReturn.extend(toAdd)

        

        else:
            tmpStr = ""
            word = words[i] 

            while True:
                if (i + 1 < len(words) and len(words[i + 1]) + len(word) < width):
                    i += 1
                    word += " " + words[i]
                else:
                    break     
                    
                           

            word += " " * (width - len(word))

            for x in range(5):
                for letter in word:
                    tmpStr += letterToSymbols(letter).split("\n")[x]
                tmpStr += "\n"

            toReturn.append(tmpStr)


        i += 1


    [print(line) for line in toReturn]

    return toReturn

def letterToSymbols(test : str) -> str:
    str = ""
    for x in range(5):
        for letter in test:
            str += consts.getLetter(letter)[x] + b
        str += "\n"

    return str

printMaxLength("It now will place stuff on the same line!", 6)