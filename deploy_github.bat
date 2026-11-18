@echo off
title OmniCite AI - Deploiement GitHub 1-Clic
color 0a
echo ========================================================
echo   OMNICITE AI - DEPLOIEMENT AUTOMATIQUE SUR GITHUB
echo ========================================================
echo.
cd /d "%~dp0"

echo [1/4] Verification de Git...
git --version >nul 2>&1
if errorlevel 1 (
    echo [ERREUR] Git n'est pas installe ou non accessible dans le PATH.
    pause
    exit /b 1
)

echo [2/4] Initialisation du repertoire Git local...
if not exist ".git" (
    git init
    git branch -M main
)

echo [3/4] Ajout des fichiers et creation du commit...
git add .
git commit -m "OmniCite AI SaaS - Production Release with GEO Audit, Stripe & Lead Capture"

echo.
echo [4/4] Publication sur GitHub via GitHub CLI...
gh --version >nul 2>&1
if not errorlevel 1 (
    echo Tentative de creation automatique du repository sur votre compte GitHub...
    gh repo create omnicite-ai --public --source=. --push
    if not errorlevel 1 (
        echo.
        echo ========================================================
        echo  SUCCES : Votre SaaS est maintenant publie sur GitHub !
        echo ========================================================
        echo Vous pouvez maintenant le connecter en 1 clic sur :
        echo - Render : https://render.com
        echo - Railway : https://railway.app
        echo.
        pause
        exit /b 0
    )
)

echo.
echo [INFO] Pour lier votre repo distant manuellement :
echo 1. Creez un repo nomme 'omnicite-ai' sur github.com
echo 2. Executez :
echo    git remote add origin https://github.com/VOTRE_USER/omnicite-ai.git
echo    git push -u origin main
echo.
pause
