# =========================
# Imports and Configuration
# =========================
import os
import streamlit as st
import pandas as pd
import plotly.express as px
import base64

# =========================

import streamlit as st
import base64

def set_bg_video_centered(video_file, video_opacity=0.5, width="100vw", height="85vh", border_radius="24px"):
    with open(video_file, "rb") as video:
        video_bytes = video.read()
    video_base64 = base64.b64encode(video_bytes).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            position: relative;
            min-height: 100vh;
        }}
        #bgvid {{
            position: fixed;
            top: 50%;
            left: 50%;
            width: {width};
            height: {height};
            transform: translate(-50%, -50%);
            object-fit: cover;
            z-index: -1;
            opacity: {video_opacity};
            border-radius: {border_radius};
            box-shadow: 0 8px 32px 0 rgba(50, 50, 93, 0.15);
        }}
        .block-container {{
            position: relative;
            z-index: 1;
            background: transparent !important;
        }}
        </style>
        <video autoplay loop muted id="bgvid">
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        </video>
        """,
        unsafe_allow_html=True
    )

# Usage: adjust width, height, and opacity as needed
set_bg_video_centered("v2.mp4", video_opacity=0.8, width="100vw", height="100vh")

# =========================
# Set Streamlit page configuration
st.set_page_config(page_title="Crocodile Dashboard", layout="wide")

# =========================
# Data Loading
# =========================
@st.cache_data
def load_data():
    """Load the crocodile dataset with date parsing."""
    df = pd.read_csv("crocodile_dataset.csv", parse_dates=['Date of Observation'], dayfirst=True)
    return df

df = load_data()

# =========================
# Footer Function
# =========================
def footer():
    """Display a fixed footer at the bottom right."""
    st.markdown(
        """
        <div style='position: fixed; right: 10px; bottom: 10px; color: #0000; font-size: 16px;'>
            @ All Rights Reserved to VUYYALA HIMACHAND.
        </div>
        """, unsafe_allow_html=True
    )

# =========================
# Home Page
# =========================
def main_page():
    """Display the main dashboard overview and top images."""
    st.markdown(
        "<h1 style='color:#000000;text-align:center;font-size:42px;'>Crocodile Conservation Insights: Global Field Observations Dashboard</h1>",
        unsafe_allow_html=True
    )
    st.write("---")
    # Metrics with half-transparent background
    st.markdown(
        f"""
        <div style='background:rgba(255,255,255,0.8);padding:18px 0 8px 0;border-radius:12px;margin-bottom:10px;'>
        <div style='display:flex;justify-content:space-around;'>
            <div style='text-align:center;'><b>Total Observations</b><br>{len(df)}</div>
            <div style='text-align:center;'><b>Unique Species</b><br>{df['Common Name'].nunique()}</div>
            <div style='text-align:center;'><b>Countries/Regions</b><br>{df['Country/Region'].nunique()}</div>
            <div style='text-align:center;'><b>Avg. Length (m)</b><br>{df['Observed Length (m)'].mean():.2f}</div>
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write("---")
    # Filters with half-transparent background
    st.markdown("<div style='background:rgba(255,255,255,0.8);padding:16px 8px 8px 8px;border-radius:12px;'>", unsafe_allow_html=True)
    with st.form(key="filters_form"):
        col1, col2, col3 = st.columns(3)
        country = col1.multiselect("Country/Region", options=df['Country/Region'].unique(), default=df['Country/Region'].unique())
        age_class = col2.multiselect("Age Class", options=df['Age Class'].unique(), default=df['Age Class'].unique())
        sex = col3.multiselect("Sex", options=df['Sex'].unique(), default=df['Sex'].unique())
        submit = st.form_submit_button("Apply Filters")
    st.markdown("</div>", unsafe_allow_html=True)
    filtered_df = df[
        df['Country/Region'].isin(country) &
        df['Age Class'].isin(age_class) &
        df['Sex'].isin(sex)
    ]
    # Filtered data table with half-transparent background
    st.markdown("<div style='background:rgba(255,255,255,0.8);padding:12px 8px 8px 8px;border-radius:12px;'>", unsafe_allow_html=True)
    st.success(f"Showing {len(filtered_df)} filtered observations.")
    st.dataframe(filtered_df.head(10))
    st.markdown("</div>", unsafe_allow_html=True)
    
 # --- Place images at the bottom in 2 rows ---
    st.write("---")
    st.markdown("<h4 style='text-align:center;'>Top 5 Crocodiles</h4>", unsafe_allow_html=True)
    images_and_captions = [
        ("c1.png", "New Guinea crocodile"),
        ("c2.png", "Borneo crocodile"),
        ("c3.jpg", "American Crocodile"),
        ("c4.jpg", "Cuban Crocodile"),
        ("c5.jpg", "Morelet's Crocodile"),
        ("c6.jpg", "orinoco crocodile")]
    # First row: 3 images
    cols1 = st.columns(3)
    for i in range(3):
        img_file, caption = images_and_captions[i]
        with cols1[i]:
            if os.path.exists(img_file):
                st.image(img_file, use_container_width=True)
                st.markdown(f"<div style='text-align:center; font-size:24px; color:#000000; margin-top:8px;'>{caption}</div>",unsafe_allow_html=True)

            else:
                st.write(f"No image: {caption}")
    # Second row: 2 images
    cols2 = st.columns(3)
    for i in range(3, 6):
        img_file, caption = images_and_captions[i]
        with cols2[i-3]:
            if os.path.exists(img_file):
                st.image(img_file, use_container_width=True)
                st.markdown(f"<div style='text-align:center; font-size:24px; color:#000000; margin-top:8px;'>{caption}</div>",unsafe_allow_html=True)
            else:
                st.write(f"No image: {caption}")
                st.markdown("<div style='height: 400px;'></div>", unsafe_allow_html=True)
