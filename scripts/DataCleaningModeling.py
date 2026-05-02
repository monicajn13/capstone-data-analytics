import pandas as pd

# -----------------------------
# 1. Load CSV files
# -----------------------------
labor_force = pd.read_csv("labor_force.csv")
socioeconomic = pd.read_csv("socioeconomic_data.csv")
transport_core = pd.read_csv("transportation_core.csv")
transport_mode = pd.read_csv("transportation_mode.csv")
unemployment = pd.read_csv("unemployment.csv")

# -----------------------------
# 2. Clean column names
# -----------------------------
def clean_columns(df):
    df.columns = df.columns.str.strip().str.replace(" ", "_").str.replace("%", "Percent")
    return df

labor_force = clean_columns(labor_force)
socioeconomic = clean_columns(socioeconomic)
transport_core = clean_columns(transport_core)
transport_mode = clean_columns(transport_mode)
unemployment = clean_columns(unemployment)

# -----------------------------
# 3. Create and standardize ZIP column
# -----------------------------
def create_zip_column(df):
    if "ZIP" in df.columns:
        zip_col = "ZIP"
    elif "GeoID_Name" in df.columns:
        zip_col = "GeoID_Name"
    elif "GeoID_Name_1" in df.columns:
        zip_col = "GeoID_Name_1"
    elif "Location" in df.columns:
        zip_col = "Location"
    else:
        print(df.columns)
        raise KeyError("No ZIP, GeoID_Name, GeoID_Name_1, or Location column found.")

    df["ZIP"] = (
        df[zip_col]
        .astype(str)
        .str.replace(".0", "", regex=False)
        .str.strip()
    )

    return df


labor_force = create_zip_column(labor_force)
socioeconomic = create_zip_column(socioeconomic)
transport_core = create_zip_column(transport_core)
transport_mode = create_zip_column(transport_mode)
unemployment = create_zip_column(unemployment)

# -----------------------------
# 4. Select and rename needed columns
# -----------------------------

# Unemployment
unemployment = unemployment[["ZIP", "pcivunemp"]]
unemployment = unemployment.rename(columns={
    "pcivunemp": "Unemployment_Rate"
})

# Labor force
labor_force = labor_force[["ZIP", "plaborforce"]]
labor_force = labor_force.rename(columns={
    "plaborforce": "Labor_Force"
})

# Socioeconomic
socioeconomic = socioeconomic[[
    "ZIP",
    "mhhinc_20202024",
    "ppov_20202024",
    "pbach_20202024"
]].rename(columns={
    "mhhinc_20202024": "Median_Income",
    "ppov_20202024": "Poverty_Rate",
    "pbach_20202024": "Percent_Bachelors"
})

# Transportation core
transport_core = transport_core[[
    "ZIP",
    "avtt_20202024",  # commute time
    "avmv_20202024"   # vehicles per household
]].rename(columns={
    "avtt_20202024": "Commute_Time",
    "avmv_20202024": "Vehicles_per_Household"
})

# Transportation mode
transport_mode = transport_mode[[
    "ZIP",
    "ptranpt_20202024",
    "ptranmv_20202024"
]].rename(columns={
    "ptranpt_20202024": "Percent_Public_Transit",
    "ptranmv_20202024": "Percent_Driving"
})

# -----------------------------
# 5. Merge datasets
# -----------------------------
df = unemployment.merge(labor_force, on="ZIP", how="left")
df = df.merge(socioeconomic, on="ZIP", how="left")
df = df.merge(transport_core, on="ZIP", how="left")
df = df.merge(transport_mode, on="ZIP", how="left")

df = df.groupby("ZIP", as_index=False).mean(numeric_only=True)

# -----------------------------
# 6. Handle missing values
# -----------------------------
# Drop rows with missing key variables
df = df.dropna(subset=["Unemployment_Rate", "Commute_Time"])

# Optional: fill remaining missing values
df = df.fillna(df.mean(numeric_only=True))

# -----------------------------
# 7. Create Transportation Score
# -----------------------------
# Normalize variables (min-max scaling)
df["Commute_Norm"] = (df["Commute_Time"] - df["Commute_Time"].min()) / (df["Commute_Time"].max() - df["Commute_Time"].min())
df["Vehicles_Norm"] = (df["Vehicles_per_Household"] - df["Vehicles_per_Household"].min()) / (df["Vehicles_per_Household"].max() - df["Vehicles_per_Household"].min())
df["Transit_Norm"] = (df["Percent_Public_Transit"] - df["Percent_Public_Transit"].min()) / (df["Percent_Public_Transit"].max() - df["Percent_Public_Transit"].min())

# Create score (higher = worse transportation access)
df["Transportation_Score"] = (
    df["Commute_Norm"] +
    (1 - df["Vehicles_Norm"]) +  # fewer vehicles = worse
    (1 - df["Transit_Norm"])     # less transit = worse
)

# -----------------------------
# 8. Final cleanup
# -----------------------------
# Keep only final columns
final_df = df[[
    "ZIP",
    "Unemployment_Rate",
    "Labor_Force",
    "Median_Income",
    "Poverty_Rate",
    "Percent_Bachelors",
    "Commute_Time",
    "Vehicles_per_Household",
    "Percent_Public_Transit",
    "Percent_Driving",
    "Transportation_Score"
]]

# -----------------------------
# 9. Save final dataset
# -----------------------------
final_df.to_csv("master_dataset.csv", index=False)