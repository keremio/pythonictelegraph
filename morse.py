import winsound
choice = input("press d to decrypt the morse code, c to create one\n")
morsedict = {
       "a" : ".-",
       "b" : "-...",
       "c" : "-.-.",
       "d" : "-..",
       "e" : ".",
       "f" : "..-.",
       "g" : "--.",
       "h" : "....",
       "i" : "..",
       "j" : ".---",
       "k" : "-.-",  
       "l" : ".-..",
       "m" : "--",
       "n" : "-.",
       "o" : "---",
       "p" : ".--.",
       "q" : "--.-",
       "r" : ".-.",
       "s" : "...",
       "t" : "-",
       "u" : "..-",
       "v" : "...-",
       "w" : ".--",
       "x" : "-..-",
       "y" : "-.--",
       "z" : "--..",
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

inv_morsedict = {v: k for k, v in morsedict.items()}
def morse(m):
    m = m.split()
    for i in m:
        print(inv_morsedict[i], end = "")
def text(t):
    t = t.lower()
    t = list(t)
    for i in t:
        print(morsedict[i], end = " ")
        for j in morsedict[i]:
            if (j == "."):
                winsound.Beep(2000,150)
            if (j == "-"):
                winsound.Beep(2000,450)  
                
        
if (choice == 'D' or choice == 'd'):
    morse(input())
elif (choice == 'C' or choice == 'c'):
    text(input())
else:
    print("WRONG DECISION, TRY AGAIN\n")
