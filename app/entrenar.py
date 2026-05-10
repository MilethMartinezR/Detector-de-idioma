import pandas as pd
import re
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

print("=" * 50)
print("   ENTRENANDO EL MODELO DE DETECCION DE IDIOMAS")
print("=" * 50)

# ─── 1. Cargar el corpus ───────────────────────────────
print("\n[1/5] Cargando el corpus...")

ruta_csv = os.path.join(os.path.dirname(__file__), '..', 'datos', 'Language Detection.csv')

if not os.path.exists(ruta_csv):
    print("\n[ERROR] No se encontro el archivo del corpus.")
    print("Por favor coloca el archivo 'Language Detection.csv'")
    print("dentro de la carpeta 'datos/'")
    input("\nPresiona Enter para salir...")
    exit(1)

df = pd.read_csv(ruta_csv)
print(f"       Corpus cargado: {len(df)} textos en total")

# ─── 2. Filtrar idiomas ────────────────────────────────
print("\n[2/5] Filtrando idiomas seleccionados...")

idiomas = ['Spanish', 'English', 'French', 'Portugeese']
df = df[df['Language'].isin(idiomas)].copy()

print(f"       Textos seleccionados: {len(df)}")
for idioma in idiomas:
    cantidad = len(df[df['Language'] == idioma])
    print(f"       - {idioma}: {cantidad} textos")

# ─── 3. Normalizar textos ──────────────────────────────
print("\n[3/5] Normalizando textos...")

def normalizar(texto):
    texto = texto.lower()
    texto = re.sub(r'\d+', ' ', texto)
    texto = re.sub(r'[^a-záéíóúñüçàèùâêîôûãõäöß\s]', ' ', texto)
    texto = re.sub(r'\s+', ' ', texto)
    return texto.strip()

df['texto_limpio'] = df['Text'].apply(normalizar)
df = df[df['texto_limpio'].str.len() > 5]
print(f"       Textos después de normalizar: {len(df)}")

# ─── 4. Entrenar el modelo ─────────────────────────────
print("\n[4/5] Entrenando el modelo...")

X = df['texto_limpio']
y = df['Language']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

vectorizador = TfidfVectorizer(
    analyzer='char',
    ngram_range=(2, 4),
    max_features=50000,
    sublinear_tf=True
)

X_train_vec = vectorizador.fit_transform(X_train)
X_test_vec = vectorizador.transform(X_test)

modelo = LogisticRegression(max_iter=1000, random_state=42)
modelo.fit(X_train_vec, y_train)

y_pred = modelo.predict(X_test_vec)
accuracy = accuracy_score(y_test, y_pred)
print(f"       Exactitud del modelo: {accuracy * 100:.2f}%")

# ─── 5. Guardar el modelo ──────────────────────────────
print("\n[5/5] Guardando el modelo...")

carpeta_modelo = os.path.join(os.path.dirname(__file__), '..', 'modelo')
os.makedirs(carpeta_modelo, exist_ok=True)

joblib.dump(modelo, os.path.join(carpeta_modelo, 'modelo_idiomas.pkl'))
joblib.dump(vectorizador, os.path.join(carpeta_modelo, 'vectorizador.pkl'))

print("       modelo_idiomas.pkl guardado")
print("       vectorizador.pkl guardado")

print("\n" + "=" * 50)
print(f"   MODELO LISTO - Exactitud: {accuracy * 100:.2f}%")
print("=" * 50)
