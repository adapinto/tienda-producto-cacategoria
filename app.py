import pymongo

from classes import Tienda, DbMongo


def main():
    
    db=DbMongo.getDB()
    
    tienda = Tienda("La Tienda 2","11111111")
    tienda.save(db)
    
    
    
if __name__=="__main__":
        main()    
    