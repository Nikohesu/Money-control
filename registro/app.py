from flask import Flask,render_template,request,redirect,url_for,flash
import mysql.connector


app = Flask(__name__)
app.secret_key = "clave_secreta"

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
def del_user(id) :
    cursor.execute(f"DELETE FROM `registros` WHERE id={id}")
    conn.commit()
    conn.close
    return redirect(url_for("home_crud"))
def update_user():
    pass
"""def del_user (nombre,email,contrasena):
    cursor.execute("DELETE FROM usuarios WHERE nombre=%s AND email=%s AND contrasena=%s",(nombre,email,contrasena))
    conn.commit()
    conn.close
"""
#-------------------------------------------aqui termian la funciones CRUD----------------------------------------------------------------
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
        flash ("usuario agregado")


    return redirect(url_for("home_crud"))

#luego de que se autentique el insert se lleva al home CRUD
@app.route("/home-crud")
def home_crud():
    cursor.execute("SELECT id, nombre, apellido, telefono,email,contrasena, genero FROM registros")
    usuarios = cursor.fetchall()
    return render_template("crud.html", usuarios=usuarios)

@app.route("/delete_confirm/<int:id>", methods=["GET","POST"])
def delete_confirm (id):
    cursor.execute(f"SELECT * FROM `registros` WHERE id={id}")
    usuario=cursor.fetchall()
    name = usuario[0][1]
    last_name = usuario[0][2]
    email = usuario [0][3]

    return render_template("delete-confirm.html", user_name=name, user_lastname=last_name, user_email=email)




@app.route("/opc-crud", methods=["POST"])
def opc_crud() :
    but = request.form["but"]
    id = request.form["id"]
    

    if but == "add":
        return redirect(url_for("formulario"))
    
    elif but == "del" :
        return redirect(url_for("delete_confirm", id=id))



if __name__ == "__main__":
    app.run(debug=True)

