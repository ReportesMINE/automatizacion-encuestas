from app.services.cleaner import limpiar_texto
from app.domain.sector_classifier import clasificar_sector

def reglas_empleadores():
    return {
        "Empresa_Limpia": lambda df: df["Empresa"].apply(limpiar_texto) if "Empresa" in df.columns else "",
        "Cargo_Limpio": lambda df: df["Cargo"].apply(limpiar_texto) if "Cargo" in df.columns else "",
        "Sector_Limpio": lambda df: df["Sector de Industria"].apply(limpiar_texto) if "Sector de Industria" in df.columns else "",
        "Sector": lambda df: df["Sector de Industria"].apply(clasificar_sector) if "Sector de Industria" in df.columns else ""
    }
