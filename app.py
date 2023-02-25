import pymongo

from classes import Tienda, DbMongo
from dotenv import load_dotenv


def main():
    store, db =DbMongo.getDB()
    
    tienda = Tienda("La Tienda 6","55555555")
    tienda.save(db)
    
    tienda.telefono="77777777"
    tienda.update(db)
    
    #tienda.delete(db)
    
    #lista_tiendas=Tienda.get_list(db)
    #lista_tiendas[0].update(db)
    
    store.close()
    
if __name__=="__main__":
        load_dotenv()
        main()    
    