from fastapi import FastAPI, HTTPException, UploadFile, File
import pandas as pd

app = FastAPI()

@app.post("/analyze-csv")

def analyze_csv_file(file: UploadFile = File(...)):

    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed")
    
    try:
        df = pd.read_csv(file.file)
    
    except Exception:

        raise HTTPException(status_code=400, detail="Invalid CSV file")
    
    return analyze_dataframe(df)
    
def analyze_dataframe(df):
    
    rows, cols = df.shape

    column_names = list(df.columns)

    missing_values = df.isnull().sum().to_dict()

    numeric_stats = {}

    for col in df.select_dtypes(include=['number']).columns:
        numeric_stats[col] = {
            "mean": float(df[col].mean()),
            "min": float(df[col].min()),
            "max": float(df[col].max())
        }

    return {
    "rows": rows,
    "columns": cols,
    "column_names": column_names,
    "missing_values": missing_values,
    "statistics": numeric_stats
    }