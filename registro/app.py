from flask import Flask,render_template,request,redirect,url_for
import mysql.connector

app = Flask(__name__)

db_connfig = {
    "host" : "localhost",
    "user" : "Jhoan",
    "password" : "1217",
    "database" : "formulario"
}

def add_user (nombre,apellido,telefono,email,contrasena,genero):
    conn= mysql.connector.connect(**db_connfig)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO registros (nombre,apellido,telefono,email,contrasena,genero) VALUES (%s,%s,%s,%s,%s,%s)",(nombre,apellido,telefono,email,contrasena,genero))
    conn.commit()
    conn.close
def del_user (nombre,email,contrasena):
    conn= mysql.connector.connect(**db_connfig)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE nombre=%s AND email=%s AND contrasena=%s",(nombre,email,contrasena))
    conn.commit()
    conn.close


@app.route("/")
def formulario ():
    return render_template("registro.html")

@app.route("/procesar_formulario", methods=["POST"])
def procesar_formulario() :
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    telefono = request.form["telefono"]
    email = request.form["email"]

    contrasena = request.form["contrasena"]
    genero = request.form["genero"]
    accion = request.form["but"]

    if accion=="Enviar":
        add_user(nombre,apellido,telefono,email,contrasena,genero)

    return redirect(url_for("home"))

@app.route("/home")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)

