import pandas as pd


# Métricas Gerais
def rating_summary(df: pd.DataFrame):
    avg_rating = df['Delivery_person_Ratings'].mean()
    max_rating = df['Delivery_person_Ratings'].max()
    min_rating = df['Delivery_person_Ratings'].min()

    return avg_rating, max_rating, min_rating


# Agregações

def rating_by_city(df: pd.DataFrame):
    return df.groupby('City')['Delivery_person_Ratings'].mean().reset_index()


def rating_by_weather(df: pd.DataFrame):
    return df.groupby('Weatherconditions')['Delivery_person_Ratings'].mean().reset_index()

def rating_by_trafic(df: pd.DataFrame):
    return df.groupby('Road_traffic_density')['Delivery_person_Ratings'].mean().reset_index()


def rating_vs_time(df: pd.DataFrame):
    return df[['Time_taken(min)', 'Delivery_person_Ratings']]


def rating_vs_age(df: pd.DataFrame):
    return df[['Delivery_person_Age', 'Delivery_person_Ratings']]
    
# Insigths

def rating_insights(df, df_city, df_weather):
    
    best_city = df_city.sort_values('Delivery_person_Ratings', ascending=False).iloc[0]['City']
    worst_city = df_city.sort_values('Delivery_person_Ratings').iloc[0]['City']

    best_weather = df_weather.sort_values('Delivery_person_Ratings', ascending=False).iloc[0]['Weatherconditions']
    worst_weather = df_weather.sort_values('Delivery_person_Ratings').iloc[0]['Weatherconditions']

    avg_rating = df['Delivery_person_Ratings'].mean()

    insights = f"""
    ⭐ Avaliação média geral: {avg_rating:.2f}

    🏙️ Cidade com melhor avaliação: {best_city}
    🏙️ Cidade com pior avaliação: {worst_city}

    🌦️ Melhor condição climática: {best_weather}
    🌦️ Pior condição climática: {worst_weather}

    📌 Observação:
    Avaliações tendem a cair em condições climáticas adversas e regiões mais densas.
    """

    return insights