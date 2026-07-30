import pandas as pd

# Eficiencia
def calculate_efficiency(df):
    df1 = df.copy()

    df1['tempo'] = df1['Time_taken(min)']
    df1['eficiencia'] = df1['distance_km'] / df1['tempo']

    return df1


# Tipo de veículo
def rating_by_vehicle(df):
    return df.groupby('Type_of_vehicle')['Delivery_person_Ratings'].mean().reset_index()


def time_by_vehicle(df):
    return df.groupby('Type_of_vehicle')['Time_taken(min)'].mean().reset_index()


# Elencar performance
def top_fast_deliverers(df):
    df_aux = (
        df.groupby('Delivery_person_ID')
        .agg({
            'Time_taken(min)': 'mean',
            'City': lambda x: x.mode()[0]
        })
        .reset_index()
    )

    return df_aux.nsmallest(10, 'Time_taken(min)')


def top_slow_deliverers(df):
    df_aux = (
        df.groupby('Delivery_person_ID')
        .agg({
            'Time_taken(min)': 'mean',
            'City': lambda x: x.mode()[0]
        })
        .reset_index()
    )
    return df_aux.nlargest(10, 'Time_taken(min)')


# Avaliar consistência
def delivery_consistency(df):
    df_aux = df.groupby('Delivery_person_ID')['Time_taken(min)'].agg(['mean', 'std']).reset_index()
    df_aux['coef_var'] = df_aux['std'] / df_aux['mean']
    return df_aux


# Insigths da visão
def entregadores_insights(df_vehicle_time, df_consistency):

    fastest_vehicle = df_vehicle_time.sort_values('Time_taken(min)').iloc[0]['Type_of_vehicle']
    slowest_vehicle = df_vehicle_time.sort_values('Time_taken(min)', ascending=False).iloc[0]['Type_of_vehicle']

    most_consistent = df_consistency.sort_values('coef_var').iloc[0]['Delivery_person_ID']
    least_consistent = df_consistency.sort_values('coef_var', ascending=False).iloc[0]['Delivery_person_ID']

    return fastest_vehicle, slowest_vehicle, most_consistent, least_consistent