from classes.DbMongo import DbMongo


class Categoriatienda:
    
    def __init__(self, categoria, id=""):
        self.categoria=categoria
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
        collection = db["categoria_tienda"]
        tipos = collection.find()

        list_categoria_tienda = []
        for e in tipos:
            temp_categoria = Categoriatienda(
                e["categoria"]
                , e["_id"] 
            )

            list_categoria_tienda.append(temp_categoria)
        return list_categoria_tienda
    
    @staticmethod
    def get_dict(db):
        collection = db["categoria_tienda"]
        categorias = collection.find()

        dict_categoria_tienda = {}
        for e in categorias:
            dict_categoria_tienda[e["categoria"]] = e["_id"] 

        return dict_categoria_tienda

    @staticmethod
    def delete_all(db):
        lista_e = Categoriatienda.get_list(db)
        for e in lista_e:
            e.delete(db)
        