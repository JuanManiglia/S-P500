import pandas as pd
import numpy as np

class DataAnalyzer:
    """
    Esta clase se utiliza para tareas de minería de datos.
    """

    @staticmethod
    def df_info(df):
        '''
        La función proporciona toda la información relevante de un pandas.DataFrame.
            Argumentos:
                - df: Un pandas.Dataframe
            Prints:
                - df.shape[0]: Número de filas.
                - df.shape[1]: Número de columnas.
                - df.columns: El nombre de las columnas del dataset.
                - df.info(): Informacíon basica sobre el dataset.
                - df.isna().sum(): Valores del tipo NaN por columna.
        '''
        print('####\nINFORMACION DEL DATAFRAME\n####')
        print('\nNumero de Filas:', df.shape[0])
        print('Numero de Columnas:', df.shape[1])
        print('\n#### COLUMNA DEL DATAFRAME ####\n', df.columns, '\n')
        print('### TIPOs DE COLUMNA DEL DATAFRAME ###\n')
        print('\n', df.info(verbose=True)) 
        print('\n### TOTAL DE VALORES NaN ###\n')
        print('\n', df.isna().sum()) 
        print(f"\n### CHEQUEO DE DUPLICADOS ###\n {df.duplicated().values.any()}: {df.duplicated().sum()}")

    @staticmethod
    def remove_cols(df, cols):
        '''
        Esta función elimina columnas específicas de un Dataframe.
        Parámetros:
            - df: Un pandas Dataframe.
        Returns:
            - cols: una lista con las columnas que se desean borrar.
            - df: el mismo dataframe sin las columnas eliminadas.
        '''
        df.drop(columns=cols, inplace=True)
        return f'Las siguientes columnas se han eliminado de su DataFrame: {cols}'

    @staticmethod
    def apply_function_to_cols(df, cols, function):
        '''
        Esta función se usa para aplicar funciones a columnas específicas en un Dataframe.
        Parámetros:
            - df: Un pandas DataFrame.
            - cols: Una lista of columnas.
            - función: La función que se aplicará.
        Returns:
            - df: Un Dataframe con la función aplicada.
        '''
        for i in cols:
            df[i] = df[i].apply(function)

    @staticmethod
    def cols_to_lowercase(df):
        """
        Esta función convierte todos los nombres de las columnas en minúsculas.
        Parámetros:
            - df: Un pandas DataFrame.
        """
        df = df.rename(columns=str.lower)
        return df
    
    @staticmethod
    def split_df_column(df, cols, sep=" ", n=1):
        """
        Esta función divide una columna de un Dataframe en función de un separador.
        Parámetros:
            - df: Un pandas DataFrame.
            - sep: Un separator (Por Defecto: ' ').
            - cols: Una columna o una lista de Columnas de un DataFrame.
            - n: Un número entero que especifica la cantidad de divisiones (Por Defecto: 1).
        """
        df[cols] = df[cols].str.split(sep, n=n, expand=True)

    @staticmethod
    def strip_df_column(df, cols, strip, to_float=False):
        """
        Esta función quita un valor de una columna de un Dataframe.
        Parametros:
            - df: Un pandas DataFrame.
            - cols: Una columna o una lista de Columnas de un DataFrame.
            - strip: La cadena que se va a quitar.
            - to_float: Si True, el tipo de datos de la columna será flotante.
        """
        df[cols] = df[cols].str.strip(strip)
        if to_float:
            df[cols] = df[cols].astype(float)

    @staticmethod
    def get_df_value_counts(df):
        """
        Esta función verifica cuántos valores diferentes hay en cada columna de un Dataframe.
        Parámetros:
            - df: Un pandas DataFrame.
        """
        print(f"###### CANTIDAD DE VALORES DIFERENTES EN EL DATAFRAME ######\n")
        for pos, column in enumerate(df.columns):
            print(F"{column}: {len(df[column].value_counts())}")

    @staticmethod
    def check_data_percentage(df, subset):
        """
        Esta función muestra el porcentaje de corte de un Dataframe.
        Parámetros:
            - df: Un pandas Dataframe.
            - subset: La porción específica del Dataframe.
        """
        percentage = round((subset.shape[0] * 100) / df.shape[0], 4)
        print(f"El porcentaje de los datos del subconjunto en los datos en general es: {percentage}%")

    @staticmethod
    def less_zero_units(df, col):
        '''
        Esta función comprueba si una columna contiene cero o valores negativos.
        Parámetros:
            - df: Un pandas DataFrame
            - col: Una columna del DataFrame

        Returns:
            - zero_df: Un Dataframe con los valores de la columna que son iguales a cero.
            - less_zero_df: Un Dataframe con los valores de la columna que son menores a cero.
        '''
        zero_df = df[df[col] == 0]
        less_zero_df = df[df[col] < 0]
        print(f"Total de filas sin unidades en la {col} columna: {zero_df.shape[0]}")
        print(f"Total de filas con valores menores de 0 en la {col} columna: {less_zero_df.shape[0]}")

        return zero_df, less_zero_df

    @staticmethod
    def check_data_distribution(df, col):
        '''
        Esta función verifica cómo se distribuyen los valores.
        Parámetros:
            - df: Un pandas Dataframe
            - col: Una columna del DataFrame
        '''
        x = df[col]

        percentile_25 = np.percentile(x, 25)
        percentile_50 = np.percentile(x, 50)
        percentile_75 = np.percentile(x, 75)

        print(f"La {col} columna tiene esta distribución de datos:")
        print("Percentil 25: {percentile_25}")
        print("Percentil 50: {percentile_50}")
        print("Percentil 75: {percentile_75}")