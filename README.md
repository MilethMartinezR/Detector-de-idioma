# 🌍 Detector de Idiomas

Detecta automáticamente si un texto está en **Español, Inglés, Francés o Portugués**.

---

## 📁 Estructura del proyecto

```
detector_idiomas/
│
├── INICIAR.bat              ← Doble clic para iniciar en Windows
├── iniciar.sh               ← Ejecutar en Linux/Mac
├── requirements.txt         ← Librerías necesarias (automático)
│
├── datos/
│   └── Language Detection.csv   ← ⚠️ DEBES COLOCAR ESTE ARCHIVO AQUÍ
│
├── modelo/
│   └── (se generan automáticamente)
│
└── app/
    ├── entrenar.py          ← Entrena el modelo
    └── app.py               ← Aplicación web
```

---

## ▶️ Cómo usar

### En Windows:
1. Coloca el archivo `Language Detection.csv` dentro de la carpeta `datos/`
2. Haz **doble clic** en `INICIAR.bat`
3. Espera a que se abra el navegador
4. ¡Listo!

### En Linux/Mac:
1. Coloca el archivo `Language Detection.csv` dentro de la carpeta `datos/`
2. Abre una terminal en la carpeta del proyecto
3. Ejecuta: `bash iniciar.sh`
4. ¡Listo!

---

## ⚠️ Requisito previo

Solo necesitas tener **Python instalado**.

- Windows: descárgalo desde https://www.python.org/downloads/
  - Durante la instalación marca ✅ **"Add Python to PATH"**
- Linux: `sudo apt install python3 python3-pip`

---

## 📌 Notas

- La **primera vez** que inicies tardará unos minutos (instala librerías y entrena el modelo)
- Las siguientes veces abrirá directamente
- El modelo se guarda en la carpeta `modelo/` automáticamente
