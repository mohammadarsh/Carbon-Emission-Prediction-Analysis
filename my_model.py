# my_model.py

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.ensemble import RandomForestRegressor

# Function to predict CO2 emissions
def predict_co2_emissions(input_data):
    # Load the vehicle dataset
    df = pd.read_csv('co2 Emissions.csv')

    # Drop rows with natural gas as fuel type
    fuel_type_mapping = {"Z": "Premium Gasoline","X": "Regular Gasoline","D": "Diesel","E": "Ethanol(E85)","N": "Natural Gas"}
    df["Fuel Type"] = df["Fuel Type"].map(fuel_type_mapping)
    df_natural = df[~df["Fuel Type"].str.contains("Natural Gas")].reset_index(drop=True)

    # Remove outliers from the data
    df_new = df_natural[['Engine Size(L)', 'Cylinders', 'Fuel Consumption Comb (L/100 km)', 'CO2 Emissions(g/km)']]
    df_new_model = df_new[(np.abs(stats.zscore(df_new)) < 1.9).all(axis=1)]

    # Prepare the data for modeling
    X = df_new_model[['Engine Size(L)', 'Cylinders', 'Fuel Consumption Comb (L/100 km)']]
    y = df_new_model['CO2 Emissions(g/km)']

    # Train the random forest regression model
    model = RandomForestRegressor().fit(X, y)

    # Make prediction
    prediction = model.predict(input_data)

    return prediction[0]
