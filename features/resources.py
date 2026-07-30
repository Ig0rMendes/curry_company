import pandas as pd
import numpy as np

# Tempo de Preparo
def calculate_preparation_time(df):
    df = df.copy()

    # Converter para datetime
    df['Time_Orderd'] = pd.to_datetime(df['Time_Orderd'], format='%H:%M:%S', errors='coerce')
    df['Time_Order_picked'] = pd.to_datetime(df['Time_Order_picked'], format='%H:%M:%S', errors='coerce')

    # Calcular diferença
    df['Preparation_time'] = (df['Time_Order_picked'] - df['Time_Orderd']).dt.total_seconds() / 60

    # Corrigir casos de virada de dia (negativos)
    df.loc[df['Preparation_time'] < 0, 'Preparation_time'] += 24 * 60

    return df

# DistÂncia
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # raio da Terra em km

    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))

    return R * c
def calculate_distance(df):
    df = df.copy()

    df['distance_km'] = haversine(
        df['Restaurant_latitude'],
        df['Restaurant_longitude'],
        df['Delivery_location_latitude'],
        df['Delivery_location_longitude']
    )

    return df

# =========================================
# 🏍 VELOCIDADE (tempo por km)
# =========================================
def calculate_speed(df):
    """
    Calcula a velocidade média da entrega (km/h)
    """
    df = df.copy()

    # Converter tempo de minutos para horas
    df['Time_hours'] = df['Time_taken(min)'] / 60

    # Evitar divisão por zero
    df['Time_hours'] = df['Time_hours'].replace(0, np.nan)

    # Calcular velocidade
    df['Speed_kmh'] = df['Distance_km'] / df['Time_hours']

    return df
    
# Restaurantes Únicos 
def create_restaurant_id(df):
    df['Restaurant_latitude'] = df['Restaurant_latitude'].round(4)
    df['Restaurant_longitude'] = df['Restaurant_longitude'].round(4)

    df['Restaurant_ID'] = (
        df['City'].astype(str) + '_' +
        df['Restaurant_latitude'].astype(str) + '_' +
        df['Restaurant_longitude'].astype(str)
    )

    return df
# Filtro de restaurantes válidos
def filter_valid_restaurants(df):
    df1 = df.copy()

    return df1[
        (df1['Restaurant_latitude'] != 0) &
        (df1['Restaurant_longitude'] != 0)
    ]

# Contar% inválidos
def pct_invalid_locations(df):
    df = df.copy()

    invalid = (
        df['Restaurant_latitude'].isna() |
        df['Restaurant_longitude'].isna() |
        (df['Restaurant_latitude'] == 0) |
        (df['Restaurant_longitude'] == 0)
    )

    return invalid.mean() * 100
