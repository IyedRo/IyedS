:: Section 1: Delete Cookies (Browsers and System Cookies)
echo Deleting browser cookies...
:: For Google Chrome
del /f /s /q C:\Users\%username%\AppData\Local\Google\Chrome\User Data\Default\Cookies
del /f /s /q C:\Users\%username%\AppData\Local\Google\Chrome\User Data\Default\Cache\*
:: For Mozilla Firefox
del /f /s /q C:\Users\%username%\AppData\Roaming\Mozilla\Firefox\Profiles\*.default\cookies.sqlite
del /f /s /q C:\Users\%username%\AppData\Roaming\Mozilla\Firefox\Profiles\*.default\cache2\*
:: For Microsoft Edge
del /f /s /q C:\Users\%username%\AppData\Local\Microsoft\Edge\User Data\Default\Cookies
del /f /s /q C:\Users\%username%\AppData\Local\Microsoft\Edge\User Data\Default\Cache\*
:: For Internet Explorer (if applicable)
del /f /s /q C:\Users\%username%\AppData\Local\Microsoft\Windows\INetCache\IE\*
:: Section 2: Completion Message
echo Cookies cleared from browsers.
pause