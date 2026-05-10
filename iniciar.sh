#!/bin/bash

echo "============================================"
echo "     DETECTOR DE IDIOMAS - Iniciando..."
echo "============================================"
echo ""

# Verificar si Python esta instalado
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python3 no esta instalado."
    echo ""
    echo "En Ubuntu/Debian ejecuta:"
    echo "  sudo apt install python3 python3-pip"
    echo ""
    echo "En Mac ejecuta:"
    echo "  brew install python"
    echo ""
    read -p "Presiona Enter para salir..."
    exit 1
fi

echo "[OK] Python encontrado"
echo ""

# Instalar librerias
echo "Verificando e instalando librerias necesarias..."
echo "Esto puede tardar unos minutos la primera vez..."
echo ""
pip3 install -r requirements.txt --quiet

echo ""
echo "[OK] Librerias listas"
echo ""

# Verificar si el modelo ya existe
if [ ! -f "modelo/modelo_idiomas.pkl" ]; then
    echo "Entrenando el modelo por primera vez..."
    echo "Esto puede tardar unos minutos..."
    echo ""
    python3 app/entrenar.py
    echo ""
    echo "[OK] Modelo entrenado y guardado"
    echo ""
fi

# Iniciar la aplicacion
echo "============================================"
echo "   Abriendo la aplicacion en el navegador..."
echo "============================================"
echo ""
echo "Para cerrar la aplicacion presiona Ctrl+C"
echo ""
streamlit run app/app.py --server.headless false
