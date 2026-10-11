import os
import json

# Definisi file notebook dan struktur template isian kodenya
notebooks_structure = {
    "notebooks/01_data_exploration_and_cleaning.ipynb": {
        "title": "01. Data Exploration & Cleaning",
        "description": "Tahap awal pemeriksaan dataset Tokopedia Product Reviews, pembersihan data, dan handling missing values.",
        "steps": [
            "# 1. Import Library (pandas, numpy, dll)",
            "# 2. Load Raw Dataset dari 'data/raw/tokopedia_products_raw.csv'",
            "# 3. Check Dataset Info (shape, dtypes, head, tail)",
            "# 4. Handling Missing Values & Duplicates",
            "# 5. Data Type Formatting (rating -> float, sold -> int)",
            "# 6. Export Cleaned Data ke 'data/processed/tokopedia_cleaned.csv'"
        ]
    },
    "notebooks/02_sales_and_category_analysis.ipynb": {
        "title": "02. Sales & Category Performance Analysis",
        "description": "Analisis performa penjualan (sold) per kategori produk dan identifikasi produk terlaris.",
        "steps": [
            "# 1. Load Processed Data dari 'data/processed/tokopedia_cleaned.csv'",
            "# 2. Agregasi Total Sold & Product Count per Category",
            "# 3. Distribusi Penjualan per Kategori (Bar Chart / Pie Chart)",
            "# 4. Top 10 Products Terlaris Keseluruhan & per Kategori",
            "# 5. Simpan Grafik ke 'outputs/figures/sales_by_category.png'"
        ]
    },
    "notebooks/03_sentiment_and_review_analytics.ipynb": {
        "title": "03. Sentiment & Review Text Analytics",
        "description": "Analisis sentiment ulasan pembeli dan hubungannya terhadap rating serta jumlah barang terjual.",
        "steps": [
            "# 1. Load Processed Data dari 'data/processed/tokopedia_cleaned.csv'",
            "# 2. Distribusi Rating (1-5) dan Categorization Sentiment (Positive, Neutral, Negative)",
            "# 3. Korelasi Antara Rating vs Total Sold (Scatter Plot)",
            "# 4. Text Mining: Ekstraksi Kata Kunci pada Ulasan Rating Low (1-2) vs High (4-5)",
            "# 5. Simpan Grafik ke 'outputs/figures/sentiment_distribution.png'"
        ]
    },
    "notebooks/04_executive_summary_and_export.ipynb": {
        "title": "04. Executive Summary & Dashboard Preparation",
        "description": "Rangkuman insight utama untuk kebutuhan slide presentasi dan dashboard Looker Studio / Power BI.",
        "steps": [
            "# 1. Import All Processed Insights & Metrics Summary",
            "# 2. Rekap KPI Utama (Total Sold, Avg Rating, Total Categories, Total Shops)",
            "# 3. Buat Ringkasan Tabel Agregasi untuk Dashboard Looker Studio / Power BI",
            "# 4. Penyiapan Bahan untuk Slide Presentasi (Problem, Method, Result, Impact)",
            "# 5. Export Summary CSV ke 'outputs/reports/summary_metrics.csv'"
        ]
    }
}

def create_jupyter_notebook(path, title, description, steps):
    cells = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [f"# {title}\n", f"**Deskripsi:** {description}\n"]
        }
    ]
    
    for step in steps:
        cells.append({
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [f"{step}\n"]
        })
        
    notebook_content = {
        "cells": cells,
        "metadata": {
            "language_info": {"name": "python"}
        },
        "nbformat": 4,
        "nbformat_minor": 2
    }
    
    with open(path, "w", encoding="utf-8") as f:
        json.dump(notebook_content, f, indent=2)

print("--- Membuat File Jupyter Notebook (.ipynb) ---")
for nb_path, content in notebooks_structure.items():
    create_jupyter_notebook(nb_path, content["title"], content["description"], content["steps"])
    print(f"[OK] File berhasil dibuat: {nb_path}")

print("\n Selesai! Semua file notebook (.ipynb) siap diisi kodingan di VS Code.")