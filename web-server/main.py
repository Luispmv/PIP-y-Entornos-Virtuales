import store

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

mi_nombre = "Pablo"

@app.get("/")
def get_list():
	return [1,2,3]

@app.get("/contact", response_class=HTMLResponse)
def get_list():
	return f'<h1 style="color:#ff0000;">Hola Mundo mi nombre es {mi_nombre}</h1>'

def run():
    store.get_categories()

if __name__=="__main__":
    run()



