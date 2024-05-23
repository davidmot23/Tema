import json
import os
import csv

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

#persoane1()



import pandas as pd

def jsontocsv():
    with open("tema_curs15/Tema/problema1.json", encoding='utf-8') as inputfile:
        df = pd.read_json(inputfile)

    df.to_csv("tema_curs15/Tema/output.csv", encoding='utf-8', index=False)

jsontocsv()