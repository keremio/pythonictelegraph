def morse(letter):
    
     switcher = {
       "a" and "A": ".-",
       "b" and "B": "-...",
       "c" and "C": "-.-.",
       "d" and "D": "-..",
       "e" and "E": ".",
       "f" and "F": "..-.",
       "g" and "G": "--.",
       "h" and "H": "....",
       "i" and "I": "..",
       "j" and "J": ".---",
       "k" and "K": "-.-",  
       "l" and "L": ".-..",
       "m" and "M": "--",
       "n" and "N": "-.",
       "o" and "O": "---",
       "p" and "P": ".--.",
       "q" and "Q": "--.-",
       "r" and "R": ".-.",
       "s" and "S": "...",
       "t" and "T": "-",
       "u" and "U": "..-",
       "v" and "V": "...-",
       "w" and "W": ".--",
       "x" and "X": "-..-",
       "y" and "Y": "-.--",
       "z" and "Z": "--..",
       "1": ".----",
       "2": "..---",
       "3": "...--",
       "4": "....-",
       "5": ".....",
       "6": "-....",
       "7": "--...",
       "8": "---..",
       "9": "----.",
       "0": "-----",
       " ": "/"
        }
     return switcher.get(letter, " ")

import winsound
text = input()
for i in text:
    for j in morse(i):
        if (j == "."):
            print(j, end="")
            winsound.Beep(2000,150)
        if (j == "-"):
            print(j, end="")
            winsound.Beep(2000,450)  
        if (j == "/"):
            print(j, end="")
    print(" ", end="")
