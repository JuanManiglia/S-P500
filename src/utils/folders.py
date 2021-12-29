import os, sys
import pandas as pd


class Folders:
    """
    Esta clase se utiliza para administrar estructuras de carpetas y agregar rutas para facilitar el flujo de trabajo.
    """

    @staticmethod
    def get_current_path(file=False):
        """
        Muestra la ruta actual:
        Parámetros:
            - file: si es True, muestra el directorio de trabajo actual
                    si es False, muestra el directorio que contiene el archivo
        """
        if file:
            return os.getcwd()
        else:
            return os.path.dirname(os.getcwd())

    @staticmethod
    def add_path(num, jupyter=True):
        '''
        Agrega una ruta a sys.
        Args:
            - num: número de veces que se obtiene el nombre de directorio hasta llegar a la ruta raíz.
        
        Returns:
            - dirpath: la ruta deseada.
        '''
        if jupyter:
            dirpath = os.getcwd()
        else:
            dirpath = __file__ # en caso de jupyter se usa os.getcwd()
        for i in range(num):
            dirpath = os.path.dirname(dirpath)
        sys.path.append(dirpath)

        return dirpath

    @staticmethod
    def append_path(path=os.path.dirname(os.getcwd()), jupyter=True):
        """
        Agrega ruta a sys.

        Returns:
            - dirpath: el camino deseado
        """  
        if jupyter:
            path = os.getcwd()
        else:
            path = __file__ # en caso de jupyter se usa os.getcwd()

        path = sys.path.append(path)

        return path


    @staticmethod
    def read_directory_data(path):
        """
        Este método lee los datos del directorio y le asigna variables.
        Parámetros:
            - path: la ruta del directorio que se va a leer.
        """
        files_dict = {'csv': [], 'xlsx': []}
        variable_dict = {}
        list_csv = []
        list_xlsx = []

        for pos, file in enumerate(os.listdir(path)):
            if file.endswith('.csv'):
                filename = file.split('.')[0]
                filename_str = str(filename)
                list_csv.append(filename)
                filename = pd.read_csv(f"{path}{file}")
                variable_dict[filename_str] = filename

            elif file.endswith('.xlsx'):
                filename = file.split('.')[0]
                filename_str = str(filename)
                list_xlsx.append(filename)
                filename = pd.read_excel(f"{path}{file}", engine='openpyxl')
                variable_dict[filename_str] = filename

        files_dict['csv'].append(list_csv)
        files_dict['xlsx'].append(list_xlsx)
        print(f"Las siguientes variables ya están listas para usarse:\n{files_dict}")

        return variable_dict

class Saver:
    """
    Esta clase se utiliza para guardar archivos.
    """
    @staticmethod
    def save_output_file(df, filename, path):
        """
        
Esta función guarda archivos de datos en csv y los coloca en la carpeta de salida.
        Parámetros:
        - df: Un pandas Dataframe.
        - filename: El nombre del archivo.
        - path: La ruta en la que se guardará el archivo.
        """
        doc_name = path + filename + '.csv'  
        df.to_csv(doc_name, index=False)
        print(f"Se ha guardado el siguiente archivo:\n{filename}")
        print(f"\nLo puedes encontrar aquí: {doc_name}")