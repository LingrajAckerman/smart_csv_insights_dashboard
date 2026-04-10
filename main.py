from fastapi import FastAPI, HTTPException, UploadFile, File
import pandas as pd

app = FastAPI()

@app.post("/analyze-csv")

def analyze_csv_file(file: UploadFile = File(...)):

    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed")