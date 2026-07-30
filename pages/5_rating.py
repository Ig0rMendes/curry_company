import streamlit as st

from data.loader import load_data
from processing.cleaning import clean_data
from features.filters import apply_filters

from metrics.rating import (
    rating_summary,
    rating_by_city,
    rating_by_weather,
    rating_by_trafic,
    rating_vs_time,
    rating_vs_age,
    rating_insights
)

from visuals.rating_plots import (
    plot_rating_vs_time,
    plot_rating_by_city,
    plot_rating_by_weather,
    plot_rating_by_trafic,
    plot_rating_vs_age
)



# Dados

df = load_data('data/train.csv')
df = clean_data(df)


# Barra LAteral
st.sidebar.title("⭐ Experiência do Cliente")

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



# Métricas

st.title("⭐ Experiência do Cliente")

avg_rating, max_rating, min_rating = rating_summary(df)

col1, col2, col3 = st.columns(3)

col1.metric("Rating Médio", f"{avg_rating:.2f}")
col2.metric("Rating Máximo", f"{max_rating:.2f}")
col3.metric("Rating Mínimo", f"{min_rating:.2f}")


#Gráficos

st.subheader("🕓 Rating vs Tempo")
st.plotly_chart(plot_rating_vs_time(rating_vs_time(df)))

st.subheader("🏙️ Rating por Cidade")
df_city = rating_by_city(df)
st.plotly_chart(plot_rating_by_city(df_city))

st.subheader("🌤 Rating por Condições Externas")
col1, col2 = st.columns(2)
with col1:
    df_weather = rating_by_weather(df)
    st.plotly_chart(plot_rating_by_weather(df_weather), use_container_width=True)

with col2:
    df_trafic = rating_by_trafic(df)
    st.plotly_chart(plot_rating_by_trafic(df_trafic), use_container_width=True)



st.subheader("👨‍🦱 Avaliações por Idade")
st.plotly_chart(plot_rating_vs_age(rating_vs_age(df)))

#Insigths
st.markdown("""
### Insights 🧠
O gráfico revela um "penhasco" na satisfação: até 30 minutos, o rating se mantém estável e alto (4,70-4,75), mas cai bruscamente para cerca de 4,35 logo após esse ponto, indicando um limite crítico de tolerância do cliente, não uma degradação gradual.
Entre 30 e 45 minutos o rating oscila sem recuperação clara, e curiosamente entregas ainda mais longas (45-50 min) apresentam notas levemente melhores — possível sinal de gestão de expectativa em atrasos maiores.
Isso reforça os 30 minutos como o verdadeiro SLA-alvo da operação, sendo o ponto mais crítico a ser monitorado para evitar quedas bruscas na satisfação.

Já quando se observa região, clima e trânsito, o cenário é bem mais estável: as médias de rating permanecem próximas de 4,6 em todas as condições, sugerindo que a operação lida bem com esses fatores externos. Para a idadedo do entregador, é avaliado que sua experiência impacta na menor quantidade de avaliações negativas.
Isso ajuda a explicar o gap entre o rating médio (4,61) e o mínimo (2,50): mais do que dispersão aleatória, os casos mais críticos provavelmente refletem entregas concentradas justamente nos intervalos de maior tempo, apontando para falhas pontuais no processo em vez de um problema estrutural amplo.

No conjunto, a leitura é clara: a experiência do cliente depende muito mais da eficiência logística do que de fatores externos. Isso reforça a definição de um SLA de entrega mais rígido, o acompanhamento próximo dos casos de maior atraso e o tempo de entrega como principal indicador de qualidade do serviço.
""")
