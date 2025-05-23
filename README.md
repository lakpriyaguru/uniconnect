# PyData UniConnect 2025 WUSL - Assessment

# Group 09 - CASE 03: The Wheels in Motion

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset Description](#dataset-description)
- [Project Structure](#project-structure)
- [Installation \& Setup](#installation--setup)
- [Tasks \& Methodology](#tasks--methodology)
  - [Task 02: Data Preparation](#task-02-data-preparation-task_02ipynb)
  - [Task 03: NLP with HuggingFace](#task-03-nlp-with-huggingface-task_03ipynb)
  - [Task 04: Interactive Dashboard](#task-04-interactive-dashboard-task_04py)
- [Results \& Insights](#results--insights)
- [Contributors](#contributors)

---

## Project Overview

This project analyzes and visualizes the landscape of public passenger vehicles registered in Illinois, including taxis, liveries, ambulances, medicars, charter and sightseeing buses, horse-drawn carriages, and pedicabs. Our goals are to:

- Clean, integrate, and explore multi-source vehicle licensing data
- Apply NLP to customer reviews using HuggingFace models
- Build an interactive Plotly Dash dashboard to tell a compelling data story

This repository is maintained as part of the UniConnect Python Project for Group 09.

---

## Dataset Description

**Vehicle Data:**

- 9 CSV files in `PassengerVehicle_Stats/`, each representing a different fuel type (e.g., Gasoline, Electric, Hybrid, etc.)
- Each file contains vehicle attributes such as status, make, model, year, color, fuel source, accessibility, company info, and more

**Customer Reviews:**

- `car_reviews.csv`: 7,000+ customer reviews for Kia vehicles (used for NLP tasks)

**Key Features:**

- Public Vehicle Number, Status, Vehicle Make/Model/Year, Color, Fuel Source
- Wheelchair Accessibility, Company Name, Address, City/State/ZIP
- Taxi Affiliation, License Management, Record ID

---

## Project Structure

```
uniconnect_project_group_09
├── PassengerVehicle_Stats/        # Raw vehicle CSV files (9 files, by fuel type)
│   ├──Bio-Diesel_PassengerVehicle_Stats.csv
│   ├──Compressed-Natural-Gas_PassengerVehicle_Stats.csv
│   ├──Diesel_PassengerVehicle_Stats.csv
│   ├──Electric_PassengerVehicle_Stats.csv
│   ├──Flex-Fuel_PassengerVehicle_Stats.csv
│   ├──Gasoline_PassengerVehicle_Stats.csv
│   ├──Horse_PassengerVehicle_Stats.csv
│   ├──Hybrid_PassengerVehicle_Stats.csv
│   └──Pedal_PassengerVehicle_Stats.csv
│
├── .gitignore                   # gitignore file
├── analyzed_reviews.csv         # Analyzed Reviews with NLP predictions
├── analyzed_reviews.parquet     # Analyzed Reviews with NLP predictions (parquet)
├── car_reviews.csv              # Raw customer reviews for Kia vehicles
├── combined_vehicles.csv        # Combined and cleaned vehicle data
├── README.md                    # Project documentation (this file)
├── requirements.txt             # Python dependencies
├── task_02.ipynb                # Data preparation notebook
├── task_03.ipynb                # NLP and sentiment analysis notebook
└── task_04.py                   # Plotly Dash dashboard script
```

---

## Installation \& Setup

1. **Clone the repository:**

```bash
git clone https://github.com/lakpriyaguru/uniconnect_project_group_09.git
cd uniconnect_project_group_09
```

2. **Create a virtual environment and install dependencies:**

```bash
python -m venv .venv
source .venv/bin/activate    # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

3. **Data files:**
   - Ensure all CSV files are present in the directory.

---

## Tasks \& Methodology

### Task 02: Data Preparation (`task_02.ipynb`)

- **Combine** all 9 vehicle CSVs into one DataFrame (`vehicles_df`)
- **Explore** data structure, types, and missing/duplicate values
- **Clean** data by removing duplicates and handling missing/outlier values where necessary
- **Feature Engineering:**
  - Extract `Vehicle Type` from the `Record ID`
  - Drop unnecessary columns (`Address`, `Public Vehicle Number`)
- **Output:**
  - `combined_vehicles.csv`

### Task 03: NLP with HuggingFace (`task_03.ipynb`)

- **Read** `car_reviews.csv`
- **Zero-shot classification** to assign each review to one of:
  - Driving experience, Features, Value for money, Issues, Other
- **Sentiment analysis** using a suitable HuggingFace model
- **Output:**
  - `analyzed_reviews.csv` (with `talks_about` and `sentiment` columns)
- **Visualizations:**
  - Sentiment and topic distribution charts

### Task 04: Interactive Dashboard (`task_04.py`)

- **Built with Plotly Dash**
- **Features:**
  - At least 5 interactive chart types (bar, pie, treemap, sunburst, histogram, etc.)
  - Filters for vehicle type, fuel source, year, and more
  - Story-driven layout for actionable insights
- **Run locally:**

```bash
python task_04.py
# Visit http://localhost:8050 in your browser
```

---

## Results \& Insights

- **Fleet Composition:**
  - Breakdown by vehicle type, fuel source, and company
- **Operational Status:**
  - Active vs. inactive/violation vehicles
- **Accessibility:**
  - Proportion of wheelchair-accessible vehicles
- **Dashboard:**
  - Interactive exploration and business insights

---

## Contributors

- Lakpriya Gurugamage
- Kavindu Madulakshan
- Randika Achinthani
- Nadeesha Perera

---
