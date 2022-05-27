# Proyecto-Final-LM_Parte-1

# Objetivo

El objetivo fundamental del proyecto es la realización de una página web alojada en Heroku y creada con el web framework python Flask, que utilizando algún servicio web proporcione una funcionalidad original.

Sería muy interesante que buscaras una API (o APIs) de algún tema que te interese, para que te resulte más atractivo realizar la práctica. Al entender más del tema será más fácil entender la documentación y utilizar las distintas funciones que te ofrece.

# Proceso

Estudio y búsqueda de uno o varios servicios web (API Restful). Si se va a escoger una sola API se recomienda que la autentificación sea con key, si escoges dos API, una de ella puede ser sin autentificación. Las API deben devolver json como lenguaje de marcas.

# Entrega

En redmine entrega los siguientes puntos:

- La ejecución y salida de 3 peticiones a la API principal (si eliges dos API, solo a una de ella) utilizando curl. Estas peticiones se harán sobre URL con parámetros.
- 3 programas python que muestren información de las consultas a la API (se pueden usar las mismas consultas que has utilizado en el punto anterior) utilizando la librería requests. 
- Una descripción de lo que va a hacer tu aplicación web utilizando estos servicios web.
- Las URL de la docuementación del servicio web (o servicios) que vais a utilizar.

Una vez que este corregida la parte 1, se abrirá la tarea de la 2ª parte.


#### ¿QUÉ HACE EL PROGRAMA 1?
- Nos mostrará la lista de continentes, a continuación le indicaremos un continente válido y nos mostrará la lista de países de dicho continente.

#### ¿QUÉ HACE EL PROGRAMA 2?
- El programa nos comienza mostrando un menú con una serie de opciones, escogemos una de las opciones ("Mostrar todas las ligas", "Buscar ligas" o "Salir del programa"). Una vez que introduzcamos la liga por teclado nos mostrará las temporadas en las que ha participado.

#### ¿QUÉ HACE EL PROGRAMA 3?
- El programa nos pedirá un nombre de un jugador. En caso de que encuentre varios resultados los mostrará y nos pedirá uno en concreto. Finalmente nos mostrará las estadísticas de dicho jugador.

## Descripción de lo que va a hacer la aplicación web
- La aplicación web servirá para conocer las estadísticas generales sobre futbol, ya sea información acerca de jugadores, equipos que pertenecen a una liga, y sus puestos, además de otras funcionalidades que incluye la API. Es cierto que la API está limitada, con esto me refiero a que no obtendremos la información completa, sino una parte de ella.


## URL de la documentación de la API
https://docs.sportmonks.com/football/
