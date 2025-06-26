@echo off
:: This script performs essential cleanup tasks to optimize system performance and remove traces.
:: Author: User (Optimized for Windows Cleanup)

:: Section 1: Flush DNS Cache
echo Flushing DNS cache...
ipconfig /flushdns
echo DNS cache flushed.
pause

:: Section 2: Clear Log Files (Only from known log directories)
echo Clearing log files from known locations...
del /f /s /q C:\Windows\*.log
del /f /s /q C:\Users\%username%\AppData\Local\*.log
del /f /s /q C:\Users\%username%\AppData\Roaming\*.log
echo Log files cleared.
pause

:: Section 3: Clean Temporary Files (Safely)
echo Cleaning temporary files...
del /f /s /q %temp%\*
del /f /s /q C:\Windows\Temp\*
echo Temporary files cleaned.
pause

:: Section 4: Clean Internet Explorer and Edge Cache (if applicable)
echo Cleaning Internet Explorer and Edge cache...
del /f /s /q C:\Users\%username%\AppData\Local\Microsoft\Windows\WebCache\*
del /f /s /q C:\Users\%username%\AppData\Local\Microsoft\Edge\User Data\Default\Cache\*
echo Cache cleaned.
pause

:: Section 5: Remove WiFi Profiles (No saved WiFi passwords or networks)
echo Removing saved WiFi profiles...
netsh wlan delete profile name=*
echo All WiFi profiles deleted.
pause

:: Section 6: Clear Windows Update Cache
echo Clearing Windows Update Cache...
net stop wuauserv
del /f /s /q C:\Windows\SoftwareDistribution\Download\*
net start wuauserv
echo Windows Update cache cleared.
pause

:: Section 7: Clear Windows Defender History
echo Clearing Windows Defender history...
del /f /s /q C:\ProgramData\Microsoft\Windows Defender\Scans\History\*
echo Windows Defender history cleared.
pause

:: Section 8: Clear Event Logs
echo Clearing Event Logs...
wevtutil cl Application
wevtutil cl Security
wevtutil cl System
echo Event logs cleared.
pause

:: Section 9: Clean Prefetch Files
echo Cleaning Prefetch files...
del /f /s /q C:\Windows\Prefetch\*
echo Prefetch files cleaned.
pause

:: Section 10: Clean System Restore Points (Optional - Be cautious)
echo Deleting all system restore points...
vssadmin delete shadows /for=c: /all
echo System restore points deleted.
pause

:: Section 11: Final Clean-up Message
echo All cleanup tasks completed successfully.
pause
