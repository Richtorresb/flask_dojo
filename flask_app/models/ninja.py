from flask_app.config.mysqlconnection import connectToMySQL

class Ninjas:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM esquema_dojos_y_ninjas.ninjas;"
        results = connectToMySQL('esquema_dojos_y_ninjas').query_db(query)
        usuarios = []
        for usuario in results:
            usuarios.append( cls(usuario) )
        return usuarios
    
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO esquema_dojos_y_ninjas.ninjas ( first_name, last_name, age, created_at, updated_at, dojo_id ) VALUES ( %(first_name)s, %(last_name)s,%(age)s, NOW() , NOW(), %(dojo_id)s );"

        return connectToMySQL('esquema_dojos_y_ninjas').query_db( query, data )

    @classmethod
    def seleccionar(cls, data ):
        query = "SELECT * FROM esquema_dojos_y_ninjas.ninjas JOIN esquema_dojos_y_ninjas.dojos ON ninjas.dojo_id = dojos.id WHERE ninjas.dojo_id = %(id)s;"
        results = connectToMySQL('esquema_dojos_y_ninjas').query_db(query, data)
        usuarios = []
        for usuario in results:
            usuarios.append( cls(usuario) )
        return usuarios