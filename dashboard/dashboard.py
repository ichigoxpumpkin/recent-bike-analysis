import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
bike_data = pd.read_csv('hour.csv')

# Main title for the Streamlit app
st.title("Bike Sharing Data Analysis")

# Generating descriptive statistics for the dataset
st.write("### Descriptive Statistics of The Data")
st.write(bike_data.describe())

# Clean the dataset by removing unnecessary columns
bike_data_clean = bike_data.drop(['instant', 'dteday'], axis=1)

# Sidebar configuration with a new layout
st.sidebar.title("📊 Bike Sharing Analysis")
st.sidebar.markdown("Welcome to the **Bike Sharing Insights Dashboard**. Use the options below to explore the data and gain insights.")

# Dataset preview section in the sidebar
st.sidebar.header("🔍 Data Exploration")
if st.sidebar.checkbox("Show Dataset Preview", value=True):
    st.write("### Preview of First 10 Rows of The Data")
    st.write(bike_data.head(10))  # Displaying the first 10 rows of the dataset

# Analysis topic selection section
st.sidebar.header("📈 Analysis Options")
selected_question = st.sidebar.radio(
    "Choose a Topic to Analyze:",
    ("Bike Rental Patterns on Weekdays vs. Weekends",
     "Impact of Temperature on Bike Rentals")
)



# Analysis for Question 1: Bike Rental Patterns on Weekdays vs. Weekends
if selected_question == "Bike Rental Patterns on Weekdays vs. Weekends":
    st.header("Bike Rental Trends on Weekdays vs. Weekends")

    # Bar plot to compare rentals on working days and weekends
    plt.figure(figsize=(10, 6))  # Adjusted size to be similar to the notebook output
    sns.barplot(x='workingday', y='cnt', data=bike_data_clean, ci=None)
    plt.title('Comparison of Bike Rentals on Workdays and Weekends')
    plt.xticks([0, 1], ['Weekend', 'Workday'])
    plt.ylabel('Number of Bike Rentals')

    st.pyplot(plt.gcf())

    # Insight derived from the notebook's findings
    st.markdown("""
    **Insight**:
    - **Working Days vs. Weekends**:
        - The bar chart shows a slight increase in the number of bike rentals on working days compared to weekends.
        - This trend suggests that bike rentals are primarily driven by commuting needs, with more users renting bikes during their daily work routines.
    - **User Type Influence**:
        - Registered users likely contribute to this higher rental count on working days, using bikes as a convenient transportation mode to and from work.
        - The relatively high rentals during weekends also indicate significant casual or leisure usage, even though it is lower compared to working days.
    """)

# Analysis for Question 2: Impact of Temperature on Bike Rentals
elif selected_question == "Impact of Temperature on Bike Rentals":
    st.header("Exploring the Impact of Temperature on Bike Rentals")

    # Scatter plot to show the relationship between temperature and rental counts
    plt.figure(figsize=(12, 7))  # Adjusted size to match the notebook style
    sns.scatterplot(x=bike_data_clean['temp'], y=bike_data_clean['cnt'])
    plt.title('Relationship Between Temperature and Number of Bike Rentals')
    plt.xlabel('Temperature (Normalized)')
    plt.ylabel('Number of Bike Rentals')

    st.pyplot(plt.gcf())

    # Insight based on the data analysis from the notebook
    st.markdown("""
    **Insight**:
    - **Positive Correlation with Temperature**:
        - The scatter plot indicates a clear positive correlation between temperature and the number of bike rentals.
        - As the temperature increases, the number of bike rentals also tends to increase, reaching a peak at moderate to warm temperatures.
    - **Optimal Temperature Range**:
        - The highest density of bike rentals occurs within a normalized temperature range of around 0.4 to 0.8, suggesting that users prefer to rent bikes when it's neither too cold nor too hot.
        - Beyond this optimal range, the number of rentals starts to decline, possibly due to extreme weather conditions being less comfortable for biking.
    """)

# Conclusion section to summarize the analysis, moved to the main content area
st.header("Summary of Findings")
st.markdown("""
**Summary**:
- **What is the trend of bike renting based on the days?**
    - **Higher Rentals on Working Days:** The data indicates that bike rentals are higher on working days compared to weekends. This suggests that a significant portion of the rentals are driven by commuters using the service for their daily travel to work or school.
    - **Weekend Rentals:** While the number of rentals is lower on weekends, it remains substantial, indicating that bikes are also used for recreational purposes during these days, likely by casual users.
    - **User Behavior:** The distinct pattern of higher rentals on weekdays points to registered users who are more consistent in their rental behavior, as they are likely using bikes as part of their daily routine.

- **What is the trend of bike rentals from the temperature?**
    - **Positive Correlation with Temperature:** There is a clear positive correlation between temperature and bike rentals. As the temperature rises to a moderate level, the number of bike rentals increases, indicating a preference for biking in warmer conditions.
    - **Optimal Temperature Range:** The highest bike rentals occur when the temperature is within a moderate range (normalized values of 0.4 to 0.8). This suggests that users are most comfortable riding when it's neither too cold nor too hot.
    - **Weather Sensitivity:** Extreme temperatures on either end of the scale tend to reduce the number of bike rentals, showing that weather conditions significantly influence user decisions to rent a bike.
""")
