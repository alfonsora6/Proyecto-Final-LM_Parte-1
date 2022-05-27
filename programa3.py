import requests
import json
import os

token=os.environ["token"]
url_base="https://soccer.sportmonks.com/api/v2.0/"
payload={'api_token':token}

print("BÚSQUEDA DE JUGADORES\n")
jugador=input("Introduce el nombre de un jugador: ")

url=url_base+"players/search/"+jugador


r=requests.get(url,params=payload)
if r.status_code == 200:
    datos=r.json()
    jugadores=[]
    for jugador in datos.get("data"):
        jugadores.append(jugador.get("display_name"))
    
    if len(jugadores)>1:
        encontrado=True
        print("\nLISTA DE JUGADORES ENCONTRADOS:\n")
        for var in jugadores:
            print("-",var)
        jugador=input("\nIntroduce el nombre de uno de los jugadores encontrados: ")
        while jugador not in jugadores:
            print("Debes escoger uno de los jugadores encontrados.")
            jugador=input("\nIntroduce el nombre de uno de los jugadores encontrados: ")

    elif len(jugadores)==1:
        encontrado=True
        print("\nJUGADOR ENCONTRADO:\n")
        for var in jugadores:
            print("-",var)
            jugador=var

    else:
        print("No se han encontrado jugadores con ese nombre.")
        encontrado=False
    
    if encontrado==True:
        print("\nEstadísticas de %s\n"%jugador)
        for var in datos.get("data"):
            if var.get("display_name")==jugador:
                print("- Nombre Completo: %s" %var.get("fullname"))
                print("- Nacionalidad: %s" %var.get("nationality"))
                print("- Fecha de nacimiento: %s" %var.get("birthdate"))
                print("- País de nacimiento: %s" %var.get("birthcountry"))
                print("- Lugar de nacimiento: %s" %var.get("birthplace"))
                print("- Altura: %s" %var.get("height"))

else:
    print("Error")
    print(r.status_code)
