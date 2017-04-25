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
mkdir input_dialogs
mkdir input_dialog_repacked

mkdir orig_dialogs
mkdir orig_resources
mkdir orig_lvl
mkdir origin_dialog_to_transl


mkdir input_lvl_binaries
mkdir input_lvl_binaries2
mkdir input_resources_binaries

mkdir result_lvl
mkdir result_resources

pause
exit /B