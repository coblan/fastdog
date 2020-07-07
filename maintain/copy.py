import os
import zipfile
import invoke
import shutil
local = invoke.Context()
base_dir = os.path.dirname(__file__)

def git_copy(src,dst,temp_dir=base_dir):
    tmp_fl_path = os.path.join(base_dir,'git_copy_tmp.zip')
    with local.cd(src):
        local.run(r'git archive -o %(tmp_fl_path)s HEAD'%locals())
    
    with zipfile.ZipFile(tmp_fl_path, 'r') as zip_ref:
        zip_ref.extractall(dst)


def copy(src_root,target_root,filters=[]):
    #src_root = r'D:\work\H5\dist'
    #target_root = r'D:\work\Release\Live-Binary\H5\dist'

    for root, dirs, files in os.walk(src_root):
        rel_path = os.path.relpath(root, src_root)
        for fl in files:
            check_passed = True
            for item in filters:
                if not item.check_file(root,fl):
                    check_passed= False
                    break
            if check_passed:
                fl_path = os.path.join(root, fl)
                try:
                    os.makedirs(os.path.join(target_root, rel_path))
                except Exception:
                    pass
                target_path = os.path.join(target_root, rel_path, fl)
                shutil.copy(fl_path, target_path)
                print(target_path)
        
        # 去掉不要的dir
        left_dirs = []
        for d_item in dirs:
            check_passed = True
            for item in filters:
                if not item.check_dir(root,d_item):
                    check_passed= False
                    break
            if check_passed:
                left_dirs.append(d_item)
        dirs[:] = left_dirs #[d for d in dirs if left_dirs(d)]
        for d in dirs:
            target_dir_path = os.path.join(target_root, rel_path, d)
            if not os.path.exists(target_dir_path):
                os.makedirs(target_dir_path)
                print(target_dir_path)

class PythonFilter(object):
    def check_file(self,path,name):
        if name.endswith('.pyc'):
            return False
        if name.startswith('.'):
            return False
        else:
            return True
    
    def check_dir(self,path,name):
        if name == '__pycache__':
            return False
        return True

class JsFilter(object):
    def check_file(self,path,name):
        return True
    
    def check_dir(self,path,name):
        if name.startswith('.'):
            return False
        elif name in ['node_modules']:
            return False
        else:
            return True