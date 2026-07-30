import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpeza profissional do dataset de entregas.

    Objetivo:
    Garantir consistência, remover ruídos e preparar dados
    para análises e feature engineering.

    Estratégia:
    - Padronização de strings
    - Tratamento de NaN
    - Conversão de tipos
    - Limpeza de colunas críticas (tempo, localização)
    - Remoção de outliers
    """

    df1 = df.copy()

    # =====================================
    # 🔹 1. STRIP EM COLUNAS STRING
    # =====================================
    cols_strip = [
        'ID', 'Road_traffic_density', 'Type_of_order',
        'Type_of_vehicle', 'City', 'Festival', 'Weatherconditions',
        'Time_Orderd', 'Time_Order_picked'
    ]

    for col in cols_strip:
        if col in df1.columns:
            df1[col] = df1[col].astype(str).str.strip()

    # =====================================
    # 🔹 2. PADRONIZAÇÃO DE NaN
    # =====================================
    df1.replace(['NaN', 'NaN ', '', 'None', 'nan'], pd.NA, inplace=True)

    # =====================================
    # 🔹 3. LIMPEZA DE CATEGORIAS
    # =====================================
    if 'Weatherconditions' in df1.columns:
        df1['Weatherconditions'] = (
            df1['Weatherconditions']
            .str.replace('conditions ', '', regex=False)
        )

    # =====================================
    # 🔹 4. CONVERSÃO NUMÉRICA
    # =====================================

    # Ratings
    df1['Delivery_person_Ratings'] = (
        df1['Delivery_person_Ratings']
        .astype(str)
        .str.extract(r'(\d+\.\d+)')
    )
    df1['Delivery_person_Ratings'] = pd.to_numeric(
        df1['Delivery_person_Ratings'], errors='coerce'
    )

    # Tempo de entrega
    df1['Time_taken(min)'] = (
        df1['Time_taken(min)']
        .astype(str)
        .str.extract(r'(\d+)')
    )
    df1['Time_taken(min)'] = pd.to_numeric(
        df1['Time_taken(min)'], errors='coerce'
    )

    # Idade
    df1['Delivery_person_Age'] = pd.to_numeric(
        df1['Delivery_person_Age'], errors='coerce'
    )

    # Entregas múltiplas
    df1['multiple_deliveries'] = pd.to_numeric(
        df1['multiple_deliveries'], errors='coerce'
    )

    # =====================================
    # 🔹 5. LOCALIZAÇÃO (CRÍTICO)
    # =====================================
    cols_location = [
        'Restaurant_latitude', 'Restaurant_longitude',
        'Delivery_location_latitude', 'Delivery_location_longitude'
    ]

    for col in cols_location:
        df1[col] = pd.to_numeric(df1[col], errors='coerce')

    # =====================================
    # 🔹 6. DATAS
    # =====================================
    df1['Order_Date'] = pd.to_datetime(
        df1['Order_Date'], format='%d-%m-%Y', errors='coerce'
    )

    # =====================================
    # 🔹 7. HORÁRIOS (CRÍTICO)
    # =====================================
    cols_time = ['Time_Orderd', 'Time_Order_picked']

    for col in cols_time:
        df1[col] = pd.to_datetime(
            df1[col], format='%H:%M:%S', errors='coerce'
        )

    # =====================================
    # 🔹 8. REMOVER NaN (COLUNAS CRÍTICAS)
    # =====================================
    df1 = df1.dropna(subset=[
        'Delivery_person_Age',
        'Delivery_person_Ratings',
        'Time_taken(min)',
        'multiple_deliveries',
        'Restaurant_latitude',
        'Restaurant_longitude',
        'Delivery_location_latitude',
        'Delivery_location_longitude',
        'Time_Orderd',
        'Time_Order_picked'
    ])

    # =====================================
    # 🔹 9. REMOÇÃO DE OUTLIERS
    # =====================================
    df1 = df1[
        (df1['Delivery_person_Age'].between(18, 60)) &
        (df1['Delivery_person_Ratings'].between(1, 5)) &
        (df1['Time_taken(min)'] < 200)
    ]

    # =====================================
    # 🔹 10. TIPAGEM FINAL
    # =====================================
    df1['Delivery_person_Age'] = df1['Delivery_person_Age'].astype(int)
    df1['multiple_deliveries'] = df1['multiple_deliveries'].astype(int)
    df1['Time_taken(min)'] = df1['Time_taken(min)'].astype(int)

    # =====================================
    # 🔹 11. FEATURES DE DATA (BONUS)
    # =====================================
    df1['order_day'] = df1['Order_Date'].dt.day
    df1['order_week'] = df1['Order_Date'].dt.isocalendar().week
    df1['order_month'] = df1['Order_Date'].dt.month

    return df1