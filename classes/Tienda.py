from classes.DbMongo import DbMongo

class Tienda:
    
    def __init__(self,nombre,telefono,id=""):
        self.nombre = nombre
        self.telefono=telefono
        self.__id=id
        self.__collection= "tienda"
        
    def save(self,db):
        #store, db=DbMongo.getDB()
        collection=db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id =  result.inserted_id
        
    def update(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        objStore = { '$set' : self.__dict__ }
        collection.update_one( filterToUse , objStore )

    def delete(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        collection.delete_one( filterToUse )
    
    @staticmethod
    def get_list(db):
        collection = db["tienda"]
        tiendas = collection.find()

        list_tiendas = []
        for e in tiendas:
            temp_tienda = Tienda(
                e["nombre"]
                , e["telefono"]
                , e["_id"] 
            )

            list_tiendas.append(temp_tienda)
        return list_tiendas
        