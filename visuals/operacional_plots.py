import plotly.express as px


def plot_orders_by_weekday(df):
    fig = px.bar(df, x='weekday', 
                 y='orders', 
                 labels={
                    'weekday': 'Dia da Semana',
                    'orders': 'Número de Pedidos'
                }
    )
    fig.update_layout(
        title={
            'text': 'Pedidos por Dia da Semana',
            'x': 0.5,
            'xanchor': 'center'
        }
    )
    return fig


def plot_orders_by_city(df):
    fig = px.bar(df, x='City',
                 y='orders',
                 labels={
                    'City': 'Região',
                    'orders': 'Número de Pedidos'
                }      
    )
    fig.update_layout(
        title={
            'text': 'Pedidos por Região',
            'x': 0.5,
            'xanchor': 'center'
        }
    )
    return fig


def plot_delivery_time_distribution(df):
    fig = px.histogram(df, x='Time_taken(min)',
                       nbins=50,
                       labels={
                        'Time_taken(min)': 'Tempo de Entrega (min)',
                        }      
    )
    fig.update_layout(
        title={
            'text': 'Distribuição de Pedidos por Tempo de Entrega',
            'x': 0.5,
            'xanchor': 'center'
        }
    )
    return fig


def plot_delivery_time_by_city(df):
    fig = px.bar(df, x='City',
                 y='Time_taken(min)',
                 labels={
                    'City': 'Região',
                    'Time_taken(min)': 'Tempo de Entrega (min)'
                }      
    )
    fig.update_layout(
        title={
            'text': 'Tempo Médio por Região',
            'x': 0.5,
            'xanchor': 'center'
        }
    )
    return fig


def plot_delivery_time_multiple(df):
    fig = px.bar(
        df,
        x='multiple_deliveries',
        y='tempo_por_entrega',
        labels={
                    'multiple_deliveries': 'Entregas Múltiplas',
                    'tempo_por_entrega': 'Tempo por Entrega (min)'
                }      
    )
    fig.update_layout(
        title={
            'text': 'Tempo Médio por Número de Entregas',
            'x': 0.5,
            'xanchor': 'center'
        }
    )
    return fig