import pandas as pd
import numpy as np

def procesar_excel(ruta_entrada: str, ruta_salida: str, reglas: dict, columnas_a_eliminar: list = None) -> None:
    df = pd.read_excel(ruta_entrada)
    df.replace(r'^\s*$', np.nan, regex=True, inplace=True)
    df = df.dropna(how="all")

    df.columns = (
        df.columns
        .str.replace('\n', ' ')
        .str.replace('\r', ' ')
        .str.replace('  ', ' ')
        .str.strip()
    )

    if columnas_a_eliminar:
        columnas_a_eliminar_limpias = [
            col.replace('\n', ' ').replace('\r', ' ').replace('  ', ' ').strip()
            for col in columnas_a_eliminar
        ]

        #for i, col in enumerate(df.columns):
        #    print(f"{i}: {repr(col)}")

        #for i, col in enumerate(columnas_a_eliminar_limpias):
            #print(f"{i}: {repr(col)}")
        no_encontradas = [col for col in columnas_a_eliminar_limpias if col not in df.columns]

        if no_encontradas:
            print("\n❌ Estas columnas NO se encontraron EXACTAMENTE en el DataFrame:")
            for col in no_encontradas:
                print(f"- {repr(col)}")
        else:
            df = df.drop(columns=[col for col in columnas_a_eliminar_limpias if col in df.columns], errors='ignore')

        #for i, col in enumerate(df.columns):
        #    print(f"{i}: {repr(col)}")

    for nueva_col, funcion in reglas.items():
        df[nueva_col] = funcion(df)

    df.to_excel(ruta_salida, index=False)
    print(f"✅ Guardado en: {ruta_salida}")
    print("\n| {:<40} | {:<10} |".format("Columna", "Tipo"))
    print("|" + "-" * 42 + "|" + "-" * 12 + "|")
    for col, dtype in df.dtypes.items():
        print("| {:<40} | {:<10} |".format(col, str(dtype)))