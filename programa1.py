import requests
import json
import os

token=os.environ["token"]
url_base="https://soccer.sportmonks.com/api/v2.0/"
payload={'api_token':token}

url=url_base+"continents"

continentes=[]

r=requests.get(url,params=payload)

if r.status_code == 200:
    datos=r.json()
    for continente in datos.get("data"):
        continentes.append(continente.get("name"))
    print("LISTA DE CONTINENTES:")
    for var in continentes:
        print(var)

    continente=input("\nSelecciona un continente: ")
    while continente not in continentes:
        print("El continente no existe.")
        continente=input("\nSelecciona un continente: ")
    

    url2=url_base+"countries"
    paises=[]

    r2=requests.get(url2,params=payload)
    if r2.status_code == 200:
        datos2=r2.json()
        for pais in datos2.get("data"):
            if pais.get("extra"):
                if pais.get("extra").get("continent") == continente:
                    paises.append(pais.get("name"))

        print("\nPAÍSES DE",(continente).upper())
        for var2 in paises:
            print(var2) 
    else:
        print("Error")
        print(r2.status_code)

else:
    print("Error")
    print(r.status_code)