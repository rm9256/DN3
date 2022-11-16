def emso_leta_preracun():
    emso = (input("Vnesi EMSO: "))
    emso = emso[4:7]
    letoRojstva = int(emso)
    #print(type(letoRojstva))
    #print(letoRojstva)
    if letoRojstva < 23:
        letoRojstva = letoRojstva + 2000
    else:
        letoRojstva = letoRojstva + 1000
    #print(letoRojstva)    
    starost = 2022 - letoRojstva
    print("Star si ", starost)
    return starost

#emso_leta_preracun()    
