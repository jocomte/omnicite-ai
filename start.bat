@echo off
title OmniCite AI - GEO SaaS Server
color 0b
echo ========================================================
echo   DEMARRAGE DE OMNICITE AI (GEO & AI VISIBILITY SAAS)
echo ========================================================
echo.
echo [1/2] Ouverture de votre navigateur sur http://localhost:8000...
timeout /t 2 /nobreak > nul
start http://localhost:8000
echo [2/2] Lancement du serveur Python SQLite & Stripe...
python server.py
pause
