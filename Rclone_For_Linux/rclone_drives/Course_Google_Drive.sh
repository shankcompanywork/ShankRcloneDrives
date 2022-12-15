#!/bin/bash
mount_point_name="Course_Google_Drive"

rclone_mounting_location="$HOME/rclone/$mount_point_name"
mkdir -p $rclone_mounting_location

base_path="/$HOME/rclone"
mkdir -p $base_path

conf_file_path="../rclone_config/$mount_point_name/rclone.conf"
mkdir -p $rclone_mounting_location

rclone mount "$mount_point_name:" $rclone_mounting_location --config $conf_file_path --vfs-cache-mode full --allow-non-empty