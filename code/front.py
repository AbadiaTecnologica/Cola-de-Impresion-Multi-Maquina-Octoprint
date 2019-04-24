from flask import Flask,render_template
import baseDatos as base
from forms import AnadirForm,flash_errors
from flask import request
from werkzeug.utils import secure_filename


app = Flask(__name__,static_url_path='/static')
base.imprimeTabla("Trabajo")


@app.route("/",methods=['GET', 'POST'])
def main():
    primeraForm=AnadirForm(request.form)


    if(primeraForm.validate_on_submit()):
        filename = secure_filename(primeraForm.file.data.filename)
        primeraForm.file.data.save('uploads/' + filename)
        base.nuevoTrabajo(primeraForm["pedido"].data, primeraForm["nombre"].data,primeraForm ["boquilla"].data, primeraForm["rollo"].data, primeraForm["maquina"].data, primeraForm["volumen"].data, primeraForm["fecha"].data)
    else:
        flash_errors(primeraForm)
    return render_template('index.html',form=primeraForm,lista=base.listaTabla("Trabajo"),function4changing=function4changing)

def function4changing():
    print("B")




app.jinja_env.globals.update(function4changing=function4changing)




app.run(host='0.0.0.0')





