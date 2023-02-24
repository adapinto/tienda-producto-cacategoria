import pymongo

class DbMongo:
        
        @staticmethod
        
        def getDB():
            user = 'Adimari'
            password = '99725478Adimari'
            cluster = 'poounahclase3.v7p4vxg.mongodb.net'
            query_string = 'retryWrites=true&w=majority'

         ## Connection String
            uri = "mongodb+srv://{0}:{1}@{2}/?{3}".format(
                  user
                , password
                , cluster
                , query_string
            )
        
            store=pymongo.MongoClient(uri)
            db=store['ejercicio-practica']
            
            return db