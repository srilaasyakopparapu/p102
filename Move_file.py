import os
import shutil
from_dir="c:/pythonfiles/c102/assets"
to_dir="c:/myorganizer/images"
listoffiles=os.listdir(from_dir)
for filename in listoffiles:
    root,ext=os.path.splitext(filename)
    if ext ==" ":
        continue
    if ext in ['.txt','.doc','.docx','.pdf']:
        path1=from_dir+"/"+filename
        path2=to_dir+"/"+filename
        if os.path.exists(to_dir):
            print("moving...."+filename)
            shutil.move(path1,path2)
        else: 
            os.makedirs(to_dir)
            print("moving...."+filename)
            shutil.move(path1,path2)