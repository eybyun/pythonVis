import pymysql
from . import obj_process
from . import obj_call
from . import obj_return

dbName = "pythonDB"
tPro_drop = "DROP TABLE IF EXISTS PROCESS"
tPro_create = "CREATE TABLE IF NOT EXISTS PROCESS(process_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,frame TEXT,event TEXT );"
tCall_drop = "DROP TABLE IF EXISTS CALLS"
tCall_create = "CREATE TABLE IF NOT EXISTS CALLS(call_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,obj TEXT, path TEXT,line INT,className TEXT,funcName TEXT,process_id INT,FOREIGN KEY (process_id) REFERENCES PROCESS (process_id));"
tRe_drop = "DROP TABLE IF EXISTS RETURNS"
tRe_create = "CREATE TABLE IF NOT EXISTS RETURNS(return_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,className TEXT,funcName TEXT,process_id INT,FOREIGN KEY (process_id) REFERENCES PROCESS (process_id));"
db = pymysql.connect(host="localhost", user="root", passwd="apmsetup", db="pythonDB", charset='utf8')
cur = db.cursor()

class DB:

    def __init__(self):
        cur.execute(tPro_drop)
        cur.execute(tPro_create)
        cur.execute(tCall_drop)
        cur.execute(tCall_create)
        cur.execute(tRe_drop)
        cur.execute(tRe_create)

    def inData(self, listData):
        for obj in listData:
            if isinstance(obj, obj_process.OBJ_Process):
                cur.execute("insert into Process values (0,'"+str(obj.frame)[1:-1].split()[3]+"','"+obj.event+"')")
            elif isinstance(obj, obj_call.OBJ_Calls):
                print("insert into Calls values (0,'"+obj.obj+"','"+obj.path+"',"+obj.line+",'"+obj.className+"','"+obj.funcName+"', (SELECT process_id FROM process ORDER BY process_id DESC LIMIT 1))")
                cur.execute("insert into Calls values (0,'"+obj.obj+"','"+obj.path+"',"+obj.line+",'"+obj.className+"','"+obj.funcName+"', (SELECT process_id FROM process ORDER BY process_id DESC LIMIT 1))")
            elif isinstance(obj, obj_return.OBJ_Return):
                print("Return DB")

            #print(str(obj_pro.frame)[1:-1].split()[3])
            #print("Frame:: " , str(obj_pro.frame)[1:-1].split()[3], " Event:: ", obj_pro.event)
            #print("insert into Process values (0,'"+str(obj_pro.frame)[1:-1].split()[3]+"','"+obj_pro.event+"')")
            #cur.execute("insert into Returns values (0,'"+str(obj_pro.frame)[1:-1].split()[3]+"','"+obj_pro.event+"')")

#pyDB = DB();

#cur.execute("CREATE TABLE if not exists PROCESS()")