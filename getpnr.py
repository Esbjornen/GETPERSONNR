import requests
import random 

looping=True



print("\nHämta personnummer från skatteverket!\n")

while looping:
    randomtal = random.randint(1, 100)

    url = f"https://skatteverket.entryscape.net/rowstore/dataset/b4de7df7-63c0-4e7e-bb59-1f156a591763/json?_offset={randomtal}&_limit=1"

    req = requests.get(url) 


    jsondata = req.json()
    lista=jsondata['results']
    print(lista)

    entill=input("\n Vill du slumpa ett personummer till? j/n\n")
    
    if (entill == "n" or entill == "N"):
        break