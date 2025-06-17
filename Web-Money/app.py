from flask import Flask,render_template,request,redirect,url_for,flash
import mysql.connector

app = Flask(__name__)
app.secret_key = "secretkey"

db_connfig = {
    "host" : "localhost",
    "user" : "Jhoan",
    "password" : "1217",
    "database" : "formulario"
}
#-----------coneccion con la base de datos------------
try:
    conn = mysql.connector.connect(**db_connfig)
    cursor = conn.cursor()
except mysql.connector.errors.InterfaceError as err :
    print (f"error en la base de datos {err}")

#---------Funciones CRUD ---------
def add_user (nombre,apellido,telefono,email,contrasena,genero):
    try:
        cursor.execute("INSERT INTO registros (nombre,apellido,telefono,email,contrasena,genero) VALUES (%s,%s,%s,%s,%s,%s)",(nombre,apellido,telefono,email,contrasena,genero))
        conn.commit()
        flash ("usuario  agregado")
        return 1
    except mysql.connector.Error as err:
        flash (f"no se puede conectar con la base de datos, usuario no agregado: error {err}")
        return 0
    finally:
        conn.close

#-------templates y procesaminetos---------
@app.route("/")
def registrate():
    return render_template("registrate.html")

@app.route("/procesar_registro", methods = ["POST"])
def procesar_registro ():
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    contrasena = request.form["contrasena"]
    email = request.form["email"]
    telefono = request.form["telefono"]
    genero = request.form["genero"]

    re = add_user(nombre,apellido,telefono,email,contrasena,genero)

    if re == 0 :
        print("0")
    if re == 1 :
        print("1")

    return redirect(url_for("crud"))

@app.route("/crud")
def crud ():
    return render_template("crud.html")

if __name__ == "__main__":
    app.run(debug=True)