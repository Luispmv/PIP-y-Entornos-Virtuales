#PIP-y-Entornos-Virtuales

#De csv a grafico con la carpeta Graficos

Dentro de la carpte Graficos creamos un pequeño proyecto que toma informacion de paises alojada en un archivo csv.

Queriamos que este proyecto no tuviera problemas con las dependencias asi que esta carpeta en especifico cuenta con un entorno virtual.

## Paso a paso para usar nuestro proyecto

cd Graficos --> nos movemos a la carpeta Graficos

python3 -m -venv env --> Una vez nos encontramos en la carpeta creamos un nuevo entorno virtual, en este caso lo llamamos env, tu lo puedes llamar como quieras.

source /env/bin/activate --> Una vez creamos el entorno virtual lo activamos

ls --> Listamos el contenido de Graficos y podemos ver la existencia de un archivo llamado requirements.txt

cat requirements.txt --> Vemos el contenido del archivo y podemos observar que aqui se encuentran todas las dependencias necesarias para que el proyecto funcione

pip3 install -r requirements.txt --> instalamaos todas las dependencias del archivo 

python3 main.py