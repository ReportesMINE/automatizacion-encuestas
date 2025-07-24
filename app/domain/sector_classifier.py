import re
import unicodedata

def limpiar_general(texto: str) -> str:
    if not isinstance(texto, str):
        return ""
    texto = texto.lower().strip()
    texto = unicodedata.normalize("NFD", texto).encode("ascii", "ignore").decode("utf-8")
    texto = re.sub(r'\.', '', texto)
    return texto

def clasificar_sector(texto: str) -> str:
    if not isinstance(texto, str):
        return "No clasificado"

    texto = limpiar_general(texto)

    sectores = {
        "Tecnología (TI) y Software": ["tecnologia", "software", "it", "informatic", "sistema", "digital", "desarrollo", "datos", "startup", "cloud", "ai", "ml"],
        "Servicios Financieros y Banca": ["banco", "financ", "fintech", "credit", "asegur", "riesgo", "contable", "bancario"],
        "Salud y Farmacéutica": ["salud", "hospital", "medic", "farmaceut", "clinica", "bio", "enfermer"],
        "Consumo y Retail": ["retail", "consumo", "venta", "supermercado", "moda", "ecommerce", "tienda"],
        "Industrial y Manufactura": ["manufactura", "fabrica", "produccion", "industrial", "maquinaria"],
        "Energía y Recursos Naturales": ["energia", "petroleo", "gas", "min", "recursos", "renovable", "carbon", "hidro"],
        "Consultoría y Servicios Profesionales": ["consultor", "asesor", "servicio profesional", "outsourcing", "auditor", "estrategia", "investigacion"],
        "Telecomunicaciones": ["telecom", "telefon", "redes", "comunicacion", "operador"],
        "Transporte y Logística": ["logistica", "transporte", "envio", "distribucion", "carga", "aereo", "maritimo"],
        "Sector Público y Gobierno": ["sector publico", "gobierno", "publico", "ministerio", "alcaldia", "institucion", "estado", "oficial", "entidad estatal", "seguridad social"],
        "Medios y Entretenimiento": ["medios", "television", "radio", "cine", "musica", "contenido", "entretenimiento"],
        "Agroindustria y Alimentos": ["agro", "agricultura", "alimento", "ganader", "pesca", "campo"],
    }

    for categoria, keywords in sectores.items():
        for kw in keywords:
            if re.search(r'\b' + re.escape(kw), texto):
                return categoria

    return "No clasificado"
