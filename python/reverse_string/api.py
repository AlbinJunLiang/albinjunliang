from fastapi import FastAPI
import uvicorn 
from albin.python.reverse_string.main import ReverseStringSlicing, ReverseNative

app = FastAPI()

@app.get("/reverse")
def reverse(word : str = "HELLO WORLD"):
    return  {"reversed_word" : ReverseStringSlicing().reverse_string(word).upper(),
             "original": word}


@app.get("/reverse/{word}")
def reverse(word: str):
        return  {"reversed_word" : ReverseNative().reverse_string(word).upper(),
             "original": word}

# Bloque para ejecutar al correr el archivo directamente
if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)
    