# 📊 NumPy Statistical Analysis

Analyze a numerical dataset (Student Performance) using NumPy statistical functions and identify important patterns such as skewness and outliers.

## Objective
Practice applying statistical functions to numerical data.

## Tools
- Python
- NumPy
- Jupyter Notebook
- Streamlit (for the deployed demo)

## Project Structure
```
├── NumPy_Statistical_Analysis.ipynb   # Main analysis notebook
├── app.py                             # Streamlit web app
├── requirements.txt                   # Dependencies
└── README.md
```

## What the Analysis Covers
- Mean, median, standard deviation, minimum, maximum
- Comparing mean vs median to detect skewness
- Detecting unusually high or low values (IQR rule and Z-score)
- Percentiles and written observations

## Run Locally
```bash
git clone https://github.com/<your-username>/numpy-statistical-analysis.git
cd numpy-statistical-analysis
pip install -r requirements.txt

# Notebook
jupyter notebook NumPy_Statistical_Analysis.ipynb

# Web app
streamlit run app.py
```

## Deploy (Streamlit Community Cloud)
1. Push this repo to GitHub.
2. Go to share.streamlit.io and click **New app**.
3. Select the repo, branch `main`, and main file `app.py`.
4. Click **Deploy**.

## Key Observations (sample dataset)
1. The mean is slightly pulled away from the median by a few extreme scores.
2. The standard deviation shows how widely scores are spread around the mean.
3. A handful of unusually low/high scores were flagged as outliers.

## Interview Questions
- **Mean vs median?** Mean is the arithmetic average; median is the middle value and is not affected by extremes.
- **When is median more useful?** When data is skewed or has outliers (e.g., salaries, house prices).
- **What does standard deviation tell us?** How spread out values are around the mean.

## Author
Swetha, AI & ML Track, Veda Technology
