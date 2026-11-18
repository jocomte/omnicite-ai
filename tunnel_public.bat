@echo off
title OmniCite AI - Exposition Publique Instantanee (Tunnel Cloudflare)
color 0b
echo ========================================================
echo   OMNICITE AI - GENERATION D'URL PUBLIQUE HTTPS
echo ========================================================
echo.
echo Ce script va creer une adresse web publique HTTPS securisee
echo (Cloudflare Tunnel) accessible depuis n'importe quel appareil
echo dans le monde sans configuration DNS.
echo.
echo Assurez-vous que server.py est lance (start.bat).
echo.
npx --yes untun tunnel http://localhost:8000
pause
