from flask import Flask,render_template,request,redirect,url_for
import mysql.connector

app = Flask(__name__)

db_connfig = {
    "host" : "localhost",
    "user" : "Jhoan",
    "password" : "1217",
    "database" : "contactenos"
}

def add_contacto (nombre,correo,dipositivo,tipo,mensaje):
    conn= mysql.connector.connect(**db_connfig)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO mensajes (nombre,correo,dipositivo,tipo,mensaje) VALUES (%s,%s,%s)",(nombre,correo,dipositivo,tipo,mensaje))
    conn.commit()
    conn.close
def del_contacto (nombre,correo,dipositivo,tipo,mensaje):
    conn= mysql.connector.connect(**db_connfig)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM mensajes WHERE nombre=%s AND correo=%s AND dispositivo=%s AND tipo=%s AND mensaje=%s",(nombre,correo,dipositivo,tipo,mensaje))
    conn.commit()
    conn.close


@app.route("/")
def formulario ():
    return render_template("contactenos.html")

@app.route("/procesar_contactenos", methods=["POST"])
def procesar_formulario() :
    nombre = request.form["nombre"]
    correo = request.form["correo"]
    dipositivo = request.form["dipositivo"]
    tipo = request.form["tipo"]
    accion = request.form["but"]

    if accion=="Enviar":
        add_contacto(nombre,correo,dipositivo,tipo,mensaje)
    if accion=="eliminar":
        del_contacto(nombre,correo,dipositivo,tipo,mensaje)

    return redirect(url_for("cexito"))

@app.route("/cexito")
def exito():
    return render_template("cexito.html")

if __name__ == "__main__":
    app.run(debug=True)
