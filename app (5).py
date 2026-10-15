import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="NumPy Statistical Analysis", page_icon="📊", layout="centered")
st.title("📊 NumPy Statistical Analysis")
st.caption("Upload a CSV or use the sample student dataset, then explore key statistics.")

# ---------- Load data ----------
uploaded = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded is not None:
    df = pd.read_csv(uploaded)
else:
    rng = np.random.default_rng(42)
    scores = np.clip(rng.normal(68, 12, 100), 0, 100).round(1)
    scores[:3] = [12.0, 15.0, 99.5]  # a few unusual values
    df = pd.DataFrame({
        "student_id": np.arange(1, 101),
        "math_score": scores,
        "hours_studied": np.clip(rng.normal(5, 2, 100), 0, 12).round(1),
    })

numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
if not numeric_cols:
    st.error("No numeric columns found in this dataset.")
    st.stop()

col = st.selectbox("Choose a numeric column", numeric_cols, index=min(1, len(numeric_cols) - 1))
data = df[col].dropna().to_numpy(dtype=float)

# ---------- Statistics ----------
mean, median, std = np.mean(data), np.median(data), np.std(data)
c1, c2, c3 = st.columns(3)
c1.metric("Mean", f"{mean:.2f}")
c2.metric("Median", f"{median:.2f}")
c3.metric("Std Dev", f"{std:.2f}")
c4, c5, c6 = st.columns(3)
c4.metric("Min", f"{np.min(data):.2f}")
c5.metric("Max", f"{np.max(data):.2f}")
c6.metric("Count", f"{data.size}")

# ---------- Observations ----------
st.subheader("Observations")
if abs(mean - median) > 0.1 * std:
    side = "right" if mean > median else "left"
    st.write(f"• Mean and median differ noticeably, so the data is skewed to the **{side}**.")
else:
    st.write("• Mean and median are close, so the data is roughly symmetric.")

q1, q3 = np.percentile(data, [25, 75])
iqr = q3 - q1
outliers = data[(data < q1 - 1.5 * iqr) | (data > q3 + 1.5 * iqr)]
st.write(f"• Found **{outliers.size}** unusually high/low values (IQR rule): {np.sort(outliers).tolist()}")
st.write(f"• Standard deviation is {std:.2f}, so most values lie within {mean - std:.2f} to {mean + std:.2f}.")

# ---------- Chart ----------
st.subheader("Distribution")
counts, edges = np.histogram(data, bins=15)
st.bar_chart(pd.DataFrame({"count": counts}, index=np.round(edges[:-1], 1)))

with st.expander("View data"):
    st.dataframe(df)
