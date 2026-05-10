@echo off
title Detector de Idiomas
color 0A
echo ============================================
echo      DETECTOR DE IDIOMAS - Iniciando...
echo ============================================
echo.

:: Verificar si Python esta instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python no esta instalado.
    echo.
    echo Por favor descarga e instala Python desde:
    echo https://www.python.org/downloads/
    echo.
    echo IMPORTANTE: Durante la instalacion marca la casilla
    echo "Add Python to PATH"
    echo.
    pause
    exit
)

echo [OK] Python encontrado
echo.

:: Instalar librerias si no estan instaladas
echo Verificando e instalando librerias necesarias...
echo Esto puede tardar unos minutos la primera vez...
echo.
pip install -r requirements.txt --quiet

echo.
echo [OK] Librerias listas
echo.

:: Verificar si el modelo ya existe
if not exist "modelo\modelo_idiomas.pkl" (
    echo Entrenando el modelo por primera vez...
    echo Esto puede tardar unos minutos...
    echo.
    python app\entrenar.py
    echo.
    echo [OK] Modelo entrenado y guardado
    echo.
)

:: Iniciar la aplicacion
echo ============================================
echo    Abriendo la aplicacion en el navegador...
echo ============================================
echo.
echo Para cerrar la aplicacion cierra esta ventana
echo.
streamlit run app\app.py --server.headless false
pause
