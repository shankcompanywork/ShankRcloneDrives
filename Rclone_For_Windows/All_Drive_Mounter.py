# Just "_union" in the end to the union drive for the giving more time for the mounting purpose

import subprocess
import time
import os
import win32api

main_path="C:/ShankData/ShankRcloneDrives/Rclone_For_Windows/rclone_drives"
union_drive_mounting_time=18
normal_drive_mounting_time=5

def dest_location(dest_location):
    dest_file_list = []
    for root, dirs, files in os.walk(dest_location):
        for file in files:
            dest_file_list.append(file)
    return dest_file_list

file_name_arr = dest_location(main_path)

print(file_name_arr)


for file_name in file_name_arr:

    proc = subprocess.Popen(
        f'cd {main_path} & {file_name}', 
        shell=True, 
        stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE
    )

    if file_name.split(".")[0].split("_")[-1].lower() == "union":
        print("================ Union Drive Detected ================")
        print(f"Union Drive Sleep Time Is Set To {union_drive_mounting_time} seconds")
        time.sleep(union_drive_mounting_time)
    else:
        print("================ Normal Drive Detected ================")
        print(f"Normal Drive Sleep Time Is Set To {normal_drive_mounting_time} seconds")
        time.sleep(normal_drive_mounting_time)



# Just for checkin ghow many drives are there with drives letter in python
drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
print(drives)