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
for file_txt in file_path:
    file_name_txt="anno3.txt"
    with open(file_txt,'r+') as f,open(file_txt,'a') as out:
        temps=f.readlines()
        print(temps)
        f.seek(0)
        a=temps[1]
        print(temps)
        f.truncate()#delete all data in txt file
        f.close()
        out.write(a)
        out.close()
            