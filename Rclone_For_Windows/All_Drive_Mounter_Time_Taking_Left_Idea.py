# Just "_union" in the end to the union drive for the giving more time for the mounting purpose

import subprocess
import time
import os
import win32api

main_path="C:/ShankData/ShankRcloneDrives/rclone_drives/"
union_drive_mounting_time=14
normal_drive_mounting_time=3

def dest_location(dest_location):
    dest_file_list = []
    for root, dirs, files in os.walk(dest_location):
        for file in files:
            dest_file_list.append(file)
    return dest_file_list

file_name_arr = dest_location(main_path)

print(file_name_arr)


# for file_name in file_name_arr:

#     proc = subprocess.Popen(
#         f'cd {main_path} & {file_name}', 
#         shell=True, 
#         stdin=subprocess.PIPE, 
#         stdout=subprocess.PIPE
#     )

#     if file_name.split(".")[0].split("_")[-1].lower() == "union":
#         print("================ Union Drive Detected ================")
#         print(f"Union Drive Sleep Time Is Set To {union_drive_mounting_time} seconds")
#         time.sleep(union_drive_mounting_time)
#     else:
#         print("================ Noral Drive Detected ================")
#         print(f"Union Drive Sleep Time Is Set To {normal_drive_mounting_time} seconds")
#         time.sleep(normal_drive_mounting_time)



# Just for checkin ghow many drives are there with drives letter in python
main_arr = []

drives = win32api.GetLogicalDriveStrings()
drives = [i.replace(":\\","") for i in drives.split('\000')[:-1]]

for i in range(1,len(file_name_arr)+1):
    print(i)

capital_alpha_arr = [chr(i) for i in range(ord('A'), ord('Z')+1)]
print(capital_alpha_arr)

import random

while len(main_arr) != len(file_name_arr):
    each_letter = random.choice(capital_alpha_arr)
    if each_letter not in drives:
        main_arr.append(each_letter)

print(main_arr)


for drive_letter in main_arr:

    proc = subprocess.Popen(
        f'cd {main_path} & "../rclone_setup/rclone.exe" mount ShankPersonalData: {drive_letter} --config="../rclone_config/Shank_Personal_Google_Drive/rclone.conf" --drive-use-trash=false --vfs-cache-mode=full', 
        shell=True,
        stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE
    )

