import pandas as pd

def evaluar_dataset(path):
    print(f"\n📊 Evaluando dataset: {path}")
    df = pd.read_csv(path)
    total_filas, total_columnas = df.shape
    print(f"\n✅ Tamaño: {total_filas} filas x {total_columnas} columnas")

    # Valores nulos
    nulos = df.isnull().sum()
    columnas_con_nulos = nulos[nulos > 0]
    if not columnas_con_nulos.empty:
        print("\n⚠️ Columnas con valores nulos:")
        print(columnas_con_nulos)
    else:
        print("\n✅ No hay valores nulos.")

    # Tipos de datos
    print("\n🔎 Tipos de datos:")
    print(df.dtypes)

    # Valores únicos por columna
    print("\n📌 Valores únicos por columna:")
    for col in df.columns:
        print(f"- {col}: {df[col].nunique()} únicos")

    # Duplicados
    duplicados = df.duplicated().sum()
    print(f"\n🧭 Filas duplicadas: {duplicados}")

    # Revisión de columnas poco útiles
    columnas_con_pocos_unicos = [col for col in df.columns if df[col].nunique() <= 1]
    if columnas_con_pocos_unicos:
        print("\n⚠️ Columnas con un solo valor (poco útiles):")
        print(columnas_con_pocos_unicos)

    # Revisión general
    print("\n🧠 Evaluación final:")
    if total_filas < 100:
        print("❌ Dataset demasiado pequeño para modelos robustos.")
    elif len(columnas_con_nulos) > total_columnas * 0.3:
        print("❌ Demasiadas columnas con valores nulos.")
    elif duplicados > total_filas * 0.5:
        print("❌ Muchos duplicados, podrían afectar el análisis.")
    else:
        print("✅ Dataset apto para análisis y modelado inicial.")

if __name__ == "__main__":
    evaluar_dataset("data/processed/datos_limpios.csv")
