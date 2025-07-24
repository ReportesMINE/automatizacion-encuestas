import pandas as pd
from app.services.cleaner import limpiar_texto

def reglas_eventos():
    columnas_a_eliminar = [
        'Nombre',
        'Total de puntos',
        'Comentarios del cuestionario',
        'Hora de publicación de la calificación',
        'Puntos: Nombre Completo',
        'Comentarios: Nombre Completo',
        'Puntos: Correo institucional',
        'Comentarios: Correo institucional',
        'Puntos: ¿Qué semestre de la maestría se encuentra cursando?',
        'Comentarios: ¿Qué semestre de la maestría se encuentra cursando?',
        'Puntos: Nombre de la empresa y/o organización donde actualmente trabaja',
        'Comentarios: Nombre de la empresa y/o organización donde actualmente trabaja',
        'Puntos: ¿Qué cargo ocupa actualmente?',
        'Comentarios: ¿Qué cargo ocupa actualmente?',
        'Puntos: ¿Qué cargo aspira al terminar la Maestría?',
        'Comentarios: ¿Qué cargo aspira al terminar la Maestría?',
        'Puntos: LinkedIn',
        'Comentarios: LinkedIn'
    ]

    reglas = {
        "Nombre de la empresa y/o organización donde actualmente trabaja_Limpio": lambda df: df["Nombre de la empresa y/o organización donde actualmente trabaja"].apply(limpiar_texto) if "Nombre de la empresa y/o organización donde actualmente trabaja" in df.columns else "",
        "¿Qué cargo ocupa actualmente?_Limpio": lambda df: df["¿Qué cargo ocupa actualmente?"].apply(limpiar_texto) if "¿Qué cargo ocupa actualmente?" in df.columns else "",
        "¿Qué cargo aspira al terminar la Maestría?_Limpio": lambda df: df["¿Qué cargo aspira al terminar la Maestría?"].apply(limpiar_texto) if "¿Qué cargo aspira al terminar la Maestría?" in df.columns else "",
        "Año": lambda df: pd.to_datetime(df["Hora de finalización"], errors='coerce').dt.year,
    }

    return reglas, columnas_a_eliminar