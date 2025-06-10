from flask import Flask,render_template,request,redirect,url_for
import mysql.connector


app = Flask(__name__)

db_connfig = {
    "host" : "localhost",
    "user" : "Jhoan",
    "password" : "1217",
    "database" : "formulario"
}
conn = mysql.connector.connect(**db_connfig)
cursor = conn.cursor()

@app.route("/")
def formulario ():
    return render_template("registro.html")

#--------------------------------------------aqui estan la funciones CRUD----------------------------------------------------------------



def add_user (nombre,apellido,telefono,email,contrasena,genero):
    cursor.execute("INSERT INTO registros (nombre,apellido,telefono,email,contrasena,genero) VALUES (%s,%s,%s,%s,%s,%s)",(nombre,apellido,telefono,email,contrasena,genero))
    conn.commit()
    conn.close
def del_user() :
    pass
def update_user():
    pass
"""def del_user (nombre,email,contrasena):
    cursor.execute("DELETE FROM usuarios WHERE nombre=%s AND email=%s AND contrasena=%s",(nombre,email,contrasena))
    conn.commit()
    conn.close
"""
#-------------------------------------------aqui termian la funciones CRUD----------------------------------------------------------------


#ruta principal (Insert)
@app.route("/")
def formulario ():
    return render_template("registro.html")

#prosesa formulario e inteviene los datos(Insert)
@app.route("/procesar_formulario", methods=["GET", "POST"])
def procesar_formulario() :
    nombre = request.form["Nombre"]
    apellido = request.form["Apellido"]
    telefono = request.form["Telefono"]
    email = request.form["Email"]

    contrasena = request.form["Contrasena"]
    genero = request.form["Genero"]
    accion = request.form["but"]

    if accion=="enviar":
        add_user(nombre,apellido,telefono,email,contrasena,genero)

    return redirect(url_for("home_crud"))

#luego de que se autentique el insert se lleva al home CRUD
@app.route("/home-crud")
def home_CRUD():
    cursor.execute("SELECT id, nombre, apellido, telefono,email,contrasena, genero FROM registros")
    usuarios = cursor.fetchall()
    return render_template("crud.html", usuarios=usuarios)



@app.route("/opc-crud")
def opc_crud() :
    pass






    
if __name__ == "__main__":
    app.run(debug=True)

