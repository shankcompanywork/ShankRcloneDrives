@echo on
"..\rclone_setup\rclone.exe" ^
mount ^
Course_Google_Drive: ^
\\server\CourseGoogleDrive ^
--config="..\rclone_config\Course_Google_Drive\rclone.conf" ^
--cache-dir="..\rclone_setup\RcloneCache" ^
--drive-use-trash=false ^
--vfs-cache-max-size=8G ^
--vfs-cache-max-age=10h ^
--union-min-free-space 1G ^
--bwlimit 8M ^
--vfs-cache-mode=full