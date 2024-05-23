import json
import os


def persoane():
    persoane = [
        {
            "nume": "",
            "prenume":"",
            "varsta":""
        }
    ]
    with open("tema_curs15/Tema/problema1.json","w") as file:
        n=int(input("Va rog sa introduceti nr de persoane: "))
        for i in range(n):
            nume=(input(f"Va rog sa introduceti numele persoanei cu nr. {i} "))
            prenume=(input(f"Va rog sa introduceti prenumele persoanei cu nr. {i} "))
            varsta=(input(f"Va rog sa introduceti varsta persoanei cu nr. {i} "))
            for pers in persoane:
                pers['nume']=nume
                pers['prenume']=prenume
                pers['varsta']=varsta
                json.dump(persoane,file)

# persoane()


def persoane1():
    persoane = []
    with open("tema_curs15/Tema/problema1.json","w") as file:
        n=int(input("Va rog sa introduceti nr de persoane: "))
        for i in range(n):
            nume=(input(f"Va rog sa introduceti numele persoanei cu nr. {i+1} "))
            prenume=(input(f"Va rog sa introduceti prenumele persoanei cu nr. {i+1} "))
            varsta=(input(f"Va rog sa introduceti varsta persoanei cu nr. {i+1} "))
            Data = {'nume':nume,'prenume':prenume,'varsta':varsta}
            persoane.append(Data)
        json.dump(persoane,file)

persoane1()


