import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.preprocessing import LabelEncoder

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
    # Encoding sederhana (tanpa sklearn)
    # =====================
    encoders = {}
    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
        encoders[col] = le

    # =====================
    # Simpan ke folder preprocessing
    # =====================
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)

    df.to_csv(output_path, index=False)

    print(f"Preprocessing selesai. File disimpan di: {output_path}")

if __name__ == "__main__":
    preprocess_data(INPUT_FILE)
