import json

in_file= open("Fragen.txt","rt")
Quiz = json.loads(in_file.read())
in_file.close()

SL=[]
      
def players():
    AnzSp=int(input("Wie viele Spieler spielen mit?""\t"))
    for i in range(1,AnzSp+1):
        spieler = "Name von Spieler "+ str(i)+":"
        SpName=input(spieler)
        SL.append([SpName,0])
    return AnzSp

def print_question(L,r):
    print(L[r][0])

def print_answers(L,r):
    länge = len(L[r][1])
    for i in range(0,länge):
        print(L[r][1][i])

def correct_answer(L,r,RAntwort):
    Antworten=L[r][2]
    if RAntwort==L[r][2] :
        correct = True
    else:
        correct =False
    return correct

def result_answers(y,r,L,SL):
    print("Die richtige Antwort war ",L[r][2],"\n") 
    for i in range(0,y):
        print(SL[i][0], "hat momentan",SL[i][1],"Punkt(e).""\n")

def give_player_key():
    AnzSp=int(input("Wie viele Spieler spielen mit?""\t"))
    for i in range(1,AnzSp+1):
        spieler = "Name von Spieler "+ str(i)+":"
        SpName=input(spieler)
        key = "Taste von Spieler "+ str(i)+":"
        SpKey = input(key)
        SL.append([SpName,0,SpKey])
    return AnzSp

def get_player_by_key(pressedKey):
    for i in range(0,len(SL)):
        if SL[i][2] == pressedKey:
            foundPlayer = SL[i][2]
            return foundPlayer

print("Verfügbare Spielarten:")
print("1 - Jeder Spieler gibt eine Antwort ab.")
print("2 - Jeder Spieler bekommt eine Taste zugewiesen, drückt er diese,\nist er der einzige der die Frage beantworten darf.")
Spielart = input("Welche möchtest du nutzen?")

if Spielart == 1:
    y=players()        
    f=len(Quiz)
    for o in range (0,f):
        print_question(Quiz,o)
        print_answers(Quiz, o)
        for u in range(0,y):
            print(SL[u][0],"ist an der Reihe") 
            x=input("Antwort:")
        
            if correct_answer(Quiz,o,x):
                SL[u][1]=SL[u][1]+1
        if o != f-1:
            result_answers(y,o,Quiz,SL)
    for i in range(0,y):
        print(SL[i][0],"hat",SL[i][1],"Punkt(e) von möglichen",f,"Punkten erreicht")

if Spielart == 2:        
    y=give_player_key()        
    f=len(Quiz)
    for o in range (0,f):
        print_question(Quiz,o)
        print_answers(Quiz, o)
        PressedKey = input("Wenn du die Antwort weißt, drücke deine Taste!")
            print(SL[u][0],"ist an der Reihe")
            x=input("Antwort:")
            if correct_answer(Quiz,o,x):
                SL[u][1]=SL[u][1]+1
        if o != f-1:
            result_answers(y,o,Quiz,SL)
    for i in range(0,y):
        print(SL[i][0],"hat",SL[i][1],"Punkt(e) von möglichen",f,"Punkten erreicht")
