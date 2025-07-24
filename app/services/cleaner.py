import re
import textwrap
import pandas as pd
from typing import List
from app.config.settings import STOPWORDS, ENTIDADES_PROHIBIDAS

def normalizar_texto(texto: str) -> str:
    if not isinstance(texto, str):
        return ""
    texto = texto.lower()
    texto = re.sub(r'[áàäâ]', 'a', texto)
    texto = re.sub(r'[éèëê]', 'e', texto)
    texto = re.sub(r'[íìïî]', 'i', texto)
    texto = re.sub(r'[óòöô]', 'o', texto)
    texto = re.sub(r'[úùüû]', 'u', texto)
    texto = re.sub(r'\.', '', texto)  # Quitar puntos: S.A.S. -> SAS
    return texto

def eliminar_entidades(texto: str, entidades: List[str]) -> str:
    for entidad in entidades:
        patron = re.escape(entidad.lower())
        texto = re.sub(patron, '', texto)
    return texto

def eliminar_stopwords(texto: str, stopwords: set) -> str:
    if not isinstance(texto, str):
        return ""
    palabras = texto.split()
    palabras_filtradas = [p for p in palabras if p not in stopwords]
    return ' '.join(palabras_filtradas)

def resumir_wrap(texto):
    if pd.isna(texto):
        return texto
    texto = str(texto)
    return texto.split(".")[0] + "." if "." in texto else texto

def limpiar_texto(texto: str) -> str:
    if not isinstance(texto,str):
        return ""
    texto = normalizar_texto(texto)
    texto = eliminar_entidades(texto, ENTIDADES_PROHIBIDAS)
    texto = eliminar_stopwords(texto, STOPWORDS)
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto
