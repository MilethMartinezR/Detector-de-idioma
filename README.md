# 🌍 Detector de Idiomas

Detecta automáticamente si un texto está en **Español, Inglés, Francés o Portugués**.

---

## 📁 Estructura del proyecto

```
detector_idiomas/
│
├── INICIAR.bat             
├── iniciar.sh             
├── requirements.txt         
│
├── datos/
│   └── Language Detection.csv  
│
├── modelo/
│   └── (se generan automáticamente)
│
└── app/
    ├── entrenar.py        
    └── app.py              
```

---

## Cómo usar

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

##  Requisito previo

Solo necesitas tener **Python instalado**.

- Windows: descárgalo desde https://www.python.org/downloads/
  - Durante la instalación marca  **"Add Python to PATH"**
- Linux: `sudo apt install python3 python3-pip`

---

##  Notas

- La **primera vez** que inicies tardará unos minutos (instala librerías y entrena el modelo)
- Las siguientes veces abrirá directamente
- El modelo se guarda en la carpeta `modelo/` automáticamente
