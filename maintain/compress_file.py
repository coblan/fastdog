import os, tarfile

def make_targz(output_filename, source_dir,include_par_dir=True):
    """
    一次性打包目录为tar.gz
    :param output_filename: 压缩文件名
    :param source_dir: 需要打包的目录
    :return: bool
    """
    try:
        with tarfile.open(output_filename, "w:gz") as tar:
            if include_par_dir:
                tar.add(source_dir, arcname=os.path.basename(source_dir))
            else:
                for k in os.listdir(source_dir):
                    tar.add(os.path.join(source_dir,k) ,arcname=k)

        return True
    except Exception as e:
        print(e)
        return False
    
    
def untar(fname, dirs):
    """
    解压tar.gz文件
    :param fname: 压缩文件名
    :param dirs: 解压后的存放路径
    :return: bool
    """
    try:
        t = tarfile.open(fname)
        t.extractall(path = dirs)
        return True
    except Exception as e:
        print(e)
        return False