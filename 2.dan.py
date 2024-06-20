import re

# Path to your file
file_path = '2.dan.txt'

vrstice = [line.strip() for line in open(file_path)]
vsota = 0

for vrstica in vrstice:
    vrstica = vrstica.split(":")
    GameID = vrstica[0].split(" ")[1]
    GameID = int(GameID)

    desna = vrstica[1].split(" ")
    #print(desna)
    maxr = 0
    maxg = 0
    maxn = 0
    for i in range(1, len(desna), 2):
        #print()
        #print(i)
        stevilka_barve = desna[i]
        stevilka_barve = int(stevilka_barve)
        barva_stevilke = desna[i+1]
        barva_stevilke = barva_stevilke[0]
        #print(stevilka_barve, barva_stevilke)
        if barva_stevilke == "r":
            maxr = max(maxr, stevilka_barve)
        elif barva_stevilke == "g":
            maxg = max(maxg, stevilka_barve)
        elif barva_stevilke == "b":
            maxn = max(maxn, stevilka_barve)
    vsota += maxr*maxg*maxn
print(vsota)

    #break 