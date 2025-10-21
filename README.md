# 🐊 Crocodile Conservation Insights: Global Field Observations Dashboard

## 🌟 Project Overview

This project presents an interactive **Crocodile Conservation Insights Dashboard**, a data visualization tool developed using **Streamlit** and **Python**. The dashboard provides a comprehensive overview and analysis of global crocodile field observation data, offering valuable insights into species distribution, population metrics, habitat preferences, and time-series trends.

The goal of this project is to aid conservation efforts by making complex field data accessible and interpretable for researchers, conservationists, and enthusiasts.

## ✨ Key Features

The dashboard is structured into several interactive pages, accessible via the navigation bar:

1.  **Home/Summary:** Displays key performance indicators (KPIs) like total observations, unique species, countries/regions covered, and the average observed length.
2.  **Species Distribution:** A pie chart showing the proportional distribution of observations across different crocodile species.
3.  **Country/Region Observations:** A bar chart visualizing the total count of observations per country/region, highlighting areas with the most and least field activity.
4.  **Habitat Observations:** A bar chart displaying the distribution of observations across various habitat types (e.g., Rivers, Swamps, Estuaries), revealing preferred ecological niches.
5.  **Length vs. Weight:** A scatter plot illustrating the relationship between observed length ($\text{m}$) and weight ($\text{kg}$), with points colored by sex. This helps in identifying growth patterns and sexual dimorphism.
6.  **Time-Series Data:** A line graph showing the count of observations over time (by date), which can reveal seasonal or annual patterns in field activity and data collection consistency.
7.  **Data Filtering:** Interactive widgets are available (e.g., Country/Region, Age Class, Sex) to filter the displayed data across all relevant sections for deep-dive analysis.

## 🛠️ Technologies Used

| Tool | Purpose |
| :--- | :--- |
| **Python** | Core programming language. |
| **Streamlit** | Framework for building and deploying the interactive web application/dashboard. |
| **Pandas** | Data manipulation and analysis. |
| **Altair / Plotly (or similar)** | Creating the interactive and responsive visualizations. |

## 🚀 Getting Started

Follow these steps to set up and run the dashboard locally.

### Prerequisites

You need to have **Python 3.8+** installed on your system.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/himachand-dev/Crocodile-dashboard]
    cd Crocodile-dashboard # Replace with your actual project directory name
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    *(Assuming your dependencies are listed in a `requirements.txt` file)*
    ```bash
    pip install -r requirements.txt
    ```
    *If you do not have a `requirements.txt`, you will need to install the libraries manually: `pip install streamlit pandas matplotlib seaborn` (or the specific libraries you used for plotting).*

### Running the Dashboard

1.  **Execute the Streamlit application:**
    *(Assuming your main application file is named `app.py`)*
    ```bash
    streamlit run app.py
    ```

2.  The application will automatically open in your default web browser at `http://localhost:8501`.

## 📂 Data

The dashboard uses a dataset containing various field observations. The data includes the following key attributes for each observation:
* `Observation ID`
* `Common Name` and `Scientific Name`
* `Observed Length (m)` and `Observed Weight (kg)`
* `Age Class` and `Sex`
* `Date of Observation`
* `Country/Region`
* `Habitat Type`

```
crocodile-conservation-insights/ # Main project directory
├── app.py                       # The single Python file containing all Streamlit code, UI logic, and data visualization setup.
├── assets/                      # A single folder for all supporting files (data and media)
│   ├── crocodile_data.csv       # The dataset containing the 1000+ crocodile observations (the source data).
│   ├── new_guinea.jpg           # Image for the Top 5 Crocodiles section
│   ├── american.jpg             # Image for the Top 5 Crocodiles section
│   ├── orinoco.jpg              # Image for the Top 5 Crocodiles section
│   └── (other_images.jpg)       # All other crocodile images used for the dashboard background and Top 5 section
└── README.md                    # Project overview and setup instructions (the file we created).
```

## 👨‍💻 Author

**[V. Himachand]**
* **Roll No:** 321020
* **Class:** V Pharm. D
* **Date:** 19-09-2025

---
***Thank You!***
