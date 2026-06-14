@echo off
cd /d "%~dp0"

echo ===================================
echo RENOMEANDO COMPROVANTES...
echo ===================================
echo.

py renomear.py

echo.
echo ===================================
echo PROCESSO FINALIZADO
echo ===================================
pause