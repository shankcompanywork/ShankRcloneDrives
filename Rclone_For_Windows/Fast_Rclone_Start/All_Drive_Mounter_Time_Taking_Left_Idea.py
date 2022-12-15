import subprocess
import os
import win32api
import random

# Always Put Slash at the end

# Executable Rclone File Path 
rclone_path="C:/ShankData/ShankRcloneDrives/Rclone_For_Windows/rclone_setup/rclone.exe"
# rclone_path="../rclone_setup/rclone.exe"

# All Drives Name
config_drive_name_arr = ["ShankPersonalData","ShankCompanyWork","Course_Google_Drive","ShankPractiseWork"]

# Rclone Config Base Path
rclone_config_base_path = "C:/ShankData/ShankRcloneDrives/Rclone_For_Windows/rclone_config/"

# Destination Rclone Config Path
orignal_rclone_config_path = "C:/ShankData/ShankRcloneDrives/Rclone_For_Windows/Fast_Rclone_Start/"

new_file_name = "main_content.conf"

main_arr = []

drives = win32api.GetLogicalDriveStrings()
drives = [i.replace(":\\","") for i in drives.split('\000')[:-1]]

capital_alpha_arr = [chr(i) for i in range(ord('A'), ord('Z')+1)]
print(capital_alpha_arr)

while len(main_arr) != len(config_drive_name_arr):
    each_letter = random.choice(capital_alpha_arr)
    if each_letter not in drives and each_letter not in main_arr:
        main_arr.append(each_letter)

print(main_arr)

def get_full_path_of_all_files(dest_location):
    dest_file_list = []
    for root, dirs, files in os.walk(dest_location):
        for file in files:
            dest_file_list.append(os.path.join(root,file))
    return dest_file_list


main_config_path = orignal_rclone_config_path+new_file_name

all_path = get_full_path_of_all_files(rclone_config_base_path)

main_content = ""
for each_path in all_path:
    content = open(each_path,'r')
    main_content += "\n"
    main_content += content.read()
    main_content += "\n"

f = open(main_config_path,"w+")
f.write(main_content)
f.close()

config_drive_name_arr = ["ShankPersonalData","ShankCompanyWork","Course_Google_Drive","ShankPractiseWork"]

for drive_letter,config_drive_name in zip(main_arr,config_drive_name_arr):
    print(drive_letter)
    print(config_drive_name)
    
    main_str = (f'{rclone_path} mount {config_drive_name}: {drive_letter}: --config="{main_config_path}" --drive-use-trash=false --vfs-cache-mode=full -o volname="{config_drive_name}"')

    # main_str = (f'{rclone_path} mount {config_drive_name}: \\server\{drive_letter} --config="{main_config_path}" --drive-use-trash=false --vfs-cache-mode=full')

    proc = subprocess.Popen(
        main_str, 
        shell=True,
        stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE
    )
