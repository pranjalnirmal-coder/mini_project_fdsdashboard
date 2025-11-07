import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- BACKEND SETUP ---
# Load data
df = pd.read_csv("ScreevsmentalH.csv")

# Page configuration
st.set_page_config(page_title="Mental Health Data Visualizer", layout="wide")

# Seaborn style
sns.set(style="whitegrid", palette="muted", font_scale=1.1)

# --- FRONTEND ---
st.title("Mental Health & Lifestyle Dashboard")
st.markdown("### Visual Analysis of Stress, Sleep, and Screen Habits")

# Sidebar
st.sidebar.header("Visualization Controls")
show_data = st.sidebar.checkbox("Show Raw Data", False)
if show_data:
    st.subheader("📋 Dataset Preview")
    st.dataframe(df, use_container_width=True, height=400)  # ✅ Full-width scrollable table

# Line Plot
st.subheader("Stress Level vs Age")
fig1 = plt.figure(figsize=(8,5))
sns.lineplot(x='age', y='stress_level_0_10', data=df, marker='o', color='royalblue')
plt.title('Stress Level vs Age', fontsize=14, weight='bold')
plt.xlabel('Age')
plt.ylabel('Stress Level (0–10)')
st.pyplot(fig1)

# Bar Chart
st.subheader("Average Stress Level by Occupation")
fig2 = plt.figure(figsize=(8,5))
sns.barplot(x='occupation', y='stress_level_0_10', data=df, estimator='mean', ci=None, palette='coolwarm')
plt.title('Average Stress Level by Occupation', fontsize=14, weight='bold')
plt.xlabel('Occupation')
plt.ylabel('Average Stress Level (0–10)')
st.pyplot(fig2)

# Box Plot
st.subheader("Sleep Hours by Occupation")
fig3 = plt.figure(figsize=(8,5))
sns.boxplot(x='occupation', y='sleep_hours', data=df, palette='pastel')
plt.title('Sleep Hours by Occupation', fontsize=14, weight='bold')
plt.xlabel('Occupation')
plt.ylabel('Sleep Hours')
st.pyplot(fig3)

# Pie Chart
st.subheader("Sleep Quality Distribution (1–5)")
fig4 = plt.figure(figsize=(7,7))
sleep_quality_counts = df['sleep_quality_1_5'].value_counts().sort_index()
colors = sns.color_palette('pastel')[0:5]
plt.pie(sleep_quality_counts,
        labels=[f'Quality {i}' for i in sleep_quality_counts.index],
        autopct='%1.1f%%',
        startangle=140,
        colors=colors,
        textprops={'fontsize': 11})
plt.title('Sleep Quality Distribution (1–5)', fontsize=14, weight='bold')
st.pyplot(fig4)

# Scatter Plot
st.subheader("Screen Time vs Mental Wellness Index")
fig5 = plt.figure(figsize=(8,5))
sns.scatterplot(x='screen_time_hours', y='mental_wellness_index_0_100', data=df, color='seagreen', s=70, alpha=0.7)
plt.title('Screen Time vs Mental Wellness Index', fontsize=14, weight='bold')
plt.xlabel('Screen Time (hours)')
plt.ylabel('Mental Wellness Index (0–100)')
st.pyplot(fig5)

# Histogram
st.subheader("Distribution of Sleep Hours")
fig6 = plt.figure(figsize=(8,5))
sns.histplot(df['sleep_hours'], bins=10, kde=True, color='mediumorchid')
plt.title('Distribution of Sleep Hours', fontsize=14, weight='bold')
plt.xlabel('Sleep Hours')
plt.ylabel('Frequency')
st.pyplot(fig6)

# Footer
st.markdown("---")
