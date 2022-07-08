from pymongo import MongoClient
import gridfs
connection=MongoClient("localhost",27017)
database=connection['Images']
fs=gridfs.GridFS(database)
file="/home/shivanisri/Downloads/img.png"
with open(file,'rb') as f:
    contents=f.read()
    fs.put(contents,filename="file")