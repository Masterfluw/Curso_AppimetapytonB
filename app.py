from flask import Flask, request, jsonify, json, render_template
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

# Token de verificacion para la configuracion
TOKEN_ANDERCODE = "ANDERCODE"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        challenge = verificar_token(request)
        return challenge
    elif request.method == 'POST':
        reponse = recibir_mensajes(request)
        return reponse
    
def verificar_token(req):
    token = req.args.get('hub.verify.token')
    challenge = req.args.get('hub.challenge')
    
    if challenge and token == TOKEN_ANDERCODE:
        return challenge
    else:
        return jsonify({'error': 'token invalido'}), 401
  
def recibir_mensajes(req):
        
    try:
       req = request.get_json()
       entry = req['entry'][0] 
       changes = entry['changes'][0]
       value = changes['value']
       objeto_mensaje= value['messages']
       
       if objeto_mensaje:
           messages = objeto_mensaje
           if "type" in messages:
               tipo = messages ["type"]
               if tipo == "interactive":
                   return 0
               if "text" in messages:
                   text = messages["text"]["body"]
                   numero = messages["from"]       
               agregar_mensajes_log(json.dumps(text))
           agregar_mensajes_log(json.dumps(numero))
               
       return jsonify({'messaje':'EVENT_RECEIVED'})
    except Exception as e:
        return jsonify({'messaje':'EVENT_RECEIVED'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,debug=True)
