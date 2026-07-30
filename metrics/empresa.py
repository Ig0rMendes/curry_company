import streamlit as st
import pandas as pd
from features.resources import (create_restaurant_id,
                                calculate_preparation_time
                                )
def executive_view(df: pd.DataFrame):
    """
    Render executive dashboard with key business metrics.
    """
    # =========================
    # 📦 MÉTRICAS
    # =========================
    total_orders = df.shape[0]

    total_delivery = df['Delivery_person_ID'].nunique()

    df1 = df.copy()
    df1 = create_restaurant_id(df1)
    total_restaurants = df1['Restaurant_ID'].nunique()

    avg_delivery_time = df['Time_taken(min)'].mean()

    avg_rating = df['Delivery_person_Ratings'].mean()

    df1 = df.copy()
    df1 = calculate_preparation_time(df1)
    avg_preparation_time = df1['Preparation_time'].mean()
    
    return (
        total_orders,
        total_delivery,
        total_restaurants,
        avg_delivery_time,
        avg_rating,
        avg_preparation_time
        )