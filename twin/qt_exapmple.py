from PySide2.QtWidgets import QMessageBox
from PySide2.QtCore import QObject,Signal
from .router import director_view,director,worker
import chardet

class Mystd(QObject): 
    msg_singal = Signal(str)
    def __init__(self,):
        super().__init__()
        self.msg_singal.connect(self.on_write)
        
    def write(self, output_stream):
        self.msg_singal.emit(output_stream)
        #if output_stream != '\n':
        #worker.call('log',{'msg':output_stream})
        #back_log.info(output_stream) 
    def on_write(self,output_stream):
        #if isinstance(output_stream,str):
            #output_str = output_stream
        #else:
            #encode = chardet.detect(output_stream).get('encode')
            #output_str = output_stream.decode(encode)
        worker.call('log',{'msg':output_stream})
    
@director_view('alert')
def alert(msg):
    #director.get('root_win').message(msg)
    QMessageBox.information(None,'提示',msg,QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)

    