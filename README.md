# 📊 Smart CSV Insights Dashboard

A full-stack web application that allows users to upload CSV files and automatically generates useful insights such as dataset structure, missing values, and statistical summaries.

---

## 🚀 Live Demo

* 🌐 Frontend: https://gv9fcycgf2fuhvylg7aqwf.streamlit.app/
* 🔗 Backend API Docs: https://smart-csv-insights-dashboard.onrender.com/docs

---

## 🧠 Features

* 📂 Upload CSV files
* 📊 View dataset overview (rows & columns)
* 🧾 Display column names
* ⚠️ Detect missing values per column
* 📈 Generate statistics for numeric columns (mean, min, max)
* 🔄 Real-time processing via API
* ✅ Input validation and error handling

---

## 🛠️ Tech Stack

* **Backend:** FastAPI
* **Frontend:** Streamlit
* **Language:** Python
* **Libraries:** Pandas
* **Deployment:** Render (Backend), Streamlit Cloud (Frontend)

---

## ⚙️ API Endpoint

### `POST /analyze-csv`

#### Request:

* Upload a `.csv` file using form-data

#### Response:

```json
{
  "rows": 100,
  "columns": 5,
  "column_names": ["col1", "col2"],
  "missing_values": {
    "col1": 0,
    "col2": 2
  },
  "statistics": {
    "col2": {
      "mean": 50.5,
      "min": 10,
      "max": 100
    }
  }
}
```

---

## 🖥️ Local Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Run Backend (FastAPI)

```bash
uvicorn main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

### 4. Run Frontend (Streamlit)

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
.
├── main.py           # FastAPI backend
├── app.py            # Streamlit frontend
├── requirements.txt  # Dependencies
├── README.md         # Documentation
```

---

## 🚧 Error Handling

* Rejects non-CSV files
* Handles invalid/corrupted CSV uploads
* Prevents application crashes with proper validation

---

## 🔮 Future Improvements

* Support for Excel files (.xlsx)
* Data visualization (charts & graphs)
* Downloadable insights report
* Large file optimization

---

## 👨‍💻 Author

**Lingraj Jamkhandi**

---

## ✅ Notes

* This project was built as part of a time-bound technical practice.
* Focus was on **functionality, clean architecture, and production readiness**.

---