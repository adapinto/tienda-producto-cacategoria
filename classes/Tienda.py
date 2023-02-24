from classes import DbMongo

class Tienda:
    
    def __init__(self,nombre,telefono):
        self.nombre = nombre
        self.telefono=telefono
        self.__collection= "tienda"
        
    def save(self,db):
        collection=db[self.__collection]
        collection.insert_one(self.__dict__)
        
        