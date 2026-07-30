import pandas as pd

def orders_by_weekday(df: pd.DataFrame):
    df_aux = df.copy()
    
    df_aux['weekday'] = df_aux['Order_Date'].dt.day_name()

    df_weekday = df_aux.groupby('weekday').size().reset_index(name='orders')

    ordered_days = [
        'Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday'
    ]

    df_weekday['weekday'] = pd.Categorical(
        df_weekday['weekday'],
        categories=ordered_days,
        ordered=True
    )

    df_weekday = df_weekday.sort_values('weekday')

    return df_weekday


def orders_by_city(df: pd.DataFrame):
    return df.groupby('City').size().reset_index(name='orders')


def delivery_time_distribution(df: pd.DataFrame):
    return df['Time_taken(min)']


def delivery_time_by_city(df: pd.DataFrame):
    return df.groupby('City')['Time_taken(min)'].mean().reset_index()


def delivery_time_multiple(df: pd.DataFrame):
    df_aux = df.copy()
    df_aux['multiple_deliveries'] = df_aux['multiple_deliveries'].fillna(0)
    df_aux['tempo_por_entrega'] = df_aux['Time_taken(min)'] / (df_aux['multiple_deliveries'] + 1)

    return df_aux.groupby('multiple_deliveries')['tempo_por_entrega'].mean().reset_index()
def operational_insights(df, df_weekday, df_city, df_time_city):

    # Volume
    busiest_day = df_weekday.sort_values('orders', ascending=False).iloc[0]['weekday']
    busiest_city = df_city.sort_values('orders', ascending=False).iloc[0]['City']

    # Tempo
    slowest_city = df_time_city.sort_values('Time_taken(min)', ascending=False).iloc[0]['City']
    fastest_city = df_time_city.sort_values('Time_taken(min)').iloc[0]['City']
