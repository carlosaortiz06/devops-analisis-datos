import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Crear carpeta de salida si no existe
os.makedirs("informe/graficas", exist_ok=True)

# Cargar datos limpios
ruta = "data/processed/datos_limpios.csv"
df = pd.read_csv(ruta)

# --- Gráfica 1: Distribución de edad ---
plt.figure(figsize=(8,5))
df['edad'].hist(bins=8, color='skyblue', edgecolor='black')
plt.title("Distribución de Edad")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.grid(False)
plt.tight_layout()
plt.savefig("informe/graficas/edad.png")
plt.close()

# --- Gráfica 2: Opiniones por región ---
plt.figure(figsize=(10,6))
sns.countplot(data=df, x='region', hue='opinion')
plt.title("Opiniones por Región")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("informe/graficas/opiniones_region.png")
plt.close()

# --- Gráfica 3: Porcentaje de opiniones ---
plt.figure(figsize=(6,6))
opinion_counts = df['opinion'].value_counts()
opinion_counts.plot.pie(autopct='%1.1f%%', startangle=90, colors=['green','red','gray'])
plt.title("Distribución de Opiniones")
plt.ylabel('')
plt.tight_layout()
plt.savefig("informe/graficas/opiniones_pie.png")
plt.close()

print("✅ Gráficas generadas correctamente.")
