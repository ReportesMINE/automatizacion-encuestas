from app.services.cleaner import limpiar_texto, resumir_wrap

def reglas_estudiantes():
    columnas_a_eliminar = [
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
        'Puntos: ¿Cuál es tu cargo actual?',
        'Comentarios: ¿Cuál es tu cargo actual?',
        'Puntos: ¿Para qué empresa trabajas actualmente?',
        'Comentarios: ¿Para qué empresa trabajas actualmente?',
        'Puntos: ¿A qué sector/industria pertenece la empresa?',
        'Comentarios: ¿A qué sector/industria pertenece la empresa?',
        'Puntos: ¿Tienes experiencia laboral relevante en el campo relacionado con MINE?',
        'Comentarios: ¿Tienes experiencia laboral relevante en el campo relacionado con MINE?',
        'Puntos: ¿En qué semestre de la maestría te encuentras?',
        'Comentarios: ¿En qué semestre de la maestría te encuentras?',
        'Puntos: ¿Planeas inscribir el proyecto de grado para el próximo semestre?',
        'Comentarios: ¿Planeas inscribir el proyecto de grado para el próximo semestre?',
        'Puntos: De acuerdo a tu criterio, ¿Cómo calificarías tu experiencia hasta el momento cursando la maestría?',
        'Comentarios: De acuerdo a tu criterio, ¿Cómo calificarías tu experiencia hasta el momento cursando la maestría?',
        'Comentarios: ¿Qué tan probable es que recomiendes nuestro programa a otros?',
        'Puntos: ¿Qué tan probable es que recomiendes nuestro programa a otros?',
        'Comentarios: En términos generales, ¿consideras que la maestría ha cumplido con tus expectativas?',
        'Puntos: En términos generales, ¿consideras que la maestría ha cumplido con tus expectativas?',
        'Comentarios: ¿Tienes alguna sugerencia o comentario que te gustaría compartir con nosotros para mejorar el programa?',
        'Puntos: ¿Tienes alguna sugerencia o comentario que te gustaría compartir con nosotros para mejorar el programa?'
    ]

    reglas = {
        "¿Cuál es tu cargo actual?_Limpio": lambda df: df["¿Cuál es tu cargo actual?"].apply(limpiar_texto) if "¿Cuál es tu cargo actual?" in df.columns else "",
        "¿Para qué empresa trabajas actualmente?_Limpio": lambda df: df["¿Para qué empresa trabajas actualmente?"].apply(limpiar_texto) if "¿Para qué empresa trabajas actualmente?" in df.columns else "",
        "¿A qué sector/industria pertenece la empresa?_Limpio": lambda df: df["¿A qué sector/industria pertenece la empresa?"].apply(limpiar_texto) if "¿A qué sector/industria pertenece la empresa?" in df.columns else "",
        "¿Tienes alguna sugerencia o comentario que te gustaría compartir con nosotros para mejorar el programa?_Resumido": lambda df: df["¿Tienes alguna sugerencia o comentario que te gustaría compartir con nosotros para mejorar el programa?"].apply(lambda x: resumir_wrap(x)) if "¿Tienes alguna sugerencia o comentario que te gustaría compartir con nosotros para mejorar el programa?" in df.columns else "",
    }

    return reglas, columnas_a_eliminar
