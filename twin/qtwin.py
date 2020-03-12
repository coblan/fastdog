import os
import sys
os.environ["path"] += os.path.join(os.getcwd(), "dll")
sys.path.append(os.path.join(os.getcwd(), "dll"))

from PySide2.QtWidgets import QApplication,QWidget,QMessageBox
from PySide2.QtCore import QUrl,QObject
from PySide2.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtWidgets import QApplication,QWidget
#from PyQt5.QtCore import QUrl,QObject
from router import director
import asyncio
from quamash import QEventLoop
#from asyncqt import QEventLoop
#from PyQt4.QtGui import QApplication,QWidget,QIcon
#from PyQt4.QtCore import QUrl,QObject,pyqtSlot, pyqtProperty,QSharedMemory
#from PyQt4.QtWebKit import QWebView
#import thread
#import server
#os.environ["REQUESTS_CA_BUNDLE"] = os.path.join(os.getcwd(), "cacert.pem")
#import common
base_dir = os.path.dirname( os.path.abspath( __file__) )

import qt_exapmple

def main():
    app = QApplication(sys.argv)
    #shared= QSharedMemory("wepush")
    #if shared.attach():
        #return 0
    #shared.create(1) 
    
    #sys.stdout=common.Mystd()
   
    
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    
    win = QWebEngineView() # QWebEngineView()
    director['root_win'] = win
    #thread.start_new_thread (server.start_server,(28289,))
    #win =QWebView()
    #win.setWindowIcon(QIcon( './html/wechat.ico'))
    win.setMinimumSize(1200,900)
    win.setWindowTitle('微信群发工具V1.0')
    url = 'file:///%s/test.html'%base_dir.replace('\\','/')
    win.load(QUrl( url ) )
    win.show()

    with loop:
        from server import start_server
        #loop.set_debug(True)
        loop.run_until_complete(start_server)
        #loop.create_task(send())
        #loop.create_task(start_server)
        
        loop.run_forever()

        
    #ss = app.exec_()
    #return sys.exit( ss)    

if __name__ =='__main__':
    main()
    
    
    