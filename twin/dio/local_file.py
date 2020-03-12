from ..  router import director_view
from PySide2.QtWidgets import QFileDialog
#from subprocess import Popen,PIPE
import subprocess
import _thread
import asyncio
import functools
import sys
import chardet
import os
import io
import locale

#from PySide2.QtCore import QProcess,QObject
#import invoke
#local = invoke.Context()


@director_view('read_file')
def read_file(path):
    f=  open(path,'r',encoding='utf-8') 
    return f.read()

@director_view('file_dialog')
def file_dialog():
    path = QFileDialog.getOpenFileName()
    return path[0]
    #path = QFileDialog.getExistingDirectory()
    #return path
@director_view("save_file")
def save_file(path,text):
    with open(path,'w',encoding='utf-8') as f:
        f.write(text)

@director_view('run_code')
def run_code(code):
    print('开始运行:%s'%code)
    #loop = asyncio.get_event_loop()
   
    _thread.start_new_thread(_run_code,(code,))

#class Bba(QObject):
    #def write(self,msg):
        #print(msg)

#bcd = Bba()

def _run_code(code):
    #os.system(code)
    #proc = subprocess.Popen(code, stdout=subprocess.PIPE,shell=True)
    #for line in io.TextIOWrapper(proc.stdout, encoding="utf-8"):
        #print(line)
    #local.run(code)
    #QProcess.execute(code)
    #process = QProcess()
    #process.setProcessChannelMode(QProcess.MergedChannels)
    ##bb.readyRead.connect(bcd.write)
    #process.start(code)
    #while process.waitForReadyRead():
        #print(process.readAll() )
    
    
    #resp = os.popen(code)
    #print(resp.read())

    with subprocess.Popen(code,stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True,bufsize=1) as p:
        output, errors = p.communicate()
        if output:
            for out in output.splitlines():
                print(out.decode(locale.getpreferredencoding()))
                #print(decode(output))
        if errors:
            for out in errors.splitlines():
                print(out.decode(locale.getpreferredencoding()))
                #print(decode(output))
        #if output:
            #print(decode(output))
        #if errors:
            #print(decode(errors))
        #lines = output.decode('utf-8').splitlines()
        #print(output.decode(locale.getpreferredencoding()))
    
    #asyncio.set_event_loop(loop)
    #p = subprocess.Popen(code,shell=True,stdout=subprocess.PIPE,bufsize=1)
    ##returncode = p.poll()
    ##while returncode is not None:
    #std = p.stdout.read()
    #std = std.strip()
    #if std:
        #print(decode(std) )
    #if p.stderr:
        #err = p.stderr.read()
        #err = err.strip()
        #if err:
            #print(decode( err) )
            ##returncode = p.poll()
        
    
    #for line in iter(p.stdout.readline, b''):
        #text = line.rstrip().decode(locale.getdefaultlocale()[1])
        #print(text)
        ##loop.create_task(print(line.decode('utf-8')) )
        ##loop.call_soon_threadsafe(functools.partial(print, line.decode('utf-8')))
    #p.stdout.close()
    #p.wait()
    #loop.call_soon_threadsafe(functools.partial(print, '运行结束'))
    print('运行结束')
    #loop.create_task(print('运行结束'))
def decode(msg):
    rt = chardet.detect(msg)
    return msg.decode( rt.get('encoding') )