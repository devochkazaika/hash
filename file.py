import hashlib
import os

f = open("хеши_файлов.txt", 'w')


def hash_file(filename):
   h = hashlib.sha1()
   with open(filename,'rb') as file:
       chunk = 0
       while chunk != b'':
           chunk = file.read(1024)
           h.update(chunk)

   return h.hexdigest()


dir_list = os.listdir("./files_for_check_hash");

for i in dir_list:
    f.write(i + " -> " + hash_file("./files_for_check_hash/" +i) +"\n")
f.close()
#message = hash_file("f.txt")
#print(message)
