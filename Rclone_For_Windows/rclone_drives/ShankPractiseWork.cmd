@echo on
"..\rclone_setup\rclone.exe" ^
mount ^
ShankPractiseWork: ^
\\server\ShankPractiseWork ^
--config="..\rclone_config\Shank_Personal_Google_Drive\rclone.conf" ^
--cache-dir="..\rclone_setup\RcloneCache" ^
--drive-use-trash=false ^
--vfs-cache-max-size=8G ^
--vfs-cache-max-age=10h ^
--union-min-free-space 1G ^
--bwlimit 8M ^
--vfs-cache-mode=full