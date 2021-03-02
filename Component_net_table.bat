@echo off
if "%CONDA_PATH%" == "" ( 
echo No Conda Path 
GOTO end )

call %CONDA_PATH%\Scripts\activate.bat
	
if "%COMPONENT_MAPPING%" == "" ( 
echo No COMPONENT_MAPPING Path 
GOTO end )

python "%COMPONENT_MAPPING%\Component_net_table.py"



:End
PAUSE
 