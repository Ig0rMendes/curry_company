import pandas as pd
import streamlit as st
from pathlib import Path


def sidebar_filters(df):

    logo_path = Path(__file__).parent / "assets" / "logo.png"

    st.sidebar.image(logo_path, width=120)

    st.sidebar.markdown(
        "<h2 style='text-align: center;'>Cury Company</h2>",
        unsafe_allow_html=True
    )

    st.sidebar.markdown("---")

    min_date = df['Order_Date'].min().date()
    max_date = df['Order_Date'].max().date()

    start_date = st.sidebar.date_input('Data inicial', min_date)
    end_date = st.sidebar.date_input('Data final', max_date)

    traffic_options = st.sidebar.multiselect(
        'Condição de trânsito',
        ['Low', 'Medium', 'High', 'Jam'],
        default=['Low', 'Medium', 'High', 'Jam']
    )

    st.sidebar.markdown("---")

    st.sidebar.markdown(
        "<p style='text-align: center; font-size: 12px;'>Powered by Igor Mendes</p>",
        unsafe_allow_html=True
    )

    return start_date, end_date, traffic_options
