"""
FTP Util
"""
 
# !/usr/bin/python3
# coding: utf-8
import ftplib
import os
import socket
import traceback
 
 
class FTP(object):
    """
    connect to FTP server, download or upload file, disconnect
    """
    host = '127.0.0.1'
    port = 21
    user = 'fred'
    pwd = 'fish'
 
    client = None
 
    def __init__(self, host, port, user='', pwd='',encoding='utf-8',debug_level=2):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        
        self.encoding= encoding
        self.debug_level = debug_level
        self.client = None
 
    def connect(self):
        """
        connect by ftp server
        :return:
        """
        client = ftplib.FTP()
        client.connect(self.host, self.port, timeout=30)
        client.encoding = self.encoding
        client.login(self.user, self.pwd)
        client.set_debuglevel( self.debug_level )
        socket.setdefaulttimeout(1200)
 
        self.client = client
 
    def quit(self):
        """
        :return:
        """
        if not self.client:
            self.client.quit()
 
    def isdir(self, remote_path):
        """
        remote path is file or folder
        :param remote_path: remote path
        :return:
        """
        try:
            self.client.cwd(ftp_encode(remote_path))
            self.client.cwd('..')
            return True
        except:
            return False
 
    def listdir(self, remote_dir):
        """
        list remote file paths by ftp server
        :param remote_dir: remote folder path
        :return:
        """
        return self.client.nlst(remote_dir)
        #paths = []
        #if not self.isdir(remote_dir):
            #paths.append(remote_dir)
            #return paths
 
        #remote_paths = self.client.nlst(remote_dir) #ftp_encode(remote_dir))
        ##remote_paths = [ftp_decode(remote_path) for remote_path in remote_paths]
 
        #for remote_path in remote_paths:
            #if self.isdir(remote_path):
                #paths2 = self.listdir(remote_path)
                #if paths2:
                    #paths.extend(paths2)
            #else:
                #paths.append(remote_path)
        #return paths
 
    def mkdir(self, remote_dir):
        self.client.mkd(ftp_encode(remote_dir))
 
    def remove(self, remote_path):
        """
        delete remote file in ftp server
        :param remote_path: remote file path
        :return:
        """
        self.client.delete(ftp_encode(remote_path))
 
    def download(self, remote_path, local_dir):
        """
        download file from ftp server
        :param remote_path: remote file path
        :param local_dir: local folder path
        :return:
        """
        if not os.path.exists(local_dir):
            os.makedirs(local_dir)
 
        remote_name = os.path.basename(remote_path)
        local_path = os.path.join(local_dir, remote_name)
 
        with open(local_path, 'wb') as local_file:
            self.client.retrbinary('RETR %s' % ftp_encode(remote_path), local_file.write, 1024)
 
    def upload(self, local_path, remote_dir=''):
        """
        upload file to ftp server
        :param local_path: local file path
        :param remote_dir: remote folder path
        :return:
        """
        if not os.path.isfile(local_path):
            raise FileNotFoundError('File %s is not found' % local_path)
 
        if not self.isdir(remote_dir):
            self.mkdir(remote_dir)
 
        local_name = os.path.basename(local_path)
        remote_path = os.path.join(remote_dir, local_name)
 
        with open(local_path, 'rb') as local_file:
            self.client.storbinary('STOR %s' % ftp_encode(remote_path), local_file, 1024)
 
 
def ftp_encode(remote_path):
    """
    convert local variable to remote path
    :param remote_path: 
    :return: 
    """
    return remote_path.encode('utf-8').decode('latin-1')
 
 
def ftp_decode(remote_path):
    """
    convert remote path to local variable
    :param remote_path: 
    :return: 
    """
    return remote_path.encode('latin-1').decode('utf-8')
 
 
if __name__ == '__main__':
    ftp = None
    try:
        ftp = FTP('127.0.0.1', 21, 'admin', '123456')
        ftp.connect()
        rps = ftp.listdir('/相对路径/名称有中文/')
        for rp in rps:
            ftp.download(rp, 'E:/本地路径/名称有中文/')
    except:
        traceback.print_exc()
    finally:
        if ftp:
            ftp.quit()
