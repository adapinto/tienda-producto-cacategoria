from classes.DbMongo import DbMongo


class Producto:
    
    def __init__(self, nombre,cantidad,id=""):
        self.nombre=nombre
        self.cantidad=cantidad
        self.__id=id
        self.__collection="categoria_tienda"
        
    def save(self, db):
        collection = db[self.__collection]
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
        collection = db["producto"]
        productos = collection.find()

        list_producto = []
        for e in productos:
            temp_producto = Producto(
                e["nombre"]
                , e["cantidad"]
                , e["_id"] 
            )

            list_producto.append(temp_producto)
        return list_producto
    
    @staticmethod
    def get_dict(db):
        collection = db["producto"]
        productos = collection.find()

        dict_producto= {}
        for e in productos:
            dict_producto[e["producto"]] = e["_id"] 

        return dict_producto

    @staticmethod
    def delete_all(db):
        lista_e = Producto.get_list(db)
        for e in lista_e:
            e.delete(db)