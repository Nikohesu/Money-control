from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def formulario():
    return render_template("formulario.html")

@app.route("/procesar_formulario", methods=["POST"])
def procesar_formulario():
    
    nombre = request.form['nombre']  
    email = request.form['email']
    contrasena = request.form['contrasena']

    return f"¡hola {nombre}¡ tus datos han sido prosesados correctamente. "
  
if __name__=="__main__":
    app.run(debug=True)