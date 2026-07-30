import plotly.express as px



# LINHA: Rating x Tempo
def plot_rating_vs_time(df):
    # Agrega o rating médio por tempo de entrega
    df_agg = (
        df.groupby('Time_taken(min)')['Delivery_person_Ratings']
        .mean()
        .reset_index()
        .sort_values('Time_taken(min)')
    )

    fig = px.line(
        df_agg,
        x='Time_taken(min)',
        y='Delivery_person_Ratings',
        markers=True,
        labels={
            'Time_taken(min)': 'Tempo de Entrega (min)',
            'Delivery_person_Ratings': 'Avaliação Média'
        }
    )
    fig.update_layout(
        title={
            'text': 'Distribuição das Avaliações Médias pelo Tempo de Entrega',
            'x': 0.5,
            'xanchor': 'center'
        }
    )
    return fig


# Rating por Cidade

def plot_rating_by_city(df):
    fig = px.bar(
        df,
        x='City',
        y='Delivery_person_Ratings',
        text = 'Delivery_person_Ratings',
        labels={
            'City': 'Região',
            'Delivery_person_Ratings': 'Avaliação'
        }
    )
    fig.update_layout(
        title={
            'text': 'Distribuição das Avaliações por Região',
            'x': 0.5,
            'xanchor': 'center'
        }
    )
    
    fig.update_traces(
        texttemplate='%{text:.2f}',
        textposition='outside'
    )
    
    return fig



# Rating por Clima

def plot_rating_by_weather(df):
    fig = px.bar(
        df,
        x='Weatherconditions',
        y='Delivery_person_Ratings',
        text = 'Delivery_person_Ratings',
        labels={
            'Weatherconditions': 'Condições Climáticas',
            'Delivery_person_Ratings': 'Avaliações'
        }
    )
    fig.update_layout(
        title={
            'text': 'Avaliações por Condições Climáticas',
            'x': 0.5,
            'xanchor': 'center'
        }
    )
    
    fig.update_traces(
        texttemplate='%{text:.2f}',
        textposition='outside'
    )
    return fig

# Rating por Tráfego
def plot_rating_by_trafic(df):
    fig = px.bar(
        df,
        x='Road_traffic_density',
        y='Delivery_person_Ratings',
        text = 'Delivery_person_Ratings',
        labels={
            'Road_traffic_density': 'Condições do Tráfego',
            'Delivery_person_Ratings': 'Avaliações'
        }
    )
    fig.update_layout(
        title={
            'text': 'Avaliações por Condições de Tráfego',
            'x': 0.5,
            'xanchor': 'center'
        }
    )
    fig.update_traces(
        texttemplate='%{text:.2f}',
        textposition='outside'
    )
    return fig
# Rating x Idade

def plot_rating_vs_age(df):
    fig = px.scatter(
        df,
        x='Delivery_person_Age',
        y='Delivery_person_Ratings',
        labels={
            'Delivery_person_Age': 'Condições do Tráfego',
            'Delivery_person_Ratings': 'Avaliações'
        }   
    )
    fig.update_layout(
        title={
            'text': 'Distribuição das Avaliações por Idade dos Entregadores',
            'x': 0.5,
            'xanchor': 'center'
        }
    )
    return fig