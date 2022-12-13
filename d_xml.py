import os
import gridfs
from conn_mongo import mongo_conn
from dotenv import load_dotenv

load_dotenv()
db = mongo_conn()
fs = gridfs.GridFS(db)   


f = open(os.getenv('PATH_FILES_DOWNLOAD'), "r")
files = []

while(True):
	#read next line
	line = f.readline()
	#if line is empty, you are done with all lines in the file
	if not line:
		break
	#you can access the line
	files.append(line.strip())    
f.close

files_not = []
for i in files:
    try:
        if len(i) < 44:
            filename = '/.*'+i+'.*/'
        else:
            filename = i

        print(filename)  
        data = db.fs.files.find_one({'filename':filename})
        my_id = data['_id']
        outputdata = fs.get(my_id).read()
        download_location = os.getenv('PATH_DOWNLOAD') + i + '.xml'
        output = open(download_location, 'wb')
        output.write(outputdata)
        print("Arquivos salvo com sucesso: ",i)
        output.close
    except Exception as e:
        files_not.append(i)
        print("Arquivo não localizado ou com erro: ", i)

for i in files_not:
    print(i)