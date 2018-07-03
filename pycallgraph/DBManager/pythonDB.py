import pymysql

dbName = "pythonDB"
tPro_create = "CREATE TABLE IF NOT EXISTS PROCESS(process_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,frame TEXT,event TEXT );"
tCall_create = "CREATE TABLE IF NOT EXISTS CALLS(call_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,path TEXT,line INT,className TEXT,funcName TEXT,process_id INT,FOREIGN KEY (process_id) REFERENCES PROCESS (process_id));"
tRe_create = "CREATE TABLE IF NOT EXISTS RETURNS(return_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,className TEXT,funcName TEXT,process_id INT,FOREIGN KEY (process_id) REFERENCES PROCESS (process_id));"
db = pymysql.connect(host="localhost", user="root", passwd="apmsetup", db="pythonDB", charset='utf8')
cur = db.cursor()

class DB:

    def __init__(self):
        cur.execute(tPro_create)
        cur.execute(tCall_create)
        cur.execute(tRe_create)

    def inProcess(self, listProcess):
        cur.execute("insert")

#pyDB = DB();

#cur.execute("CREATE TABLE if not exists PROCESS()")