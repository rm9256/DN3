def najvecja_vrednost(podatki):
    #print("test")
    dolzina = len(podatki)
    #print("dolzina je: ",dolzina)
    najvecje = [0] * dolzina
    #print(najvecje)
    i = 0
    najvecjaTemp = 0
    for x in podatki.values():
        #print("x je: ",x)
        for y in x:
            #print("y je: ",y)
            if y > najvecjaTemp:
                najvecjaTemp = y
        najvecje[i] = najvecjaTemp        
        najvecjaTemp = 0   
        i = i + 1
    print(najvecje)         

#data = {"prices": [41970, 40721, 41197, 41137, 43033],"volume": [49135346712, 50768369805, 47472016405, 34809039137, 38700661463]}
#najvecja_vrednost(data)