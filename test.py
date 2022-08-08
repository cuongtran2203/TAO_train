import os
import glob
import re
input_dir="/home/vdungx/Desktop/train_tao_cuongcv/lprnet/img_2/img/*.txt"
list_file=os.listdir('/home/vdungx/Desktop/train_tao_cuongcv/lprnet/img_2/img')
file_path= glob.glob(input_dir)
#print(file_path)
# for file_txt in glob.glob():
#     if ".txt" is in file_txt:
#         txt_path= input_dir+file_txt
#         with open()
with open('/home/vdungx/Desktop/train_tao_cuongcv/lprnet/specs/ocr.txt','r+') as f,open('/home/vdungx/Desktop/train_tao_cuongcv/lprnet/specs/ocr2.txt','a') as out:
    temps=f.readlines()
    #print(temps)
    f.seek(0)
    #print(temps[0])
    a=temps[0]
    p=[]
    
    #f.truncate()
    f.close()
    for i in range(len(a)):
        out.writelines(a[i])
       
    out.close()
   
# for file_txt in file_path:
#     file_name_txt="anno3.txt"
#     with open(file_txt,'r') as f,open(file_txt,'a') as out:
#         temp=f.readline()
#         print(temp)
#         if  "." in temp :
#             temp=re.sub("\.","",temp)
#         if "-" in temp:
#             temp=re.sub("\-","",temp)
#         if " " in temp:
#             temp=re.sub("\ ","",temp)
#         out.writelines(temp)
#         out.close()