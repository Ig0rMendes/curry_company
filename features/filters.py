import pandas as pd
import streamlit as st
import os

def sidebar_filters(df):
    st.sidebar.header("Cury Company")

    # caminho seguro da imagem (funciona local e no Streamlit Cloud)
    image_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'Logo.png')
    st.sidebar.image(image_path, width=120)

    min_date = df['Order_Date'].min().date()
    max_date = df['Order_Date'].max().date()

    start_date = st.sidebar.date_input('Data inicial', min_date)
    end_date = st.sidebar.date_input('Data final', max_date)

    traffic_options = st.sidebar.multiselect(
        'Condição de trânsito',
        ['Low', 'Medium', 'High', 'Jam'],
        default=['Low', 'Medium', 'High', 'Jam']
    )

    return start_date, end_date, traffic_options


def apply_filters(df, date_range, traffic, weather):
    start_date, end_date = date_range

    df = df[
        (df['Order_Date'] >= pd.to_datetime(start_date)) &
        (df['Order_Date'] <= pd.to_datetime(end_date))
    ]

    return df
