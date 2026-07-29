import streamlit as st

from data.loader import load_data
from processing.cleaning import clean_data
from features.filters import apply_filters
from features.resources import calculate_distance
from metrics.entregadores import *
from visuals.entregadores_plots import *

st.title("🛵 Avaliação de Entregadores")

# Carregar dados
df = load_data('data/train.csv')
df = clean_data(df)

# Barra lateral
st.sidebar.title("🛵 Entregadores")

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

df = apply_filters(df, date_range, traffic, weather)

# Processamento
df = calculate_distance(df)
df = calculate_efficiency(df)

df_vehicle_rating = rating_by_vehicle(df)
df_vehicle_time = time_by_vehicle(df)

df_fast = top_fast_deliverers(df)
df_slow = top_slow_deliverers(df)

df_consistency = delivery_consistency(df)

# Graficos

col1, col2 = st.columns(2)
col1.plotly_chart(plot_rating_vehicle(df_vehicle_rating), use_container_width=True)
col2.plotly_chart(plot_time_vehicle(df_vehicle_time), use_container_width=True)

col3, col4 = st.columns(2)
col3.plotly_chart(plot_top_fast(df_fast), use_container_width=True)
col4.plotly_chart(plot_top_slow(df_slow), use_container_width=True)

st.plotly_chart(plot_consistency(df_consistency), use_container_width=True)

# Insigths
fastest_vehicle, slowest_vehicle, most_consistent, least_consistent = entregadores_insights(
    df_vehicle_time, df_consistency
)

st.markdown("### 🧠 Insights")

st.write(f"A performance dos entregadores não é impactada diretamente pelo tipo de veículo em termos de avaliação, mas apresenta diferenças relevantes no tempo de entrega, indicando influência de fatores operacionais e geográficos. Existe uma clara distinção entre entregadores eficientes e ineficientes, tanto em tempo médio quanto em consistência.")
st.write(f"Entregadores mais rápidos não apenas realizam entregas em menor tempo, como também apresentam maior previsibilidade, o que é um fator crítico para a experiência do cliente. Já os entregadores mais lentos demonstram maior variabilidade, indicando possíveis gargalos operacionais.")
st.write(f"Esses resultados sugerem oportunidades de melhoria por meio de treinamentos, otimização de rotas e análise regional, além da possibilidade de replicar boas práticas dos entregadores mais eficientes para elevar o desempenho geral da operação.")
