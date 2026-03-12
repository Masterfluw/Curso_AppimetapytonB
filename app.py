from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import http.client
import json

app = Flask(__name__)

# Configuracion de la base de datos SQLITE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///metapython.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy (app)

# modelo de la tabla llamado log (colocar nombre)
class log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha_y_hora = db.Column(db.DateTime, default=datetime.now)
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
                
                # agregar log en la BD
                agregar_mensajes_log(json.dumps(messages))
    
                if tipo == "interactive":
                    tipo_interactivo=messages["interactive"]["type"]
                    
                    if tipo_interactivo == "button_reply":
                        text = messages ["interactive"]["button_reply"]["id"]
                        numero = messages["from"]
                        
                        enviar_mensajes_whatsapp(text,numero)
                    
                if "text" in messages:
                    text = messages["text"]["body"]
                    numero = messages["from"]
            
                    enviar_mensajes_whatsapp(text,numero)
                    
                    # agregar log en la BD
                    agregar_mensajes_log(json.dumps(messages))
                    
        return jsonify({'messaje':'EVENT_RECEIVED'})
    except Exception as e:
        return jsonify({'messaje':'EVENT_RECEIVED'})
    
    def enviar_mensajes_whatsapp(texto, number):
        texto = texto.lower()
        
        if "hola" in texto:
            data={
                "messaging_product" : "whatsapp", 
                "recipient_type" : "individual",
                "to": number,
                "type": "text",
                "text": {
                    "preview_url": false, 
                    "body": "Hola ¿Como estas? Bienvenido"
                }
            }
        elif "1" in texto:
            data={
                "messaging_product" : "whatsapp", 
                "recipient_type" : "individual",
                "to": number,
                "type": "text",
                "text": {
                    "preview_url": false, 
                    "body": "Hola te ayudo a buscar el equipo ideal"
                }
            }
        elif "2" in texto:
            data={
                "messaging_product" : "whatsapp", 
                "recipient_type" : "individual",
                "to": number,
                "type": "location",
                "location": {
                "latitude": "-12.067158831865067",
                "longitude": "-77.03377940839486",
                "name": " Estadio naacional de Lima",
                "Andress": " Lima Peru"
                }                   
            }
        elif "3" in texto:
            data={
                "messaging_product" : "whatsapp", 
                "recipient_type" : "individual",
                "to": number,
                "type": "document",
                "document": {
                "llink": "https://www.aquasystemperu.com/hidroneumaticos-serie-vav.html#&gid=1&pid=2",
                "caption": "-catalogo de la bomba sumergible"
                }                   
            }
        elif "4" in texto:
            data={
                "messaging_product" : "whatsapp", 
                "recipient_type" : "individual",
                "to": number,
                "type": "audio",
                "audio": {
                "link": "https://filesamples.com/samples/audio/mp3samples1.mp3"
            }                   
            }
        elif "5" in texto:
            data={
                "messaging_product" : "whatsapp", 
                "to": number,
                "text": {
                    "preview_url" : True,
                    "body": "introduccion al mundo de las bombas para agua¡ https://www.aquasystemperu.com/index.html"
            }                   
            }
        elif "6" in texto:
            data={
                "messaging_product" : "whatsapp", 
                "recipient_type" : "individual",
                "to": number,
                "type": "text",
                "text": {
                "body": "enbreve me podre en contacto contigo"
                }                   
            }
        elif "7" in texto:
            data={
                "messaging_product" : "whatsapp", 
                "recipient_type" : "individual",
                "to": number,
                "type": "text",
                "text": {
                "preview_url":False,
                "body": "Horario de atencion : Lunes a sabado \n Horario 9:00 a 5:00 pm."
            }                   
            }
        elif "0" in texto:
            data={
                "messaging_product" : "whatsapp", 
                "recipient_type" : "individual",
                "to": number,
                "type": "text",
                "text": {
                "preview_url": False, 
                "body": "Hola,Ingresa un numero para mas informacion \n \n 1. Informacion del curso \n 2. Ubicacion del local \n 3. enviar temario en pdf \n 4. Audio explicando curso \n 5. Video de introduccion. \n 6. Hablar con fluter \n 7. Horario de atencion \n 0. Regresar al menu"
                }
            }
        elif "boton" in texto:
            data={
                "messaging_product" : "whatsapp", 
                "recipient_type" : "individual",
                "to" : number,
                "type" : "interactive",
                "interactive": {
                    "type":"button",
                    "body": {
                        "text": "confirma tu registro"
                    },
                    "footer": {
                        "text": "seleccione una opcion"
                    },
                    "action": {
                        "buttons":[
                            {
                                "type": "reply",
                                "reply": {
                                    "id": "btnsi",
                                    "title":"si"
                                }
                            },{
                                "type": "reply",
                                "reply": {
                                    "id": "btnno",
                                    "title":"No"
                                }
                            },{
                                "type": "reply",
                                "reply": {
                                    "id": "btntalvez",
                                    "title":"Tal Vez"
                                }
                            }
                        ]
                    }
                }
            } 
        elif "btnsi" in texto:
            data={
                "messaging_product" : "whatsapp", 
                "recipient_type" : "individual",
                "to" : number,
                "type" : "text",
                "text": {
                    "preview_url": False, 
                    "body": "Muchas gracias por aceptar."
                }
            }
        elif "btnno" in texto:
            data={
                "messaging_product" : "whatsapp", 
                "recipient_type" : "individual",
                "to" : number,
                "type" : "text",
                "text": {
                    "preview_url": False, 
                    "body": "Es una Lastima."
                }
            }
        elif "btntalvez" in texto:
            data={
                "messaging_product" : "whatsapp", 
                "recipient_type" : "individual",
                "to" : number,
                "type" : "text",
                "text": {
                    "preview_url": False, 
                    "body": "Estare a la espera."
                }
            }
        elif "lista" in texto:
            data={
                "messaging_product" : "whatsapp", 
                "to" : number,
                "type" : "interactive",
                "interactive": {
                    "type": "list", 
                    "body": {
                        "text": "Selecciona Alguna Opcion"
                    },
                    "footer": {
                        "text": "selecciones una de las opciones para poder ayudarte"
                    },
                    "action": {
                        "button": "Ver Opciones",
                        "sections": [
                            {
                                "title":"Compra y Venta",
                                "rows":[
                                    {
                                        "id": "btncompra", 
                                        "title":"Comprar",
                                        "description": " Compra los mejores articulos de tecnologia"
                                    },
                                    {
                                         "id": "btnvender", 
                                        "title":"vender",
                                        "description": " Vende lo que no usas"
                                    }
                                ]
                            },{
                                 "title":"Distribucion y Entrega",
                                "rows":[
                                    {
                                        "id": "btndireccion", 
                                        "title":"Local",
                                        "description": " puedes visitar nuestro local"
                                    },
                                    {
                                         "id": "btnentrega", 
                                        "title":"Entrega",
                                        "description": " La entrega se realizan todos los dias"
                                    }
                                ]
                            }
                        ]
                    }
                }
            }                 
        else:
            data = {
                "messaging_product" : "whatsapp", 
                "recipient_type" : "individual",
                "to" : number,
                "type" : "text",
                "text": {
                    "preview_url": False, 
                    "body": "Hola,Ingresa un numero para mas informacion \n \n 1. Informacion del curso \n 2. Ubicacion del local \n 3. enviar temario en pdf \n 4. Audio explicando curso \n 5. Video de introduccion. \n 6. Hablar con fluter \n 7. Horario de atencion \n 0. Regresar al menu"
                }
            }
        
            # Convertir en diccionario en formato JSON
            data = json.dumps(data)
            
            headers = {
                "Content-Type" : "application/jon",
                "Auhorization" : "Bearer EAAXHYImI1ZBEBQ2yw6RO2VR045mtGREyDK3qTlqZA72KGdwDf2zjZCTDGRoBztOyJkU6pGwpDxbiZC73fq4La6QZASuq7WVIEnEoO3Uj3QblqWyEVL2Pi7l5KbtiqLH2sLDo5QZCy7lHHCnZBR3p8W0is2PUZBsEp49YKHPgNdbyZBZBqQC0Bafy5zagDp6ywwNUfRk9bB3UTMyi2eHgipT3pZAImm3UbHReagRllELfBY4yEZABU9g3yQp4AI06L4OM5iHdFK07b1SiCfwnD9PZCc4RB"
            }
            
            connection = http.client.HTTPSConnection('graph.facebook.com')
            
            try:
                connection.request("POST", "/v22.0/1016468574875369/messages", data, headers)
                response = connection.getresponse()
                print(response.status, response.reason)
            except Exception as e:
                agregar_mensajes_log(json.dumps(e))
            finally:
                connection.close()  
            
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,debug=True)
