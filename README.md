# Insurance Risk Analytics & Predictive Modeling

## Project Overview

This project focuses on end-to-end insurance risk analytics and predictive modeling using historical car insurance data. The objective is to analyze insurance claims, understand patterns in risk and profitability, and establish a reproducible data pipeline to ensure all analysis can be audited and reproduced.

## Features & Objectives

* **Exploratory Data Analysis (EDA):** Understand the dataset, detect outliers, analyze distributions, and visualize loss ratios across provinces, vehicle types, and gender.
* **Data Version Control (DVC):** Track dataset versions, automate preprocessing, and ensure reproducible workflows.
* **Statistical Modeling:** Prepare for predictive modeling and hypothesis testing to determine risk differences across customer segments.

## Directory Structure

```
10Academy-Insurance-Risk-Analytics/
│
├── data/
│   ├── raw/                 # Raw dataset files
│   └── processed/           # Cleaned and preprocessed data
│
├── src/                     # Source code
│   ├── preprocess.py        # Data preprocessing script
│   ├── eda.py               # Exploratory Data Analysis script
│   └── dvc_pipeline.dvc     # DVC pipeline config
│
├              
├── dvc.yaml                 # DVC pipeline configuration
├── requirements.txt         # Python dependencies
└── README.md                # Project overview and instructions
```

## Installation & Setup

1. Clone the repository:

```bash
git clone <repository_url>
cd 10Academy-Insurance-Risk-Analytics
```

2. (Optional) Create a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Initialize DVC and setup remote storage:

```bash
dvc init
dvc remote add -d localstorage /path/to/local/storage
```

5. Add and track data with DVC:

```bash
dvc add data/raw/MachineLearningRating_v3.txt
git add data/.gitignore *.dvc
git commit -m "Add raw dataset and initialize DVC"
dvc push
```

## Usage

### Preprocessing Data

```bash
python src/preprocess.py
```

### Exploratory Data Analysis

```bash
python notebook/eda.py
```

### Reproducing the Pipeline

```bash
dvc repro
```

## Key Highlights

* Loss ratios calculated and visualized by province, vehicle type, and gender.
* Outliers in claims and custom value estimates identified.
* DVC ensures reproducible and auditable data pipelines.

## Contributing

Contributions are welcome! Please fork the repository, create a branch, and submit a pull request with a descriptive message.

## License

This project is for educational purposes and may be adapted for internal use.

---

*For more details, refer to the interim report covering Task 1 & Task 2.*
