from flask import Flask,redirect,render_template,request,url_for
import mysql.connector

app = Flask(__name__)

db_connfig = {
    "host" : "localhost",
    "user" : "Jhoan",
    "password" : "1217",
    "database" : "formulario"
}
conn= mysql.connector.connect(**db_connfig)
cursor = conn.cursor()


def most_users ():
        users = cursor.execute("SELECT * FROM `usuarios`")
        conn.commit()
        conn.close


def add_users(nombre,email,contraseña):
    cursor.execute("INSERT INTO usuarios (nombre,email,contrasena) VALUES (%s,%s,%s)",(nombre,email,contraseña))
    conn.commit()
    conn.close


def del_users(email,contraseña):
    cursor.execute("DELETE FROM usuarios WHERE email=%s AND contrasena=%s",(email,contraseña))
    conn.commit()
    conn.close


@app.route("/")
def reg ():
    return render_template("formulario.html")

@app.route("/procesar_formulario", methods=["GET", "POST"])
def form () :
    if request.method == "POST":
        nombre= request.form["nombre"]
        email= request.form["email"]
        contraseña= request.form["contrasena"]
        add_users(nombre,email,contraseña)
    return redirect(url_for("exito"))

@app.route("/exito")
def exito():
     return render_template("exito.html")

@app.route("/ver_usuarios")
def ver_usuarios() :
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    return render_template("index.html", usuarios=usuarios)
     
     



@app.route("/borrar_usuario", methods=["GET", "POST"])
def delete () :
    if request.method == "POST":
        email= request.form["email"]
        contraseña= request.form["contrasena"]
        del_users(email,contraseña)
        return redirect("/")
    return render_template("delete.html")



if __name__ == "__main__":
     app.run(debug=True)
"""@app.route("/borrar_usuario", methods=["GET", "POST"])
def form () :
     email= request.form["email"]
     contraseña= request.form["contrasena"]

     del_users(email,contraseña)"""
