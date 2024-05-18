
# 🚗 CO2 Emissions Analyzer 📊

This application analyzes CO2 emissions data from vehicles and provides visualizations as well as a predictive model to estimate CO2 emissions based on vehicle specifications.

## 🛠️ Tools Used

- Streamlit for creating the interactive web application.
- Matplotlib and Seaborn for data visualization.
- Pandas and NumPy for data manipulation.
- SciPy for statistical analysis.
- Scikit-learn for machine learning model implementation (Random Forest Regressor).

## 📊 Data Visualization

The application offers various visualizations including bar charts of car brands, car models, vehicle classes, engine sizes, cylinders, transmissions, and fuel types. Additionally, it provides box plots to identify outliers in the dataset.

## 🤖 CO2 Emission Prediction Model

Users can input vehicle specifications such as engine size, cylinders, and fuel consumption, and the application predicts the CO2 emissions using a Random Forest Regression model trained on the dataset.

## 🚀 Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/your_project.git
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

## 📋 Project Structure

- `app.py`: Main application script.
- `co2 Emissions.csv`: Dataset containing CO2 emissions data.
- `README.md`: This file.

## 📈 Example Visualizations

![Car Brands](screenshots/car_brands.png)
![Engine Sizes](screenshots/engine_sizes.png)
![CO2 Emissions vs. Vehicle Class](screenshots/co2_vs_vehicle_class.png)

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 🙏 Acknowledgements

Special thanks to the developers of Streamlit, Matplotlib, Seaborn, Pandas, NumPy, SciPy, and Scikit-learn for their amazing tools!
