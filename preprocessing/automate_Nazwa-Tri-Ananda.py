import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

INPUT_FILE = "online_sales_dataset.csv"
OUTPUT_DIR = "preprocessing"
OUTPUT_FILE = "online_sales_preprocessed.csv"

def preprocess_data(input_path: str):
    print("Memulai proses preprocessing data...")

    # Load data
    df = pd.read_csv(input_path)

    # =====================
    # Missing Values
    # =====================
    df.dropna(subset=['WarehouseLocation'], inplace=True)

    # Drop kolom tidak relevan
    df.drop(columns=[
        'InvoiceNo',
        'StockCode',
        'InvoiceDate',
        'CustomerID'
    ], inplace=True)

    # =====================
    # Binning
    # =====================
    df['Quantity_Group'] = pd.cut(
        df['Quantity'],
        bins=[0, 15, 35, df['Quantity'].max()],
        labels=['Low', 'Medium', 'High']
    )

    # =====================
    # Encoding sederhana 
    # =====================
    categorical_cols = df.select_dtypes(include='object').columns for col in categorical_cols: df[col] = df[col].astype('category').cat.codes

    # =====================
    # Simpan ke folder preprocessing
    # =====================
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)

    df.to_csv(output_path, index=False)

    print(f"Preprocessing selesai. File disimpan di: {output_path}")

if __name__ == "__main__":
    preprocess_data(INPUT_FILE)
