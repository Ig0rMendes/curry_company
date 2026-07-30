#Métricas da visão
def restaurantes_kpis(df):
    return {
        "total_restaurantes": df['Restaurant_ID'].nunique(),
        "total_pedidos": df['ID'].nunique(),
        "tempo_medio": round(df['Time_taken(min)'].mean(), 2)
    }

#Elencando restaurantes por volume de pedido
def pedidos_por_restaurante(df):
    return (
        df.groupby('Restaurant_ID')['ID']
        .count()
        .reset_index()
        .sort_values(by='ID', ascending=False)
    )

# Restaurantes mais rápidos
def tempo_medio_por_restaurante(df):
    return (
        df.groupby('Restaurant_ID')['Time_taken(min)']
        .mean()
        .reset_index()
        .sort_values(by='Time_taken(min)')
    )

# Avalliando numero de pedidos para as classificações de cidade
def mapa_dados(df):
    df_aux = df[[
        'Delivery_location_latitude',
        'Delivery_location_longitude',
        'City',
        'Road_traffic_density'
    ]].dropna()

    return df_aux

# HeatMap
def HeatMap (df):
    return (
        df.groupby(['Restaurant_latitude', 'Restaurant_longitude'])['ID']
        .count()
        .reset_index()
        .rename(columns={'ID': 'order_count'})
    )