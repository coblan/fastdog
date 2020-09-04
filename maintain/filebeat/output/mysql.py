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
        self.mysql = pymysql.connect(
            host=host,
               port=int(port),
               user=user,
               passwd=pswd,
               db=db_name,
               charset='utf8' )
        self.hostName = socket.gethostname()
        super().__init__()
        #print('elk-log1')
    
    @property
    def connection(self):
        if not self.mysql.open:
            self.mysql.ping(reconnect=True)
        return self.mysql

    def send(self,lines):
        actions=[ ]
        ls =[]
        for line in lines:
            ls.append(
                [line.get('@timestamp'),line.get('level','NULL'),line.get('message',''),line.get('path',''),line.get('process',''),line.get('host',self.hostName)]
                ) 
            
        if ls: 
            with self.connection.cursor() as cursor:
                cursor.executemany("insert into act_log_generallog(createtime, level ,message,path,process,host) values (%s, %s,%s,%s,%s,%s)", ls )
                self.connection.commit()        

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
            with self.connection.cursor() as cursor:
                cursor.executemany("insert into act_log_backendoperation(createtime, model, content , createuser) values (%s,%s,%s,%s)", ls )
                self.connection.commit()       


