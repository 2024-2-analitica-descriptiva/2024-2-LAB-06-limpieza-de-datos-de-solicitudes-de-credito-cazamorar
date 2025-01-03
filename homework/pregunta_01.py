"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
import pandas as pd
import os

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """

    # Rutas de entrada y salida
    input_file = "files/input/solicitudes_de_credito.csv"
    output_dir = "files/output/"
    output_file = os.path.join(output_dir, "solicitudes_de_credito.csv")

    # Asegurarse de que el directorio de salida exista
    os.makedirs(output_dir, exist_ok=True)

    try:
        # Cargar los datos en un DataFrame
        df = pd.read_csv(input_file, sep=";", index_col=0)

        
        # separaciones por espacios
        df.replace({"-": " ", "_": " "}, regex=True, inplace=True)

        # mayusculas y minusculas

        df["sexo"] = df["sexo"].str.lower()
        df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower()
        df["barrio"] = df["barrio"].str.lower()

        df["idea_negocio"] = df["idea_negocio"].str.lower().str.strip()
        df["línea_credito"] = df["línea_credito"].str.lower().str.strip()


        df["fecha_de_beneficio"] = pd.to_datetime(
            df["fecha_de_beneficio"], format="%d/%m/%Y", errors="coerce"
        ).combine_first(pd.to_datetime(df["fecha_de_beneficio"], format="%Y/%m/%d", errors="coerce"))

        df["monto_del_credito"] = (
            df["monto_del_credito"]
            .str.replace(r"[,$]", "", regex=True)
            .str.replace(r"\.00$", "", regex=True)
            .astype(float)
        )

        # Eliminar registros duplicados
        df = df.drop_duplicates()

        # Eliminar registros con datos faltantes
        df = df.dropna()

        # Guardar el archivo limpio
        df.to_csv(output_file, index=False, sep=";")

        print(f"Archivo limpio guardado en: {output_file}")
    except Exception as e:
        print(f"Error procesando el archivo: {e}")

    print(df.sexo.value_counts().to_list())

pregunta_01()
