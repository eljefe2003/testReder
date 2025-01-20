import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "¡Hola, Render! Tu servidor Flask está funcionando correctamente."

if __name__ == "__main__":
    # Usar el puerto proporcionado por Render o 5000 como predeterminado
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
