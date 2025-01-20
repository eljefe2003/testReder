from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "¡Hola, Render! Tu servidor Flask está funcionando correctamente."

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"¡Hola, {nombre}! Bienvenido a Render."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
