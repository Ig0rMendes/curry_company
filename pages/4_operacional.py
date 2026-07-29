import streamlit as st
import pandas as pd

from data.loader import load_data
from processing.cleaning import clean_data
from features.filters import apply_filters

from metrics.operacional import (
    orders_by_weekday,
    orders_by_city,
    delivery_time_distribution,
    delivery_time_by_city,
    delivery_time_multiple
)

from visuals.operacional_plots import (
    plot_orders_by_weekday,
    plot_orders_by_city,
    plot_delivery_time_distribution,
    plot_delivery_time_by_city,
    plot_delivery_time_multiple
)
from metrics.operacional import operational_insights

# Carregar dados
df = load_data('data/train.csv')
df = clean_data(df)

# Barra Lateral
st.sidebar.title("🔎 Operacional")

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

# Filtros
df = apply_filters(df, date_range, traffic, weather)

# Métricas da visão
df_weekday = orders_by_weekday(df)
df_city = orders_by_city(df)
df_time_city = delivery_time_by_city(df)
df_time_multiple = delivery_time_multiple(df)

# layout da pagina
st.title("🔎 Visão Operacional")

# Pedidos
st.markdown("## 📦 Volume de Pedidos")

col1, col2 = st.columns(2)

with col1:
    fig = plot_orders_by_weekday(df_weekday)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = plot_orders_by_city(df_city)
    st.plotly_chart(fig, use_container_width=True)

# Tempo
st.markdown("## ⏱ Tempo de Entrega")

col1, col2 = st.columns(2)

with col1:
    fig = plot_delivery_time_distribution(df)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = plot_delivery_time_by_city(df_time_city)
    st.plotly_chart(fig, use_container_width=True)

#  Múltiplas entregas
st.markdown("## 🚚 Eficiência por Múltiplas Entregas")

fig = plot_delivery_time_multiple(df_time_multiple)
st.plotly_chart(fig, use_container_width=True)

st.markdown("""
### Insights 🧠

Os dados de volume indicam uma demanda consistente ao longo da semana, com leves picos em dias específicos, sem queda relevante nos finais de semana. Esse comportamento sugere previsibilidade operacional e ausência de forte dependência de sazonalidade semanal. Além disso, a distribuição geográfica revela forte concentração de pedidos na região Metropolitana, consolidando-a como principal mercado. Em contraste, a região Semi-Urban apresenta participação praticamente irrelevante, o que pode indicar baixa penetração ou limitações operacionais, enquanto a região Urban mantém um nível intermediário com potencial claro de expansão.

Sob a ótica de eficiência, o tempo de entrega concentra-se majoritariamente entre 20 e 30 minutos, indicando um nível de serviço competitivo. No entanto, a presença de entregas com tempos elevados aponta para inconsistências na operação. A análise por região reforça esse cenário. A região Urban apresenta o melhor desempenho logístico, a Metropolitana mantém eficiência intermediária possivelmente impactada por tráfego, e a Semi-Urban concentra os maiores tempos de entrega, evidenciando os desafios estruturais.

De forma integrada, os dados mostram um desbalanceamento entre demanda e eficiência logística. A região Metropolitana combina alto volume com performance apenas moderada, indicando necessidade de otimização operacional. A região Urban apresenta boa eficiência, mas ainda com demanda limitada, sugerindo oportunidade de crescimento. Já a Semi-Urban reúne baixa demanda e baixa eficiência, levantando questionamentos sobre a viabilidade da operação nesse contexto.

Diante disso, as principais alavancas de negócio envolvem a otimização da operação na região de maior demanda, a expansão em áreas com eficiência comprovada e a reavaliação estratégica de regiões com baixo retorno operacional.

""")
