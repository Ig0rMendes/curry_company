import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        return df

    except FileNotFoundError:
        raise FileNotFoundError(
            f"Arquivo não encontrado: {path}"
        )

    except Exception as e:
        raise RuntimeError(
            f"Erro ao carregar o arquivo: {e}"
        )