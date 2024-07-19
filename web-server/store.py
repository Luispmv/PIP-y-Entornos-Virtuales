import requests


def get_categories():
    #Lllamamos a la funcion get del metodo requests y como argumento le pasamos el link con la lista de categorias
    r = requests.get("https://api.escuelajs.co/api/v1/categories")
    
    #Imprimimos el estado de la peticion
    print(r.status_code)

    #Imprimimos en consola la peticion como string
    print(r.text)

    #Formateamos nuestra peticion a JSON y ahora podemos iterar sobre ella como un diccionario
    cateogories = r.json()

    #Por cada category en nuestro JSON categories imprimimos el nombre de la categoria
    for category in cateogories:
        print(category["name"])


