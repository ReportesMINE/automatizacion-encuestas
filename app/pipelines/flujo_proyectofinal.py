import pandas as pd
from app.services.cleaner import limpiar_texto

def reglas_proyectofinal():

    reglas = {
        "Nombre de la empresa_Limpio": lambda df: df["Nombre de la empresa"].apply(limpiar_texto) if "Nombre de la empresa" in df.columns else "",
        "Año": lambda df: pd.to_datetime(df["Hora de finalización"], errors='coerce').dt.year,
        "Semestre": lambda df: pd.to_datetime(df['Hora de finalización'], errors='coerce').dt.month.apply(lambda m: 1 if m <= 6 else 2)
    }

    return reglas