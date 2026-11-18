# Health Analytics HPC Exercise

Synthetic dataset (2,000 patients; no real data) for practicing a short Python analysis on an HPC cluster.

## Files
- `data/synthetic_health_data.csv` - synthetic patient data
- `run_analysis.py` - the analysis script (descriptives, correlations, linear regression; text output only)
- `run_analysis.slurm` - batch script for submitting the job
- `requirements.txt` - Python packages needed
- `generate_data.py` - instructor use only

## Columns
| column | description |
|---|---|
| patient_id | unique ID |
| age | years |
| sex | female / male |
| bmi | body mass index |
| smoker | yes / no |
| physical_activity_hrs_week | hours of physical activity per week |
| county | one of five Tampa Bay-area counties |
| cholesterol | total cholesterol (mg/dL) |
| systolic_bp | systolic blood pressure (mmHg) |
| hypertension | 1 if systolic_bp >= 130, else 0 |

## Steps
1. Clone: `git clone <REPO_URL>` then `cd health-analytics-hpc`
2. Open `run_analysis.py`; line 1 is `DATA_PATH`. Change it only if your CSV is somewhere else.
3. Run interactively: `python run_analysis.py`
   or submit: `sbatch run_analysis.slurm`
4. Read the results: they print straight to your terminal with `python run_analysis.py`. If you used `sbatch`, the same text is saved in `health_analytics_<jobid>.out`; view it with `cat health_analytics_<jobid>.out` (no file transfer needed).

## Questions to answer
1. Which predictors in the regression are statistically significant?
2. What is the estimated change in systolic BP per additional year of age?
3. Look at the residual summary and the Durbin-Watson / Jarque-Bera lines in the regression output. Is there any sign the model assumptions are violated?
