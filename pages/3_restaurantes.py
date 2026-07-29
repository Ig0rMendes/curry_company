import streamlit as st
from streamlit_folium import folium_static
from data.loader import load_data
from processing.cleaning import clean_data
from features.filters import apply_filters
from features.resources import create_restaurant_id
from metrics.restaurantes import restaurantes_kpis
from metrics.restaurantes import HeatMap
from features.resources import filter_valid_restaurants
from features.resources import pct_invalid_locations


from visuals.restaurantes_plots import (
    top_restaurantes_pedidos,
    top_restaurantes_rapidos,
    tempo_por_trafego,    
    heatmap_restaurantes
)

st.set_page_config(layout="wide")

# Carregar dados
df = load_data('data/train.csv')
df = clean_data(df)

# Sidebar
st.sidebar.title("🍽️ Restaurantes")

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
df = create_restaurant_id(df)

#Cabeçalho
st.title("🍽️ Visão Restaurantes")

# Metricas

kpis = restaurantes_kpis(df)

col1, col2, col3 = st.columns(3)

col1.metric("Restaurantes", kpis["total_restaurantes"])
col2.metric("Pedidos", kpis["total_pedidos"])
col3.metric("Tempo médio", kpis["tempo_medio"])

# Graficos
df_valid = filter_valid_restaurants(df)
st.plotly_chart(tempo_por_trafego(df), use_container_width=True)
df_valid = filter_valid_restaurants(df)
col1, col2 = st.columns(2)
col1.plotly_chart(top_restaurantes_rapidos(df), use_container_width=True)
col2.plotly_chart(top_restaurantes_pedidos(df_valid), use_container_width=True)
st.warning("⚠️ Restaurantes com localização inválida foram removidos desta análise. Como não existem registros dos restaurantes únicos, foi criado o 'Restaurant_ID' utilizando a combinação de Cidade + Latitude + Longitude")

st.markdown(
    "<h3 style='text-align: center;'>Distribuição Geográfica da Demanda (Mapa de Calor)</h3>",
    unsafe_allow_html=True
)
# MÉTRICA
df_heat = HeatMap(df_valid)

# PLOT
mapa = heatmap_restaurantes(df_heat)

# RENDER
from streamlit_folium import st_folium
mapa = heatmap_restaurantes(df_heat)
st_folium(mapa, use_container_width=True)

# Insigths
invalid_pct = pct_invalid_locations(df)
st.markdown(f"""
### ⚠️ Qualidade dos dados

🔎 **{invalid_pct:.1f}% dos restaurantes não possuem localização válida**
Esses dados foram removidos das análises que dependem de localização para evitar distorções nos resultados.
""")
st.markdown(f"""
### 🧠 Insigths
""")
st.markdown("""
O tempo médio de preparo dos pedidos é de aproximadamente 10 minutos, indicando um processo interno eficiente e bem estruturado. Esse resultado sugere que a operação dentro dos restaurantes não é o principal fator de atraso na entrega.

Em contrapartida, o tempo de entrega é significativamente impactado pelas condições de tráfego. Em cenários de tráfego leve, o tempo médio é de 21,35 minutos, enquanto em situações de congestionamento intenso esse valor sobe para 31,02 minutos, representando um aumento de aproximadamente 45,29%. Esse comportamento evidencia que fatores externos, como festivais, são determinantes na performance logística.

A análise do mapa de calor mostra uma concentração clara de pedidos nas regiões oeste, sul e parte do centro da Índia, indicando áreas com alta demanda e maior intensidade operacional. Essas regiões tendem a exigir maior eficiência na alocação de entregadores e otimização de rotas. Por outro lado, áreas com menor densidade de pedidos podem representar oportunidades de expansão ou indicar menor penetração do serviço.

De forma geral, os dados sugerem que, embora o preparo esteja sob controle, ganhos relevantes de performance podem ser obtidos com melhorias na logística de entrega, especialmente em regiões de alta demanda e sob condições adversas de tráfego.
""")