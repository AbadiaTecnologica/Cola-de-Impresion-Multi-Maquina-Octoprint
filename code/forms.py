from wtforms import Form, StringField,validators,SubmitField,DateField
from wtforms.fields.html5 import DateField
from flask_wtf import FlaskForm
from flask import flash
import baseDatos

class  AnadirForm(FlaskForm):
    id=StringField('id')
    nombre=StringField('nombre',[validators.InputRequired()])
    pedido=StringField('pedido',[validators.InputRequired(),validators.AnyOf(baseDatos.getColumna("Pedido","idPedido"))])
    boquilla=StringField('boquilla',[validators.InputRequired(),validators.AnyOf(baseDatos.getColumna("Boquilla","idBoquilla"))])
    rollo=StringField('rollo',[validators.InputRequired(),validators.AnyOf(baseDatos.getColumna("Rollo","idRollo"))])
    maquina=StringField('maquina',[validators.InputRequired(),validators.AnyOf(baseDatos.getColumna("Maquina","idMaquina"))])
    volumen=StringField('volumen',[validators.InputRequired()])
    fecha= DateField('fecha',[validators.InputRequired()])
    submit = SubmitField('Submit')




def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))