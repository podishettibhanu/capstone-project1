# Zepto Data & AI Platform

## Project Overview

This project implements a complete Data & AI platform for a Zepto-style application. It combines data collection, data cleaning, SQL analytics, machine learning analysis, and an AI-powered support assistant.

The project is organized into three main modules:

* `data_pipeline` — Web scraping, data cleaning, SQLite database creation, and SQL analysis
* `analytics` — Titanic dataset exploration, machine learning classification, imbalance handling, and fare regression
* `support_assistant` — Retrieval-Augmented Generation (RAG) support assistant using embeddings, ChromaDB, LangGraph, and FastAPI

## Repository Structure

```text
zepto-ai/
│
├── data_pipeline/
│   ├── scrape_books.py
│   ├── clean_data.py
│   ├── database.py
│   ├── queries.sql
│   ├── run_queries.py
│   ├── query_results.md
│   ├── books_raw.csv
│   ├── books_cleaned.csv
│   └── zepto_books.db
│
├── analytics/
│
├── support_assistant/
│
├── requirements.txt
└── README.md
```

## Technologies Used

* Python
* Requests
* BeautifulSoup
* Pandas
* NumPy
* SQLite
* SQL
* Matplotlib
* Seaborn
* Scikit-learn
* SciPy
* Imbalanced-learn
* Joblib
* Sentence Transformers
* ChromaDB
* LangGraph
* LangChain
* FastAPI
* Uvicorn
* Pydantic

## Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd zepto-ai
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

## Module 1 — Data Pipeline

The data pipeline collects book information from `books.toscrape.com`.

The scraper collects:

* Title
* Price in GBP
* Star rating
* Availability
* Category

The pipeline collects data from the first five product pages and produces a dataset containing 100 books.

### Run the scraper

```powershell
python data_pipeline\scrape_books.py
```

This creates:

```text
data_pipeline/books_raw.csv
```

### Data Cleaning

The cleaning process:

* Converts price values to numeric format
* Converts star ratings from text to integers from 1 to 5
* Converts availability into a boolean `in_stock` field
* Removes rows with missing required values
* Converts GBP prices to INR

The fixed conversion rate is:

```text
1 GBP = 105.50 INR
```

### Run cleaning

```powershell
python data_pipeline\clean_data.py
```

This creates:

```text
data_pipeline/books_cleaned.csv
```

### SQLite Database

The cleaned data is stored in SQLite using two normalized tables:

```text
categories
    |
    | category_id
    |
books
```

The `books` table contains a foreign key referencing `categories.category_id`.

### Create the database

```powershell
python data_pipeline\database.py
```

This creates:

```text
data_pipeline/zepto_books.db
```

### SQL Queries

The project includes SQL queries demonstrating:

* `WHERE`
* `ORDER BY`
* `LIMIT`
* `DISTINCT`
* `BETWEEN`
* `IN`
* `JOIN`

Run all queries using:

```powershell
python data_pipeline\run_queries.py
```

The results are saved to:

```text
data_pipeline/query_results.md
```

The project also reproduces the SQL JOIN using `pandas.merge()`.

## Data Pipeline Design Decisions

### Price Conversion

Book prices are converted from GBP to INR using the fixed rate:

```text
1 GBP = 105.50 INR
```

### Rating Conversion

The website provides ratings as words such as:

```text
One
Two
Three
Four
Five
```

These are converted to:

```text
1
2
3
4
5
```

### Availability

Availability text is converted into a boolean:

```text
True  → In stock
False → Not in stock
```

### Missing Values

Rows with missing required fields such as title, price, rating, or category are removed after numeric parsing.

## SQL Results

The complete SQL queries and outputs are available in:

```text
data_pipeline/query_results.md
```

The file also contains the equivalent `pandas.merge()` result for the SQL JOIN.

## Module 2 — Analytics

The analytics module performs exploratory data analysis and machine learning using the Titanic dataset.

It includes:

* Data loading and inspection
* Missing-value analysis
* Univariate analysis
* Outlier analysis
* Survival-rate analysis
* Correlation analysis
* Multivariate visualizations
* Feature standardization exploration
* Classification
* Imbalance comparison
* Random Forest tuning
* Fare regression
* Model evaluation
* Model saving and reloading

The Titanic dataset is saved locally as:

```text
analytics/titanic.csv
```

This provides an offline fallback for the modeling workflow.

## Module 3 — Support Assistant

The support assistant implements a Retrieval-Augmented Generation workflow.

The architecture is:

```text
Support Documents
       ↓
Document Chunking
       ↓
Sentence Transformer Embeddings
       ↓
ChromaDB
       ↓
User Question
       ↓
Intent Classification
       ↓
Retrieval / Direct Answer
       ↓
Structured Response
```

The assistant uses:

* Sentence Transformers
* `all-MiniLM-L6-v2`
* ChromaDB
* LangGraph
* Pydantic
* FastAPI

A deterministic `MOCK_LLM` mode is included for the graded baseline.

## FastAPI

The support assistant exposes:

```text
POST /ask
```

The API accepts a user question and returns a structured response containing:

* Answer
* Sources
* Confidence

The API can be run locally using Uvicorn.

## Reproducibility

The project is designed to run locally without paid services.

All required Python dependencies are listed in:

```text
requirements.txt
```

The project includes generated datasets, SQL outputs, and local database files where required so that the workflow can be inspected and reproduced.

## Git Workflow

The project uses a feature-branch workflow.

The development process includes:

1. Creating a feature branch
2. Implementing project modules
3. Making multiple commits
4. Merging the feature branch into `main`

Example:

```bash
git checkout -b feature/zepto-ai-platform
git add .
git commit -m "Build data pipeline"
git commit -m "Add analytics and support assistant"
git checkout main
git merge feature/zepto-ai-platform
```

## Project Status

### Data Pipeline

* [x] Web scraping
* [x] Data cleaning
* [x] GBP to INR conversion
* [x] SQLite database
* [x] SQL queries
* [x] SQL JOIN
* [x] Pandas merge
* [x] Query results documentation

### Analytics

* [ ] Exploratory data analysis
* [ ] Visualization
* [ ] Classification
* [ ] Imbalance comparison
* [ ] Random Forest tuning
* [ ] Regression
* [ ] Model persistence

### Support Assistant

* [ ] Document ingestion
* [ ] Chunking
* [ ] Embeddings
* [ ] ChromaDB retrieval
* [ ] LangGraph workflow
* [ ] Structured responses
* [ ] FastAPI
* [ ] Docker

## License

This project was created as an academic capstone project for educational purposes.
## Current Project Status

The capstone project is currently under development.

Completed modules:
- Data Pipeline
- Titanic Analytics
- Support Assistant knowledge base

Upcoming work:
- Complete Support Assistant
- Test all modules
- Final documentation