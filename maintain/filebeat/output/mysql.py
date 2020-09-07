import pymysql

import logging
import socket
import datetime
import sys
import logging
general_log = logging.getLogger('general_log')
import json

class MysqlHander(logging.Handler):
    def __init__(self,host,port, user,pswd,db_name):
        self.host =host
        self.port = port
        self.user = user
        self.pswd = pswd
        self.db_name = db_name
        
        self.hostName = socket.gethostname()
        super().__init__()
        self.connect()
        #print('elk-log1')
    
    def connect(self):
        self.conn = pymysql.connect(
            host= self.host,
               port=int(self.port),
               user=self.user,
               passwd=self.pswd,
               db=self.db_name,
               charset='utf8' )        
    #@property
    #def connection(self):
        #general_log.debug('read mysql connection property')
        #if not self.mysql.open:
            #general_log.debug('into mysql reconnect')
            #self.mysql.ping(reconnect=True)
        #return self.mysql
    
    def executemany(self, sql,ls):
        try:
            cursor = self.conn.cursor()
            cursor.executemany(sql,ls)
        except pymysql.OperationalError:
            self.connect()
            cursor = self.conn.cursor()
            cursor.executemany(sql,ls)
        return cursor    
    
    def send(self,lines):
        actions=[ ]
        ls =[]
        for line in lines:
            ls.append(
                [line.get('@timestamp'),line.get('level','NULL'),line.get('message',''),line.get('path',''),line.get('process',''),line.get('host',self.hostName)]
                ) 
            
        if ls: 
            #with self.connection.cursor() as cursor:
            self.executemany("insert into act_log_generallog(createtime, level ,message,path,process,host) values (%s, %s,%s,%s,%s,%s)", ls )
            self.conn.commit()        

class TableMysqlHander(MysqlHander):
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
            self.executemany("insert into act_log_backendoperation(createtime, model, content , createuser) values (%s,%s,%s,%s)", ls )
            self.conn.commit()       


