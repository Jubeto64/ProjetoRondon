import pandas as pd
import os


def save_to_csv(data: dict, filepath: str):
    df_new = pd.DataFrame([data])

    if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
        df_existing = pd.read_csv(filepath, dtype={"identificador": str})
        df_result = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_result = df_new

    df_result.to_csv(filepath, index=False)