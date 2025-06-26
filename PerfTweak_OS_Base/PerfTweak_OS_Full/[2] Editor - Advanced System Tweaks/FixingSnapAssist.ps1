Write-Host "`nFixing Snap Assist settings..." -ForegroundColor Cyan

# --- Enable Snap Assist features ---
Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" -Name "SnapAssist" -Value 1 -Force

# Enable Snap Flyout UI (Windows 11 feature)
Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" -Name "EnableSnapAssistFlyout" -Value 1 -Force

# Enable dragging windows for snapping
Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name "WindowArrangementActive" -Value 1 -Force
Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name "DockMoving" -Value 1 -Force
Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name "DragFromMaximize" -Value 1 -Force

# --- Windows 11-specific Snap settings ---
$multitaskKey = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced\MultitaskingView"
If (-Not (Test-Path $multitaskKey)) {
    New-Item -Path $multitaskKey -Force | Out-Null
}
Set-ItemProperty -Path $multitaskKey -Name "Enabled" -Value 1 -Force

# --- Restart Windows Explorer to apply changes ---
Write-Host "Restarting Windows Explorer..." -ForegroundColor Yellow
Stop-Process -Name explorer -Force
Start-Process explorer

Write-Host "`n✅ Snap Assist settings applied. Please reboot your computer to finalize the settings." -ForegroundColor Green
