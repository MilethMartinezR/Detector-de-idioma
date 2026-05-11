# Detector de Idiomas

Detecta automáticamente si un texto está en **Español, Inglés, Francés o Portugués** usando técnicas de Procesamiento de Lenguaje Natural (PLN).

---

## Estructura del proyecto

```
Detector-de-idioma/
│
├── INICIAR.bat             # Ejecutor para Windows
├── iniciar.sh              # Ejecutor para Linux/Mac
├── requirements.txt        # Dependencias del proyecto
│
├── datos/
│   └── Language Detection.csv   # Corpus de entrenamiento
│
├── modelo/
│   ├── modelo_idiomas.pkl        # Modelo entrenado (generado automáticamente)
│   └── vectorizador.pkl          # Vectorizador TF-IDF (generado automáticamente)
│
├── notebook/
│   └── entrenamiento.ipynb       # Exploración y análisis del modelo
│
└── app/
    ├── entrenar.py               # Script de entrenamiento
    └── app.py                    # Interfaz web (Streamlit)
```

## Cómo usar

### En Windows (recomendado):
1. Abre una terminal en la carpeta del proyecto y ejecuta:
   ```
   .\INICIAR.bat
   ```
2. Espera a que se abra el navegador automáticamente en `http://localhost:8501`
3. ¡Listo!

> **Nota sobre Visual Studio Code:** si no ejecuta el `.bat` con el botón de Play — puede que ese botón cambie el directorio de trabajo y los archivos no se encuentran. En su lugar, abre la terminal integrada de VS Code (`Ctrl + ñ`), asegúrate de estar en la carpeta raíz del proyecto y ejecuta `.\INICIAR.bat` desde ahí. También puedes hacer doble clic directamente sobre el archivo desde el Explorador de Windows.

> **Nota sobre el correo en Streamlit:** al abrir la app por primera vez, Streamlit puede mostrar una pantalla solicitando un correo electrónico. No es obligatorio ingresar uno real — basta con escribir cualquier texto con formato de correo válido (por ejemplo, `usuario@correo.com`) y continuar.

### En Linux/Mac:
El script `iniciar.sh` está disponible. Si deseas intentarlo:
1. Abre una terminal en la carpeta del proyecto
2. Ejecuta: `bash iniciar.sh`

Si encuentras errores, puedes instalar las dependencias manualmente con `pip3 install -r requirements.txt` y luego ejecutar `streamlit run app/app.py`.

---

## Requisito previo

Solo necesitas tener **Python 3.8 o superior** instalado.

- **Windows:** descárgalo desde https://www.python.org/downloads/
  - Durante la instalación marca **"Add Python to PATH"**
- **Linux/Ubuntu:** `sudo apt install python3 python3-pip`
- **Mac:** `brew install python`

---

## Cómo funciona

El modelo usa un pipeline de dos etapas:

1. **Vectorización TF-IDF con n-gramas de caracteres:** cada texto se convierte en un vector numérico analizando secuencias de 2 a 4 caracteres (por ejemplo, de la palabra "nación" extrae `na`, `ac`, `ció`, `ión`, `naci`, `ción`, etc.). Esto permite capturar patrones fonéticos y ortográficos únicos de cada idioma sin depender de palabras completas.

2. **Clasificación con Regresión Logística:** el modelo aprende qué combinaciones de caracteres son estadísticamente más frecuentes en cada idioma y asigna probabilidades a cada uno. Se reporta el idioma con mayor probabilidad junto con un porcentaje de confianza.

---

## Idiomas soportados

| Idioma     | Código | Ejemplos de patrones clave     |
|------------|--------|-------------------------------|
| Español    | ES     | `ción`, `ño`, `que`, `dad`    |
| Inglés     | EN     | `th`, `ing`, `tion`, `the`    |
| Francés    | FR     | `eau`, `eur`, `oux`, `ais`    |
| Portugués  | PT     | `ção`, `ão`, `lho`, `nha`     |

---

## Limitaciones conocidas

### Textos cortos
El modelo requiere **mínimo 10 caracteres** (validado en la interfaz) y funciona mejor con oraciones completas. Con textos muy cortos como una sola palabra o pocas letras, los n-gramas disponibles son insuficientes para distinguir idiomas y la predicción puede ser incorrecta o con baja confianza.

### Mezcla de idiomas
Si el texto contiene párrafos o frases en más de un idioma (por ejemplo, una cita en inglés dentro de un texto en español), el modelo detectará el idioma dominante pero no identificará la mezcla. Solo produce una única etiqueta por texto.

### Nombres propios y siglas
Los nombres propios (personas, marcas, ciudades), siglas y términos técnicos en inglés presentes en textos de otro idioma pueden sesgar la predicción hacia el inglés, ya que estos elementos no aportan n-gramas característicos del idioma original.

### Solo 4 idiomas
El modelo únicamente reconoce español, inglés, francés y portugués. Si se ingresa texto en cualquier otro idioma (italiano, alemán, árabe, etc.), el sistema igualmente forzará una clasificación dentro de estos cuatro, posiblemente con baja confianza pero sin indicar que el idioma es desconocido.

### Español vs. Portugués
Estos dos idiomas comparten muchos n-gramas (ambos tienen `que`, `ción`/`ção`, `con`, `par`). En textos cortos o con vocabulario neutro pueden confundirse entre sí. Se recomienda ingresar al menos 2-3 oraciones para mejorar la distinción.

### Textos con muchos números o caracteres especiales
El preprocesamiento elimina números y símbolos, dejando solo letras. Un texto compuesto principalmente de números, URLs, código de programación o emojis quedará casi vacío tras la normalización y producirá resultados no confiables.

### El modelo no se actualiza automáticamente
El modelo se entrena una sola vez con el corpus incluido. No aprende de los textos que los usuarios ingresan en la app. Si se desea mejorar la precisión, es necesario reentrenar manualmente ejecutando `entrenar.py` con un corpus actualizado.

---

## Dependencias

| Librería       | Versión recomendada | Uso                                      |
|----------------|---------------------|------------------------------------------|
| `pandas`       | ≥ 1.3               | Carga y manipulación del corpus CSV      |
| `scikit-learn` | ≥ 1.0               | TF-IDF, Regresión Logística y métricas   |
| `joblib`       | ≥ 1.0               | Serialización del modelo entrenado       |
| `streamlit`    | ≥ 1.20              | Interfaz web interactiva                 |
| `matplotlib`   | ≥ 3.4               | Visualizaciones (notebook)               |
| `seaborn`      | ≥ 0.11              | Visualizaciones (notebook)               |

---

## Notas

- La **primera vez** que inicies tardará unos minutos (instala librerías y entrena el modelo).
- Las siguientes veces abrirá directamente sin reentrenar.
- El modelo entrenado se guarda en la carpeta `modelo/` automáticamente.
- Para reentrenar el modelo (por ejemplo, tras cambiar el corpus), elimina los archivos `.pkl` de la carpeta `modelo/` y vuelve a ejecutar el iniciador.
- Si el navegador no abre automáticamente, ve manualmente a `http://localhost:8501`.
