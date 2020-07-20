import uuid
import os
import shutil
import errno, os, stat, shutil

path = r'C:\Users\Akash\PycharmProjects\Translation_NLP\test'

def rename_obj(name):

    name = name.lower()
    uuidOne = str(uuid.uuid1())
    name = uuidOne + '.' + name.split('.')[-1]

    return name

def handleRemoveReadonly(func, path, exc):
  excvalue = exc[1]
  if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
      os.chmod(path, stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO) # 0777
      func(path)
  else:
      raise

print('path',path)
for root, folders, files in os.walk(path):
    if root == path:
        print('root',root)
        print('folders',folders)
        print('files',files)

        new_path = os.path.join(root,'subfolder')
        if os.path.exists(new_path) == False:
            os.mkdir(new_path)
        # else:
        #     shutil.rmtree(new_path, ignore_errors=False, onerror=handleRemoveReadonly)
        #     # os.remove(new_path)

        for file in files:
            old_file_name = os.path.join(root,file)

            file = str(uuid.uuid1()) + '.' + file.split('.')[-1]
            new_file_name = os.path.join(new_path, file)
            # os.rename(old_file_name,new_file_name)
            shutil.copy(old_file_name,new_file_name)
