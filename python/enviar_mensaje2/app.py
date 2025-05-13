from flask import Flask,render_template,request,redirect,url_for
import mysql.connector

app = Flask(__name__)

db_connfig = {
    "host" : "localhost",
    "user" : "Jhoan",
    "password" : "1217",
    "database" : "formulario"
}

def add_user (nombre,email,contraseña):
    conn= mysql.connector.connect(**db_connfig)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nombre,email,contrasena) VALUES (%s,%s,%s)",(nombre,email,contraseña))
    conn.commit()
    conn.close
def del_user (nombre,email,contraseña):
    conn= mysql.connector.connect(**db_connfig)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE nombre=%s AND email=%s AND contrasena=%s",(nombre,email,contraseña))
    conn.commit()
    conn.close


@app.route("/")
def formulario ():
    return render_template("formulario.html")

@app.route("/procesar_formulario", methods=["POST"])
def procesar_formulario() :
    nombre = request.form["nombre"]
    email = request.form["email"]
    contrasena = request.form["contrasena"]
    accion = request.form["but"]

    if accion=="Enviar":
        add_user(nombre,email,contrasena)
    if accion=="eliminar":
        del_user(nombre,email,contrasena)

    return redirect(url_for("exito"))

@app.route("/exito")
def exito():
    return render_template("exito.html")

if __name__ == "__main__":
    app.run(debug=True)

