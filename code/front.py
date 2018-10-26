from flask import Flask,render_template
import baseDatos as base
from forms import AnadirForm


app = Flask(__name__,static_url_path='/static')
base.imprimeTabla("Trabajo")


@app.route("/",methods=['GET', 'POST'])
def main():
    primeraForm=AnadirForm()
    for elemento in primeraForm:
        print(elemento.name)
    return render_template('index.html',form=primeraForm,lista=base.listaTabla("Trabajo"))




app.run(host='0.0.0.0')