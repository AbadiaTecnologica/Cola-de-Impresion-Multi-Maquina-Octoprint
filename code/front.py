from flask import Flask,render_template
import baseDatos as base
app = Flask(__name__,static_url_path='/static')
base.imprimeTabla("Trabajo")
@app.route("/")
def hello():
    return render_template('index.html',lista=base.listaTabla("Trabajo"))


app.run(host='0.0.0.0')