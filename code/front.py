from flask import Flask,render_template
import baseDatos as base
from forms import AnadirForm,flash_errors
from flask import request


app = Flask(__name__,static_url_path='/static')
base.imprimeTabla("Trabajo")


@app.route("/",methods=['GET', 'POST'])
def main():
    primeraForm=AnadirForm(request.form)
    # for elemento in primeraForm:
    #     print(elemento.data)
    print(primeraForm["nombre"].data)
    if(primeraForm.validate_on_submit()):

        base.nuevoTrabajo(primeraForm["pedido"].data, primeraForm["nombre"].data,primeraForm ["boquilla"].data, primeraForm["rollo"].data, primeraForm["maquina"].data, primeraForm["volumen"].data, primeraForm["fecha"].data)
    else:
        flash_errors(primeraForm)
    return render_template('index.html',form=primeraForm,lista=base.listaTabla("Trabajo"))




app.run(host='0.0.0.0')





