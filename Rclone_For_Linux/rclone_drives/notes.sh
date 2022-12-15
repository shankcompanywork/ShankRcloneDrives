#!/bin/bash
mount_point_name="sharmashankfabmain"
user_name="$(whoami)"
conf_file_path="../rclone_config/$mount_point_name/rclone.conf"
base_path="/home/$user_name/Documents/rclone"
mkdir -p $base_path
rclone_mounting_location="~/$mount_point_name/"
mkdir -p $rclone_mounting_location

rclone mount mygoogledrive: 
rclone mount "$mount_point_name:" $rclone_mounting_location --config $conf_file_path


# Rclone Drive name and the folder name in the rclone must be same
mount_point_name="sharmashankfabmain"
rclone_mounting_location="$HOME/$mount_point_name"
conf_file_path="../rclone_config/$mount_point_name/rclone.conf"
mkdir -p $rclone_mounting_location
rclone mount "$mount_point_name:" $rclone_mounting_location --config $conf_file_path --vfs-cache-mode full 