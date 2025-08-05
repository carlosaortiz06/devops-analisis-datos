import pandas as pd
import os

# Cargar datos
df = pd.read_csv("data/processed/datos_limpios.csv")

# Estadísticas básicas
total_registros = len(df)
promedio_edad = df['edad'].mean()

# Crear carpeta informe si no existe
os.makedirs("informe", exist_ok=True)

# Generar informe.md
with open("informe/informe.md", "w", encoding="utf-8") as f:
    f.write("# Informe de Resultados\n\n")
    f.write("**Resumen generado automáticamente:**\n\n")
    f.write(f"Se analizaron **{total_registros} registros**. ")
    f.write(f"La edad promedio fue de **{promedio_edad:.2f} años**.\n\n")

    f.write("## Distribución de Edad\n")
    f.write("![Edad](informe/graficas/edad.png)\n\n")

    f.write("## Opiniones por Región\n")
    f.write("![Región](informe/graficas/opiniones_region.png)\n\n")

    f.write("## Distribución de Opiniones\n")
    f.write("![Opiniones](informe/graficas/opiniones_pie.png)\n\n")

    f.write("**Conclusión generada automáticamente:**\n\n")
    f.write("Los datos procesados muestran tendencias claras en la distribución de edades y opiniones según la región. Se recomienda un análisis más profundo en futuras ejecuciones.\n")
