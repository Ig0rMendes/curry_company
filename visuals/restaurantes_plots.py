import plotly.express as px
import folium
from folium.plugins import HeatMap


def top_restaurantes_pedidos(df):
    data = (
        df.groupby('Restaurant_ID')['ID']
        .count()
        .reset_index()
        .sort_values(by='ID', ascending=False)
        .head(10)
    )

    fig = px.bar(
        data,
        x='Restaurant_ID',
        y='ID',
        labels={
            'Restaurant_ID': 'Restaurante ID',
            'ID': 'Contagem de Entregas'
        }
    )
    fig.update_layout(
        title={
            'text': 'Top 10 Restaurantes com mais Pedidos',
            'x': 0.5,
            'xanchor': 'center'
        }
    )

    return fig


def top_restaurantes_rapidos(df):
    data = (
        df.groupby('Restaurant_ID')['Time_taken(min)']
        .mean()
        .reset_index()
        .sort_values(by='Time_taken(min)')
        .head(10)
    )

    fig = px.bar(
        data,
        x='Restaurant_ID',
        y='Time_taken(min)',
        labels={
            'Restaurant_ID': 'Restaurante ID',
            'Time_taken(min)': 'Tempo de Preparo (min)'
        }
    )
    fig.update_layout(
        title={
            'text': 'Top 10 Restaurantes com Preparos mais Rápidos',
            'x': 0.5,
            'xanchor': 'center'
        }
    )

    return fig

    return fig


def tempo_por_trafego(df):
    data = (
        df.groupby('Road_traffic_density')['Time_taken(min)']
        .mean()
        .reset_index()
    )

    fig = px.bar(
        data,
        x='Road_traffic_density',
        y='Time_taken(min)',
        text='Time_taken(min)',
        labels={
            'Road_traffic_density': 'Densidade do Tráfego',
            'Time_taken(min)': 'Tempo de Entrega (min)'
        }
    )
    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig.update_layout(
        title={
            'text': 'Impacto do Tráfego no Tempo de Entrega',
            'x': 0.5,
            'xanchor': 'center'
        }
    )

    return fig

# plot de mapa usando folium

def heatmap_restaurantes(df):
    mapa = folium.Map(
        location=[
            df['Restaurant_latitude'].mean(),
            df['Restaurant_longitude'].mean()
        ],
        zoom_start=5,
    )

    heat_data = [
        [row['Restaurant_latitude'], row['Restaurant_longitude'], row['order_count']]
        for _, row in df.iterrows()
    ]

    HeatMap(heat_data).add_to(mapa)

    return mapa
