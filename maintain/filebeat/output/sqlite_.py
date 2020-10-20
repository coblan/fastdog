import sqlite3
import logging
import socket
import datetime
import sys
import logging
general_log = logging.getLogger('general_log')
import json

class SqliteHander(logging.Handler):
    def __init__(self,db_path):
        self.db_path = db_path
        self.hostName = socket.gethostname()
        super().__init__()
        self.connect()
        #print('elk-log1')
    
    def connect(self):
        self.conn =  sqlite3.connect(self.db_path) 
    
    def executemany(self, sql,ls):
        self.connect()
        cursor = self.conn.cursor()
        cursor.executemany(sql,ls)
        
    def send(self,lines):
        actions=[ ]
        ls =[]
        for line in lines:
            ls.append(
                [line.get('@timestamp'),line.get('level','NULL'),line.get('message',''),line.get('path',''),line.get('process',''),line.get('host',self.hostName)]
                ) 
            
        if ls: 
            self.executemany("insert into act_log_generallog(createtime, level ,message,path,process,host) values (?, ?,?,?,?,?)", ls )
            self.conn.commit()    
            
            
class TableSqliteHander(SqliteHander):
    def send(self,lines):
        actions=[ ]
        ls =[]
        for line in lines:
            message = line.get('message','{}')
            msg_dc = json.loads(message)
            model = msg_dc.pop('model','')
            user = msg_dc.pop('user','')
            ls.append(
                [line.get('@timestamp'),model,json.dumps(msg_dc,ensure_ascii=False),user]
                ) 
            
        if ls: 
            #with self.connection.cursor() as cursor:
            self.executemany("insert into act_log_backendoperation(createtime, model, content , createuser) values (?,?,?,?)", ls )
            self.conn.commit()   