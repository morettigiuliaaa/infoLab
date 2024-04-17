#creo un dizionario
dizionario = {"rossi":18,"bianchi":16,"verdi":6}

#inserire un elemento dentro il dict
dizionario["viola"]=14
print(dizionario)

#modificare una coppia chiave/valore
dizionario["bianchi"]=18
print(dizionario)

#iterare sul dizionario
for key,value in dizionario.items():
    print("La chiave è ..."+key)
    print("Il valore è ..."+str(value))

#calcolare il totale delle ore del dizionario
def calcoloOre(dizionario):
    valori=0
    for key,value in dizionario.items():
        valori=valori+value
    return(valori)

#numero degli insegnanti con cattedra piena
def calcoloInsegnanti(dizionario):
    insegnanti=0
    for key,value in dizionario.items():
        if value == 18:
            insegnanti+=1
    return(insegnanti)

#funzione
def stampaDizionario(dizionario):
 for key,value in dizionario.items():
    print("La chiave è ..."+key)
    print("Il valore è ..."+str(value))

#richiamo la funzione
stampaDizionario(dizionario)
print(calcoloOre(dizionario))
print(calcoloInsegnanti(dizionario))

#scrivere una funzione che modifichi le ore allocate ad un insegnante
def modificaOre(dizionario,chiave,ore):
    if chiave in dizionario:
        dizionario[chiave]=ore
    return(dizionario)

print(modificaOre(dizionario,"rossi",100))

#scalaore
def scalaore(dizionario,chiave,ore):
    monteore=0
    for chiave,value in dizionario:
        monteore=value
    if chiave in dizionario:
        dizionario[chiave]=monteore-ore
        if ore<=0:
            print("ORE ESAURITE")
    print(dizionario)

scalaore(dizionario,"rossi",5)