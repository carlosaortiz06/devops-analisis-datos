import pandas as pd

def limpiar_csv(input_file, output_file):
    df = pd.read_csv(input_file)
    df = df.dropna()
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    limpiar_csv("data/raw/datos.csv", "data/processed/datos_limpios.csv")
