from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
 

app = Flask('__name__')

# Configuracion de la base de datos SQLITE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///metapython.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy (app)

# modelo de la tabla llamado log (colocar nombre)
class log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha_y_hora = db.Column(db.DateTime, default=datetime.utcnow)
    texto = db.Column(db.TEXT)
    
# Crear tabla si no existiera
with app.app_context():
    db.create_all()
    prueba1 = log(texto='mensaje prueba1')
    prueba2 = log(texto='mensaje prueba2')
    
    db.session.add(prueba1)
    db.session.add(prueba2)
    db.session.commit()
    
    # Funcion para ordenar los registros fecha y hora 
    def ordenar_por_fecha_y_hora(registros):
        return sorted(registros, key=lambda x: x.fecha_y_hora, reverse=True)

@app.route('/')
def index():
    
    # Obtener todos los registros en la base de datos
    registros = log.query.all()
    registros_ordenados = ordenar_por_fecha_y_hora(registros)
    return render_template('index.html', registros=registros)

mensajes_log = []

# Funcion para agregar mensajes y guardar en la base de datos
def agregar_mensajes_log(texto):
    mensajes_log.append(texto)
 
    # Guardar el mensaje en la base de datos
    nuevo_registro = log(texto)
    db.session.add(nuevo_registro)
    db.session.commit()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,debug=True)
