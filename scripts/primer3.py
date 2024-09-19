#! /usr/bin/python3


import time
from copy import copy, deepcopy  # z kopiranje seznamov






global spreme   #tako defeniramoglobalno spremenljivko/ 
spreme = 1
spr2 = True
spr3 = 0.4
spr4 = "besedilo"
spr5 ='Besedilo'
spr6 = 'f3a'
toJeSpremenljivka7 = 7

seznam = [0.4, 0.6, 6.3]  # To je seznam - list

t = (4, 3, 7)   # to je tuple

d = {"avto" : "žkoda" , "ime":"Alež", "starost" :32}# to je dictionary/slovar

print(seznam[2]) #tako se indeksira tuple in list
print(t[0])
print(d["ime"]) #tako se indeksira slovar

"""
to je
večvrstični
komentar
"""




print("seznam na mestu 2: " +str(seznam[2]))
print("seznam na mestu 2: " +repr(seznam[2]))
print(f"SEznam na mestu 2: {seznam[2]}, na mestu 1 pa : {seznam[1]}")


#tako se spremeni vrednost v seznamih in slovarjih
seznam[0] = 30
d["starost"]= 33

print(d)
print(seznam)


seznam.append(88)
seznam.insert(0, 66)
d["naslov"] = "tržaška 25"

print(d)
print(seznam)

novseznam = seznam   #izogni se temu

novnovseznam = copy(seznam)   # računalnik naredi nov svoj seznam  kopiramo objekt (samo prvi nivo)
novnovnovseznam = deepcopy(seznam)   #zelo počasen!!!   kopiramo celoten objekt

x, y, z = t

_, _, x1, y1, _ = seznam

print(x, y, z)
print(x1, y1)

a = b = c = 66

def main():
    print("hello world")


if __name__ == "__main__":
    main()