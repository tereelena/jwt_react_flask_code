"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/signup', methods=['POST', 'GET'])
def signup():
    if(request.method=='GET'):
        # esta varibale estoy consultando a la base de datos por todos los registros de la tabla user
        all_people= User.query.all()
        all_people= list(map(lambda x: x.serialize(), all_people))
        return jsonify(all_people), 200 
    else:
        #metodo post vamos a recibir informacion para agregar nuevo usuario
        datos=request.get_json()
         #validamos que  lo que se traiga en el request no este vacio o null
        if(datos is None):
            return("Debes enviar informacion para registro de usuarios")
        if("email" not in datos):
            return("Debes enviar email para registro de usuarios")
        if("password" not in datos):   
            return("Debes ingresar password para registro de usuarios")
        else:
         # aqui consulto que tiene la tabla user   
         one_people= User.query.filter_by(email=datos["email"]).first() 
        if one_people is None:  
        #si es nulo creamos un nuevo elemento
           nuevoUsuario= User(email=datos["email"],password=datos["password"], is_active=True)
           db.session.add(nuevoUsuario)
           db.session.commit()
           return ("Se ha registrado un nuevo Usuario")

@app.route("/login",methods=["POST"])
def login():
    datos= request.get_json()
    if(datos is None):
        return("Debes enviar informacion para Iniciar Sesion")
    if("email" not in datos):
        return("Debes enviar email para Iniciar Sesion")
    if("password" not in datos):   
        return("Debes enviar  password para Iniciar Sesion") 
    # estoy consultando si existe alguien con el email que mande en la api y consiga la primera coincidencia     
    one_people= User.query.filter_by(email=datos["email"]).first()    
    # si existe un nusuairo con el email recibidos y existe en la bd entramos
    if one_people:
        #validamos si la clave del usuario  de la base datos coincide con la clave enviada por postman entra 
        if (one_people.password==datos["password"]):
            #creamos una variable que establece que el token creado es por dos mininutos
            expira=datetime.timedelta(minutes=1)
            #creamos un token para el usuario validado, diciendo que encriptamos el email del usuario y daremos un tiempo valido del token.
            access_token=create_access_token(identity=one_people.email,expires_delta=expira)
            #creamos un objeto donde mostramos toda la informacion relevante: los datos del usuario
            #token creado en base al email del usuario
            #el tiempo que tiene de validez el token.
            response={
                "info_user":one_people.serialize(),
                "token":access_token,
                "expires":expira.total_seconds()
            }
            return jsonify(response)
        else:
            return("clave invalida") 
    else:       
         return("No existe usuario con ese email") 

@app.route("/privado", methods=["GET"])
@jwt_required()
def privado():
    if (request.method=="GET"):
        token=get_jwt_identity()
        return(token+"lalalala")         
    