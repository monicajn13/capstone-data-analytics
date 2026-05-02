# capstone-data-analytics
Final Capstone Project for Data Analytics Course

# Transportation Access & Employment Outcomes  
## A ZIP Code–Level Analysis of Maricopa County (2020–2024)

## Overview
This project examines the relationship between transportation access and employment outcomes across ZIP codes in Maricopa County, Arizona. The purpose of the analysis is to determine whether transportation barriers, such as longer commute times, limited vehicle access, and lower public transit usage, are associated with higher unemployment rates.

Multiple datasets from PolicyMap were cleaned and merged using Python. The final dataset was analyzed and visualized using Microsoft Power BI to support clear, data-driven insights.

The findings suggest that transportation conditions are related to unemployment, but that socioeconomic factors such as income and poverty also play an important role.

---

## Technologies Used
- Python (pandas for data cleaning and transformation)
- Matplotlib, Seaborn, Plotly (optional visualizations)
- Microsoft Power BI (dashboard development)
- PolicyMap (data source)
- CSV files (data storage and processing)

---

## How to Reproduce the Analysis

### 1. Install Required Libraries
Run the following command in your terminal:

```bash
pip install pandas matplotlib seaborn plotly
```
### 2. Prepare Data Files
Download the following datasets from PolicyMap at the ZIP code level (2020–2024):

Unemployment Rate
- Labor Force Participation
- Median Household Income
- Poverty Rate
- Percent Bachelor’s Degree
- Commute Time
- Vehicles per Household
- Public Transit Usage
- Driving Usage

Place all CSV files in the same folder as the Python script.

### 3. Run the Data Cleaning Script
Execute the following command:

```bash
python DataCleaningModeling.py
```

This script will:

- Clean column names
- Merge all datasets
- Handle missing values
- Create a Transportation Score
- Output a file named master_dataset.csv

### 4. Load Data into Power BI
  1. Open Power BI Desktop
  2. Select Get Data → Text/CSV
  3. Choose master_dataset.csv
  4. Click Load

### 5. Explore the Dashboard
Use filters and slicers to:

- Compare unemployment rates across ZIP codes
- Analyze transportation variables
- Evaluate socioeconomic influences


## File Structure
```
Capstone_Project/
├── datasets/
│ ├── employment_data.csv
│ ├── labor_force.csv
│ ├── master_dataset.csv
│ ├── socioeconomic_data.csv
│ ├── transportation_core.csv
│ ├── transportation_mode.csv
│ └── unemployment.csv
│
├── documentation/
│ └── Final Capstone Full Report Nims.pdf
│
├── scripts/
│ ├── DataCleaningModeling.py
│ └── Visualizations.py
│
├── visualizations/
│ ├── CapstoneReport.pbix
│ ├── commute_vs_unemployment.png
│ ├── income_vs_unemployment.png
│ ├── interactive_commute_plot.html
│ ├── score_vs_unemployment.png
│ ├── transit_vs_unemployment.png
│ └── unemployment_distribution.png
│
└── README.md
```

## Author Name
Monica Nims

## Notes
- Data is aggregated at the ZIP code level
- Results are based on observational data and do not imply causation
- This project was completed as part of a capstone analysis
