import pymongo

from classes import Tienda, DbMongo, Categoriatienda, Producto
from dotenv import load_dotenv


def main():
    store, db =DbMongo.getDB()
    
    #tienda = Tienda("La Tienda 6","55555555")
    #tienda.save(db)
    
    #tienda.telefono="77777777"
    #tienda.update(db)
    
    #tienda.delete(db)
    
    #lista_tiendas=Tienda.get_list(db)
    #lista_tiendas[0].update(db)
    
    Tienda.delete_all(db)
    Categoriatienda.delete_all(db)
    
    Categoriatienda("Office").save(db)
    Categoriatienda("Music").save(db)
    Categoriatienda("Electronic").save(db)
    
    dictCategorias= Categoriatienda.get_dict(db)
    
    Producto("Cuaderno","20").save(db)
    Producto("Lapiz","10").save(db)
    
    tienda = Tienda("La Tiendita 8","99999999",dictCategorias["Office"])
    tienda.save(db)
    
    store.close()
    
if __name__=="__main__":
        load_dotenv()
        main()    
    