footer()

# =========================
# Chart Pages with Summaries
# =========================

def species_distribution_page():
    """Pie chart of species distribution with summary."""
    st.markdown("<h2 style='color:#000000;'>Species Distribution</h2>", unsafe_allow_html=True)
    # Create pie chart with half-transparent background
    fig = px.pie(
        df,
        names='Common Name',
        title='Species Distribution',
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    fig.update_layout(
        paper_bgcolor='rgba(255,255,255,0.7)',
        plot_bgcolor='rgba(255,255,255,0.7)',
        margin=dict(l=20, r=20, t=40, b=20)
    )
    st.markdown("<div style='background:rgba(255,255,255,0.5);padding:18px 8px 8px 8px;border-radius:12px;'>", unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True, key="fig_species")
    st.markdown(
        """
        <div style='font-size:18px; color:#000000; margin-top:14px;'>
        <b>Summary:</b>
        <ul>
            <li>Visualizes the proportion of each crocodile species observed.</li>
            <li>Highlights the most and least commonly observed species.</li>
            <li>Helps identify species diversity in the dataset.</li>
            <li>Can guide conservation focus towards less observed species.</li>
            <li>Shows species dominance in the observed regions.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    footer()

def country_observations_page():
    """Bar chart of observations by country/region with summary."""
    st.markdown("<h2 style='color:#000000;'>Observations by Country/Region</h2>", unsafe_allow_html=True)
    country_counts = df['Country/Region'].value_counts().reset_index()
    country_counts.columns = ['Country/Region', 'Count']
    fig = px.bar(
        country_counts,
        x='Count',
        y='Country/Region',
        orientation='h',
        labels={'Country/Region':'Country/Region', 'Count':'Count'},
        color='Country/Region',
        color_discrete_sequence=px.colors.qualitative.Vivid
    )
    fig.update_layout(
        paper_bgcolor='rgba(255,255,255,0.7)',
        plot_bgcolor='rgba(255,255,255,0.7)',
        margin=dict(l=20, r=20, t=40, b=20)
    )
    st.markdown("<div style='background:rgba(255,255,255,0.5);padding:18px 8px 8px 8px;border-radius:12px;'>", unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True, key="fig_country")
    st.markdown(
        """
        <div style='font-size:18px; color:#000000; margin-top:14px;'>
        <b>Summary:</b>
        <ul>
            <li>Displays the number of crocodile observations per country or region.</li>
            <li>Highlights countries with the highest and lowest observation counts.</li>
            <li>Reveals geographic distribution patterns of crocodile sightings.</li>
            <li>Can inform regional conservation priorities.</li>
            <li>Shows data coverage and possible gaps in field observations.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)
    footer()

def habitat_observations_page():
    """Bar chart of observations by habitat type with summary."""
    st.markdown("<h2 style='color:#000000;'>Observations by Habitat Type</h2>", unsafe_allow_html=True)
    habitat_counts = df['Habitat Type'].value_counts().reset_index()
    habitat_counts.columns = ['Habitat Type', 'Count']
    fig = px.bar(
        habitat_counts,
        x='Count',
        y='Habitat Type',
        orientation='h',
        labels={'Habitat Type': 'Habitat Type', 'Count': 'Count'},
        color='Habitat Type',
        color_discrete_sequence=px.colors.qualitative.Safe
    )
    # Make background transparent and reduce margins
    fig.update_layout(
        paper_bgcolor='rgba(255,255,255,0.7)',
        plot_bgcolor='rgba(255,255,255,0.7)',
        margin=dict(l=20, r=20, t=40, b=20)
    )
    st.plotly_chart(fig, use_container_width=True, key="fig_habitat")
    st.markdown(
        """
        <div style='font-size:18px; color:#000000; margin-top:14px;'>
        <b>Summary:</b>
        <ul>
            <li>Shows the distribution of crocodile observations across different habitat types.</li>
            <li>Highlights the most and least common habitats for crocodiles in the dataset.</li>
            <li>Helps understand habitat preferences and ecological requirements.</li>
            <li>Can guide habitat-focused conservation efforts.</li>
            <li>Reveals potential threats to specific habitats.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True
    )
    footer()

def length_weight_page():
    """Scatter plot of length vs weight by sex with summary."""
    st.markdown("<h2 style='color:#000000;'>Length vs Weight by Sex</h2>", unsafe_allow_html=True)
    fig = px.scatter(
        df,
        x='Observed Length (m)',
        y='Observed Weight (kg)',
        color='Sex',
        hover_data=['Common Name'],
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig.update_layout(
        paper_bgcolor='rgba(255,255,255,0.7)',
        plot_bgcolor='rgba(255,255,255,0.7)',
        margin=dict(l=20, r=20, t=40, b=20)
    )
    st.markdown("<div style='background:rgba(255,255,255,0.5);padding:18px 8px 8px 8px;border-radius:12px;'>", unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True, key="fig_length_weight")
    st.markdown(
        """
        <div style='font-size:18px; color:#000000; margin-top:14px;'>
        <b>Summary:</b>
        <ul>
            <li>Displays the relationship between observed length and weight of crocodiles.</li>
            <li>Points are colored by sex for comparison.</li>
            <li>Helps identify growth patterns and sexual dimorphism.</li>
            <li>Outliers may indicate data entry errors or unique individuals.</li>
            <li>Useful for biological and ecological studies.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)
    footer()

def observations_over_time_page():
    """Line chart of observations over time with summary."""
    st.markdown("<h2 style='color:#000000;'>Time-Series Data</h2>", unsafe_allow_html=True)
    df_time = df.groupby(df['Date of Observation'].dt.to_period('M')).size().reset_index(name='Count')
    df_time['Date of Observation'] = df_time['Date of Observation'].astype(str)
    fig = px.line(df_time, x='Date of Observation', y='Count', markers=True, color_discrete_sequence=['#229954'])
    st.plotly_chart(fig, use_container_width=True, key="fig_time")
    st.markdown(
        """
        <div style='font-size:18px; color:#000000; margin-top:14px;'>
        <b>Summary:</b>
        <ul>
            <li>Shows the trend of crocodile observations over time.</li>
            <li>Helps identify seasonal or annual patterns in data collection.</li>
            <li>Can reveal periods of increased or decreased field activity.</li>
            <li>Useful for planning future surveys and monitoring efforts.</li>
            <li>Highlights data consistency and possible gaps in time series.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    footer()

# =========================
# Summary Page
# =========================
def summary_page():
    """Summary and insights page with image and thank you message."""
    st.markdown("<h2 style='color:#000000;'>Summary & Insights</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])  # Left column for text, right column for image
    with col1:
        st.markdown(
            """
            <div style='font-size:22px; color:#000000;line-height:2.5;'>
            <ul>
                <li>The dataset contains detailed observations of crocodiles across multiple countries and habitats.</li>
                <li>Most observations are concentrated in a few countries, with a diverse range of species and age classes.</li>
                <li>The average observed length and weight are calculated and displayed.</li>
                <li>Conservation status analysis highlights the need for focused protection efforts for certain species.</li>
                <li>The dashboard enables filtering and visualization for deeper exploration and understanding.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True
        )
    with col2:
        
        st.markdown(
            "<div style='text-align:center; font-size:22px; color:#000000;'><b>DIGITAL MONK</b></div>",unsafe_allow_html=True)
    
    st.markdown("<h4 style='text-align:center;font-size:22px;color:#000000;'>VUYYALA HIMACHAND | Roll No: 321020 | Class: V Pharm. D  | Date: 19-09-2025</h4>", unsafe_allow_html=True)
    
    st.markdown("<div style='text-align:center; font-size:36px; color:#000000;'><b>THANK YOU! </b></div>", unsafe_allow_html=True)

    footer()

# =========================
# Page Navigation
# =========================

PAGES = {
    "Home": main_page,
    "Species Distribution": species_distribution_page,
    "Country Observations": country_observations_page,
    "Habitat Observations": habitat_observations_page,
    "Length vs Weight": length_weight_page,
    "Time-Series Data": observations_over_time_page,
    "Summary": summary_page
}

# Set default page if not already set
if "page" not in st.session_state or st.session_state.page not in PAGES:
    st.session_state.page = list(PAGES.keys())[0]

# --- Navigation Bar (add this block here) ---
st.write("---")
nav_pages = list(PAGES.keys())
nav_cols = st.columns(len(nav_pages), gap="large")  # gap="large" adds spacing

for i, page_name in enumerate(nav_pages):
    if nav_cols[i].button(page_name, use_container_width=True):
        st.session_state.page = page_name

# --- Call the selected page function ---
PAGES[st.session_state.page]()
