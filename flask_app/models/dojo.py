
from flask_app.config.mysqlconnection import connectToMySQL

class Dojos:
    def __init__( self , data ):
        self.id = data['id']
        self.nombre = data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM esquema_dojos_y_ninjas.dojos;"
        results = connectToMySQL('esquema_dojos_y_ninjas').query_db(query)
        usuarios = []
        for usuario in results:
            usuarios.append( cls(usuario) )
        return usuarios
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO esquema_dojos_y_ninjas.dojos ( nombre, created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
        return connectToMySQL('esquema_dojos_y_ninjas').query_db( query, data )

    @classmethod
    def select_name(cls, data):
        query = "SELECT * FROM esquema_dojos_y_ninjas.dojos WHERE id = %(id)s"
        return connectToMySQL('esquema_dojos_y_ninjas').query_db(query, data)
