@echo off
setlocal enabledelayedexpansion

:: Load environment variables from .env file
:: DEPLOY_HOSTNAME DEPLOY_PORT DEPLOY_USERNAME DEPLOY_PASSWORD
for /f "usebackq tokens=1,* delims==" %%A in (".env") do (
  set "%%A=%%B"
)

echo open %DEPLOY_HOSTNAME% 21 > ftp_commands.txt
echo user %DEPLOY_USERNAME% %DEPLOY_PASSWORD% >> ftp_commands.txt
:: echo binary >> ftp_commands.txt

::Upload player3.py to /
::echo delete /player1.py >> ftp_commands.txt
echo put player1.py /player1.py >> ftp_commands.txt

:: Logout and close the connection
echo bye >> ftp_commands.txt

:: Run FTP commands
ftp -n -s:ftp_commands.txt

:: Clean up
del ftp_commands.txt

echo Deployment completed!
