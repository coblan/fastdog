import os
import re

doc_dict = {}

def find_doc(src_root,dst_root,finder=[],tag_list=['default']):
   """{"doc":"test.md","tag":["default"]}
   hello world
   
   @finder: list 
   """
   all_tags = []
   
   for root, dirs, files in os.walk(src_root):
      rel_path = os.path.relpath(root, src_root)
      for fl in files:
         for item in finder:
            if item.check_file(root,fl):
               file_doc_list = item.parse(root,fl)
               for file_doc in file_doc_list:
                  doc = file_doc.get('doc')
                  file_doc['sort'] = file_doc.get('sort',100)
                  file_doc['tag'] = file_doc.get('tag',['default'])
                  all_tags.extend(file_doc['tag'])
                  if not doc:
                     raise UserWarning('必须要有文档路径，源文件:%s'%fl)
                  if doc not in doc_dict:
                     doc_dict[doc] = []
                  doc_dict[doc].append(file_doc)
               break
   
      # 去掉不要的dir
      left_dirs = []
      for d_item in dirs:
         check_passed = True
         for item in finder:
            if not item.check_dir(root,d_item):
               check_passed= False
               break
         if check_passed:
            left_dirs.append(d_item)
      dirs[:] = [d for d in dirs if d in left_dirs]
   
   print(set(all_tags))
   # 写doc文件
   for file_key,doc_list in doc_dict.items():
      file_path = os.path.join(dst_root,file_key)
      docs =[]
      for item in doc_list:
         for doc_tag in item.get('tag'):
            if doc_tag in tag_list:
               docs.append(item)
               break
      docs = sorted(docs,key= lambda x: x.get('sort',100) )
      content = ''.join([x.get('text') for x in docs])
      
      try:
         path = os.path.dirname(file_path)
         os.makedirs(path)
      except OSError:
         pass
      
      with open(file_path,'w',encoding='utf-8') as f:
         f.write(content)
         print('写文件 %s '%file_path)
   


class PythonDocFinder(object):

   def check_file(self,root,name):
      if name.endswith('.py'):
         return True
   
   def check_dir(self,root,name):
      return True
   
   def parse(self,root,name):
      fl = os.path.join(root,name)
      out =[]
      with open(fl,'r',encoding='utf-8') as f:
         in_the_doc_block =False
         for line in f.readlines():
            line = line.strip()
            if line.startswith(("'''",'"""')):
               if line[3:].strip().startswith('{'):
                  in_the_doc_block= True
                  head = eval(line[3:])
                  line_list = []
               elif in_the_doc_block:
                  in_the_doc_block =  False
                  head['text']='\n'.join(line_list)
                  out.append(head)
            elif in_the_doc_block:
               line_list.append(line)
          
      return out

class JSDocFinder(object):
   def check_file(self,root,name):
      if name.endswith(('.pack.js','.config.js')):
         return False
      if name.endswith(('.js','.vue')):
         return True
   
   def check_dir(self,root,name):
      return True
   
   def parse(self,root,name):
      fl = os.path.join(root,name)
      out =[]
      with open(fl,'r',encoding='utf-8') as f:
         in_the_doc_block =False
         for line in f.readlines():
            line = line.strip()
            if line.startswith("/*"):
               if line[2:].strip().startswith('{'):
                  in_the_doc_block= True
                  head = eval(line[2:])
                  line_list = []
            elif in_the_doc_block:
               if line.endswith('*/'):
                     in_the_doc_block =  False
                     head['text']='\n'.join(line_list)
                     out.append(head)
               else:
                  if line.startswith('*'):
                     line = line[2:]
                  line_list.append(line)
          
      return out
   