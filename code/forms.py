from wtforms import Form, StringField,validators,SubmitField,DateField
from flask_wtf import FlaskForm

class  AnadirForm(FlaskForm):
    id=StringField('id')
    pedido=StringField('pedido')
    boquilla=StringField('boquilla')
    rollo=StringField('rollo')
    maquina=StringField('maquina')
    volumen=StringField('volumen')
    fecha= DateField('fecha')
    submit = SubmitField('Submit')