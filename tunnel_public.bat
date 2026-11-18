@echo off
title OmniCite AI - Exposition Publique Instantanee (Tunnel)
color 0b
echo ========================================================
echo   OMNICITE AI - GENERATION D'URL PUBLIQUE HTTPS
echo ========================================================
echo.
echo Ce script va creer une adresse web publique HTTPS accessible
echo depuis n'importe quel smartphone ou ordinateur dans le monde.
echo.
echo Assurez-vous que server.py tourne sur le port 8000.
echo.
npx --yes localtunnel --port 8000
pause
