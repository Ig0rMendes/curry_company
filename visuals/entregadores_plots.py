import plotly.express as px


# Avaliação por veículo
def plot_rating_vehicle(df):
    fig = px.bar(
        df,
        x='Type_of_vehicle',
        y='Delivery_person_Ratings',
        text='Delivery_person_Ratings',
        labels={
            'Type_of_vehicle': 'Tipo de Veículo',
            'Delivery_person_Ratings': 'Rating Médio'
        }
    )

    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig.update_layout(
        title={
            'text': 'Avaliação Média por Tipo de Veículo',
            'x': 0.5,
            'xanchor': 'center'
        }
    )
    return fig


# Tempo por veículo
def plot_time_vehicle(df):
    fig = px.bar(
        df,
        x='Type_of_vehicle',
        y='Time_taken(min)',
        text='Time_taken(min)',
        labels={
            'Type_of_vehicle': 'Tipo de Veículo',
            'Time_taken(min)': 'Tempo Médio (min)'
        }
    )

    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig.update_layout(
        title={
            'text': 'Tempo médio de Entrega por Tipo de Veículo',
            'x': 0.5,
            'xanchor': 'center'
        }
    )
    return fig


# Elencar rápidos
def plot_top_fast(df):
    fig = px.bar(
        df, 
        x='Delivery_person_ID', 
        y='Time_taken(min)',
        color='City',
    labels={
            'Delivery_person_ID': 'ID Entregador',
            'Time_taken(min)': 'Tempo Médio (min)'
        }
    )
    fig.update_layout(
        title={
            'text': 'Top 10 Entregadores Mais Rápidos',
            'x': 0.5,
            'xanchor': 'center'
        }
    )
    
    return fig


# Elencar lentos
def plot_top_slow(df):
    fig = px.bar(
        df, 
        x='Delivery_person_ID',
        y='Time_taken(min)',
        color='City',
    labels={
            'Delivery_person_ID': 'ID Entregador',
            'Time_taken(min)': 'Tempo Médio (min)'
        }
    )
    fig.update_layout(
        title={
            'text': 'Top 10 Entregadores Mais Lentos',
            'x': 0.5,
            'xanchor': 'center'
        }
    )
    return fig


# Consistência dos entregadores
def plot_consistency(df):
    fig = px.scatter(
        df,
        x='mean',
        y='std',
        hover_data=['Delivery_person_ID'],
        labels={
            'mean': 'Média do Tempo de Entrega',
            'std': 'Desvio Padrão '
        }
    )
    fig.update_layout(
        title={
            'text': 'Consistência dos Entregadores (Tempo vs Variabilidade)',
            'x': 0.5,
            'xanchor': 'center'
        }
    )
    return fig