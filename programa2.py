import requests
import json
import os

token=os.environ["token"]
url_base="https://soccer.sportmonks.com/api/v2.0/"
payload={'api_token':token}


menu='''
    1- Buscar por liga.
    2- Mostrar todas las ligas disponibles.
    3- Salir
    '''
print(menu)
opcion=int(input("Selecciona una opción: "))

while opcion<1 or opcion>3:
    print("La opción debe estar comprendida entre 1 al 3.")
    opcion=int(input("Selecciona una opción: "))

#Mostrar/Buscar ligas o salir del programa.

if opcion==1:
    nombre_liga=input("Introduce el nombre de una liga: ")
    url=url_base+"leagues/search/"+nombre_liga

    r=requests.get(url,params=payload)
    if r.status_code == 200:
        datos=r.json()
        ligas=[]
        for liga in datos.get("data"):
            ligas.append(liga.get("name"))
        if len(ligas)!=0:
            print("\nRESULTADOS DE LA BÚSQUEDA:\n")
            for liga in ligas:
                print("-",liga)
        else:
            print("No se han encontrado ligas con ese nombre.")
    else:
        print("Error")
        print(r.status_code)

elif opcion==2:
    url=url_base+"leagues"
    r=requests.get(url,params=payload)
    if r.status_code == 200:
        datos=r.json()
        ligas=[]
        for liga in datos.get("data"):
            ligas.append(liga.get("name"))
        print("\nRESULTADOS DE LA BÚSQUEDA:\n")
        for liga in ligas:
            print("-",liga)
    else:
        print("Error")
        print(r.status_code)

elif opcion==3:
    print("Has salido del programa.")
    exit()

#Seleccionar liga

liga=input("\nIntroduce el nombre de una liga: ")
while liga not in ligas:
    print("La liga seleccionada, debe de ser una de las disponibles.\n\nLIGAS DISPONIBLES:\n")
    for var in ligas:
        print("-",var)
    liga=input("\nIntroduce el nombre de una liga: ")

#Asociar id de liga seleccionada a una variable

for var in datos.get("data"):
    if var.get("name")==liga:
        idliga=var.get("id")


#Mostrar temporadas de la liga seleccionada

url2=url_base+"seasons"
temporadas=[]

r2=requests.get(url2,params=payload)
if r2.status_code == 200:
        datos2=r2.json()
        for temporada in datos2.get("data"):
            if temporada.get("league_id")==idliga:
                temporadas.append(temporada.get("name"))
        print("\nTEMPORADAS DE LA %s:\n"%(liga).upper())
        for var2 in temporadas:
            print(var2)
        
else:
    print("Error")
    print(r2.status_code)


