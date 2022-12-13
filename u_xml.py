import os
import gridfs
from xml.dom import minidom
from dotenv import load_dotenv
from conn_mongo import mongo_conn

def search(origin):
    files = os.listdir(origin) 
    return files

def nameXml(file_origin):
    try:
        file = minidom.parse(file_origin)
        key = file.getElementsByTagName('chNFe')        

        if not key:
              key = file.getElementsByTagName('chCTe')

        name = key[0].firstChild.data
        return name
    except Exception as e:
        print("Error search key")

load_dotenv()
db = mongo_conn()
origin = os.getenv('PATH_ORIGIN')
destination = os.getenv('PATH_DESTINATION')

# pega arquivos do diretorio que serão importados
files= search(origin)

if len(files) == 0:
    print("sem arquivos a serem processados")
else:    
    for i in files:
        
        file_origin = origin + str(i)     #local + nome do arquivo
    
        file_data = open(file_origin, "rb")
        data = file_data.read()
       
        file_name = nameXml(file_origin)          #nome do arquivo (chave do xml)

        fs = gridfs.GridFS(db)   
        fs.put(data, filename = file_name)
                  
        print("\nupload completo file: " + i)


