import streamlit as st
import pandas as pd

df = pd.read_csv(
  "https://raw.githubusercontent.com/ThuwarakeshM/PracticalML-KMeans-Election/master/voters_demo_sample.csv"
)

st.title("Interactive K-Means Clustering")

st.write("Here is the dataset used in this analysis:")

st.write(df)
