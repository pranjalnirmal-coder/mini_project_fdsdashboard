import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- BACKEND SETUP ---
# Load data
df = pd.read_csv("ScreevsmentalH.csv")

# Page configuration
st.set_page_config(page_title="Screen Time vs Mental Wellness Survey Data Analysis", layout="wide")

# Seaborn style
sns.set(style="whitegrid", palette="muted", font_scale=1.1)

# --- FRONTEND ---
st.title("Screen Time vs Mental Wellness Survey Data Analysis")
st.markdown("### Visual Analysis of Stress, Sleep, and Screen Habits")

# --- SIDEBAR ---
st.sidebar.header("Visualization Controls")

# ✅ Gender Filter
gender_options = ["All"] + list(df["gender"].dropna().unique())
selected_gender = st.sidebar.selectbox("Select Gender", gender_options)

# Filter dataframe based on selection
if selected_gender != "All":
    filtered_df = df[df["gender"] == selected_gender]
else:
    filtered_df = df.copy()

show_data = st.sidebar.checkbox("Show Raw Data", False)
if show_data:
    st.subheader("📋 Dataset Preview")
    st.dataframe(filtered_df, use_container_width=True, height=400)

# --- VISUALIZATIONS ---

# Line Plot
st.subheader("Stress Level vs Age")
fig1 = plt.figure(figsize=(8,5))
sns.lineplot(x='age', y='stress_level_0_10', data=filtered_df, marker='o', color='royalblue')
plt.title(f'Stress Level vs Age ({selected_gender})', fontsize=14, weight='bold')
plt.xlabel('Age')
plt.ylabel('Stress Level (0–10)')
st.pyplot(fig1)

# Bar Chart
st.subheader("Average Stress Level by Occupation")
fig2 = plt.figure(figsize=(8,5))
sns.barplot(x='occupation', y='stress_level_0_10', data=filtered_df, estimator='mean', ci=None, palette='coolwarm')
plt.title(f'Average Stress Level by Occupation ({selected_gender})', fontsize=14, weight='bold')
plt.xlabel('Occupation')
plt.ylabel('Average Stress Level (0–10)')
st.pyplot(fig2)

# Box Plot
st.subheader("Sleep Hours by Occupation")
fig3 = plt.figure(figsize=(8,5))
sns.boxplot(x='occupation', y='sleep_hours', data=filtered_df, palette='pastel')
plt.title(f'Sleep Hours by Occupation ({selected_gender})', fontsize=14, weight='bold')
plt.xlabel('Occupation')
plt.ylabel('Sleep Hours')
st.pyplot(fig3)

# Pie Chart
st.subheader("Sleep Quality Distribution (1–5)")
fig4 = plt.figure(figsize=(7,7))
sleep_quality_counts = filtered_df['sleep_quality_1_5'].value_counts().sort_index()
colors = sns.color_palette('pastel')[0:5]
plt.pie(sleep_quality_counts,
        labels=[f'Quality {i}' for i in sleep_quality_counts.index],
        autopct='%1.1f%%',
        startangle=140,
        colors=colors,
        textprops={'fontsize': 11})
plt.title(f'Sleep Quality Distribution (1–5) ({selected_gender})', fontsize=14, weight='bold')
st.pyplot(fig4)

# Scatter Plot
st.subheader("Screen Time vs Mental Wellness Index")
fig5 = plt.figure(figsize=(8,5))
sns.scatterplot(x='screen_time_hours', y='mental_wellness_index_0_100', data=filtered_df, color='seagreen', s=70, alpha=0.7)
plt.title(f'Screen Time vs Mental Wellness Index ({selected_gender})', fontsize=14, weight='bold')
plt.xlabel('Screen Time (hours)')
plt.ylabel('Mental Wellness Index (0–100)')
st.pyplot(fig5)

# Histogram
st.subheader("Distribution of Sleep Hours")
fig6 = plt.figure(figsize=(8,5))
sns.histplot(filtered_df['sleep_hours'], bins=10, kde=True, color='mediumorchid')
plt.title(f'Distribution of Sleep Hours ({selected_gender})', fontsize=14, weight='bold')
plt.xlabel('Sleep Hours')
plt.ylabel('Frequency')
st.pyplot(fig6)

# Footer
st.markdown("---")
st.markdown("Developed by **Pranjal Nirmal** 💻")
