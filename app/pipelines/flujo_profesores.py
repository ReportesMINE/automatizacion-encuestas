from app.services.cleaner import limpiar_texto

def reglas_profesores():
    return {
        "Empresa_Limpia": lambda df: df["Empresa"].apply(limpiar_texto) if "Empresa" in df.columns else "",
        "Cargo_Limpio": lambda df: df["Cargo"].apply(limpiar_texto) if "Cargo" in df.columns else ""
    }
