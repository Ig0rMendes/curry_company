import streamlit as st
import pandas as pd

from data.loader import load_data
from processing.cleaning import clean_data
from features.filters import apply_filters
from metrics.empresa import executive_view 
# =========================
# Carregar dados
# =========================
df = load_data('data/train.csv')
df = clean_data(df)

# =========================
# Sidebar
# =========================
st.sidebar.title("📊 Empresa")

date_range = st.sidebar.date_input(
    "Período",
    value=(df['Order_Date'].min(), df['Order_Date'].max())
)

traffic = st.sidebar.multiselect(
    "Trânsito",
    df['Road_traffic_density'].unique(),
    default=df['Road_traffic_density'].unique()
)

weather = st.sidebar.multiselect(
    "Clima",
    df['Weatherconditions'].unique(),
    default=df['Weatherconditions'].unique()
)

# =========================
# Filtros
# =========================
df = apply_filters(df, date_range, traffic, weather)

# =========================
# Chamada das métricas da empresa
# =========================
(
    total_orders,
    total_delivery,
    total_restaurants,
    avg_delivery_time,
    avg_rating,
    avg_preparation_time
) = executive_view(df)

# =========================
# LAYOUT
# =========================
st.title("📊 Visão Empresarial")
st.markdown("### Principais indicadores do negócio")

with st.container():
    col1, col2, col3 = st.columns(3)

    col1.metric("📦 Pedidos", f"{total_orders:,}")
    col2.metric("🛵 Entregadores", f"{total_delivery:,}")
    col3.metric("🍽 Restaurantes", f"{total_restaurants:,}")

with st.container():
    col1, col2, col3 = st.columns(3)

    col1.metric(
        "⏱ Tempo Médio de Entrega",
        f"{avg_delivery_time:.2f} min"
    )

    col2.metric(
        "⭐ Rating Médio",
        f"{avg_rating:.2f}"
    )

    col3.metric(
        "👨‍🍳 Tempo Médio de Preparo",
        f"{avg_preparation_time:.2f} min"
    )

st.markdown("---")

# =========================
# Insigts
# =========================
st.markdown("""
### 💡 Insight Executivo

- O tempo médio de entrega reflete a eficiência operacional da plataforma  
- O rating médio indica a qualidade percebida pelos clientes  
- O tempo de preparo impacta diretamente o tempo total de entrega  

Esses indicadores são fundamentais para decisões estratégicas como:
- Otimização logística  
- Avaliação de performance dos entregadores  
- Gestão de restaurantes parceiros  
""")