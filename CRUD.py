
from cgi import print_directory
import pymongo
from pymongo import MongoClient
import config


#Insertion of records into database


def insert_mongo(mongoData):
    mongoHost = config.mongoHost
    mongoPort = config.mongoPort
    #database= config.databasename
    #tablename=config.tname
   
    
    mongo_uri = "mongodb://"+str(mongoHost)+":"+str(mongoPort)+"/"
    
    client = MongoClient(mongo_uri)   
    print("Enter database name:")
    db_name=input()
    mongoDB = client[db_name]
    print("Enter table name")
    tb=input()
    table= mongoDB[tb]
    status = table.insert_one(config.item_2)
    print("Successfully inserted")



# Reading of records from database

def read_mongo(uniqID):
    mongoHost = config.mongoHost
    mongoPort = config.mongoPort
    #database= config.databasename
    #tablename=config.tname
    
    
    mongo_uri = "mongodb://"+str(mongoHost)+":"+str(mongoPort)+"/"
    
    client = MongoClient(mongo_uri)    
    print("Enter database name:")
    db_name=input()
    mongoDB = client[db_name]
    print("Enter table name")
    tb=input()

    table= mongoDB[tb]
    
    mongoData = table.find_one({"_id" : uniqID})
    print(mongoData)
    


#Creation of database

def create_database(db_name):
    mongoHost = config.mongoHost
    mongoPort = config.mongoPort
    mongo_uri = "mongodb://"+str(mongoHost)+":"+str(mongoPort)+"/"
    client = MongoClient(mongo_uri) 
    mongoDB = client[db_name]
        #mongoDB = client[database]
    print("Enter table name:")
    tablename=input()
    tb=mongoDB[tablename]
    tb.insert_one(config.item_1)
    print("Successfully created database")


#Deletion of database
def delete_database(db_name):
	mongoHost = config.mongoHost
	mongoPort = config.mongoPort
	mongo_uri = "mongodb://"+str(mongoHost)+":"+str(mongoPort)+"/"

	client = MongoClient(mongo_uri) 
	client.drop_database(db_name)


print("Available operations are \n1.Create \n2.Insert \n3.Read \n4.Delete")
print("Enter your option by their respective no")
opt=input()
if (opt=="1"):
    print("Enter the username:")
    username=input()
    print("Enter the password")
    password=input()
    if((config.mongoUser==username) and (config.mongoPass==password)):
        print("Enter database name")
        db_name=input()
        create_database(db_name)
        #create_database("Dmart")
        
    else:
        print("Enter valid username or password")
#if __name__ == "__main__":

elif(opt=="2"):
    print("Enter the username:")
    username=input()
    print("Enter the password")
    password=input() 
    if((config.mongoUser==username) and (config.mongoPass==password)):
        insert_mongo(config.item_2)
    else:
        print("Enter valid username or password")

elif(opt=="3"):
    print("Enter the username:")
    username=input()
    print("Enter the password")
    password=input()
    if((config.mongoUser==username) and (config.mongoPass==password)):
        print("Enter the id")
        id=input()
        read_mongo(id)
    else:
        print("Enter valid username or password")

elif(opt=="4"):
    print("Enter the username:")
    username=input()
    print("Enter the password")
    password=input()
    if((config.mongoUser==username) and (config.mongoPass==password)):
        print("Enter database name")
        ddname=input()
        delete_database(ddname)
    else:
        print("Enter valid username or password")




    





    
    


