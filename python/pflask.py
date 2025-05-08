from flask import Flask

app = Flask(__name__)

@app.route('/')
def mostrar ():
    return "<h1>buenos dias </h1>"

if __name__ == "__main__":
    app.run()