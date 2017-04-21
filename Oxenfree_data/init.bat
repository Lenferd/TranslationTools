@echo off
::SetLocal EnableExtensions EnableDelayedExpansion
set folder_name=%1

if "%folder_name%" == "" (
    echo FAIL: "Directory name not set"
    exit /b 1
) else (
    echo folder name = %folder_name%
)
mkdir %folder_name%
cd %folder_name%

mkdir input_lvl
mkdir input_resources

mkdir result_lvl
mkdir result_dialogs
mkdir result_resources

pause
exit /B