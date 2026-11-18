DATA_PATH = "/PATH/TO/health-analytics-hpc/data/synthetic_health_data.csv"   # Edit to match filepath of data file (csv)

import pandas as pd
import statsmodels.formula.api as smf

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

df = pd.read_csv(DATA_PATH)

print("Rows, columns:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nSummary statistics:")
print(df.describe().round(2))

print("\nMean systolic BP by sex:")
print(df.groupby("sex")["systolic_bp"].mean().round(1))
print("\nMean systolic BP by smoking status:")
print(df.groupby("smoker")["systolic_bp"].mean().round(1))
print("\nHypertension prevalence by county:")
print(df.groupby("county")["hypertension"].mean().round(3))

print("\nCorrelations with systolic BP:")
print(df[["age", "bmi", "physical_activity_hrs_week", "cholesterol", "systolic_bp"]].corr()["systolic_bp"].round(3))

model = smf.ols("systolic_bp ~ age + bmi + C(sex) + C(smoker) + physical_activity_hrs_week", data=df).fit()
print("\n", model.summary())

print("\nResidual summary:")
print(model.resid.describe().round(2))
print("\nDone.")
