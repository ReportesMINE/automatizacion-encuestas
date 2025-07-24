import pandas as pd

from app.services.cleaner import limpiar_texto, resumir_wrap

def reglas_egresados():
    columnas_a_eliminar = [
        'Nombre',
        'Total de puntos',
        'Comentarios del cuestionario',
        'Hora de la última modificación',
        'Puntos: Nombre Completo',
        'Comentarios: Nombre Completo',
        'Puntos: Correo electrónico',
        'Comentarios: Correo electrónico',
        'Puntos: Código',
        'Comentarios: Código',
        'Puntos: LinkedIn',
        'Comentarios: LinkedIn',
        'Puntos: ¿Para qué empresa trabajas actualmente?',
        'Comentarios: ¿Para qué empresa trabajas actualmente?',
        'Puntos: ¿A qué sector/industria pertenece la empresa?',
        'Comentarios: ¿A qué sector/industria pertenece la empresa?',
        'Puntos: ¿Cuál es tu cargo actual?',
        'Comentarios: ¿Cuál es tu cargo actual?',
        'Puntos: ¿Está relacionado tu cargo con la formación que recibiste en MINE?',
        'Comentarios: ¿Está relacionado tu cargo con la formación que recibiste en MINE?',
        'Puntos: ¿Qué habilidades relacionadas con MINE aportan al desempeño en tu cargo actual?',
        'Comentarios: ¿Qué habilidades relacionadas con MINE aportan al desempeño en tu cargo actual?',
        'Puntos: De acuerdo a tu criterio, ¿Cómo calificarías tu experiencia al haber cursado la maestría MINE?',
        'Comentarios: De acuerdo a tu criterio, ¿Cómo calificarías tu experiencia al haber cursado la maestría MINE?',
        'Comentarios: ¿Qué tan probable es que recomiendes MINE a otros?',
        'Puntos: ¿Qué tan probable es que recomiendes MINE a otros?',
        'Comentarios: ¿Tienes alguna sugerencia o comentario que te gustaría compartir con nosotros para mejorar MINE?',
        'Puntos: ¿Tienes alguna sugerencia o comentario que te gustaría compartir con nosotros para mejorar MINE?',
        'Puntos: ¿Cómo evaluarías el apoyo brindado por nosotros como Universidad de los Andes para tu inserción laboral después de la graduación?',
        'Comentarios: ¿Cómo evaluarías el apoyo brindado por nosotros como Universidad de los Andes para tu inserción laboral después de la graduación?'
    ]

    reglas = {
        "¿Cuál es tu cargo actual?_Limpio": lambda df: df["¿Cuál es tu cargo actual?"].apply(limpiar_texto) if "¿Cuál es tu cargo actual?" in df.columns else "",
        "¿Para qué empresa trabajas actualmente?_Limpio": lambda df: df["¿Para qué empresa trabajas actualmente?"].apply(limpiar_texto) if "¿Para qué empresa trabajas actualmente?" in df.columns else "",
        "¿A qué sector/industria pertenece la empresa?_Limpio": lambda df: df["¿A qué sector/industria pertenece la empresa?"].apply(limpiar_texto) if "¿A qué sector/industria pertenece la empresa?" in df.columns else "",
        "¿Qué habilidades relacionadas con MINE aportan al desempeño en tu cargo actual?_Limpio": lambda df: df["¿Qué habilidades relacionadas con MINE aportan al desempeño en tu cargo actual?"].apply(limpiar_texto) if "¿Qué habilidades relacionadas con MINE aportan al desempeño en tu cargo actual?" in df.columns else "",
        "¿Tienes alguna sugerencia o comentario que te gustaría compartir con nosotros para mejorar MINE?_Limpio": lambda df: df["¿Tienes alguna sugerencia o comentario que te gustaría compartir con nosotros para mejorar MINE?"].apply(limpiar_texto) if "¿Tienes alguna sugerencia o comentario que te gustaría compartir con nosotros para mejorar MINE?" in df.columns else "",
        "Año": lambda df: pd.to_datetime(df["Hora de finalización"], errors='coerce').dt.year,
    }

    return reglas, columnas_a_eliminar
