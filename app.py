import pymongo

from classes import Tienda
from dotenv import load_dotenv


def main():
    
    tienda = Tienda("La Tienda 3","22222222")
    tienda.save()
    
if __name__=="__main__":
        load_dotenv()
        main()    
    