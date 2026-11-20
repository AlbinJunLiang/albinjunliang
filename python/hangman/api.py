from fastapi import FastAPI
import uvicorn 

app = FastAPI()

@app.get("/")
def leer_raiz():
    return {"mensaje": "¡Hola desde FastAPI!"}

@app.get("/hola")
def leer_raiz():
    return {"mensaje": "¡Hola!"}

# Bloque para ejecutar al correr el archivo directamente
if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)
    