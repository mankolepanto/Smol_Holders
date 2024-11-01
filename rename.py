import os
import glob
from datetime import datetime

def rename_latest_csv(download_path="C:\\cosas\\tracker_crypto\\Smol_Holders\\downloaded_files"):

    try:
        # Verificar si el directorio existe
        if not os.path.exists(download_path):
            print(f"El directorio {download_path} no existe")
            return None
            
        # Buscar todos los archivos CSV en el directorio específico
        pattern = os.path.join(download_path, "*.csv")
        csv_files = glob.glob(pattern)
        
        if not csv_files:
            print(f"No se encontraron archivos CSV en {download_path}")
            return None
            
        # Obtener el archivo más reciente
        latest_file = max(csv_files, key=os.path.getctime)
        
        # Obtener la fecha actual en formato YYYY-MM-DD
        current_date = datetime.now().strftime("%Y-%m-%d")
        
        # Crear el nuevo nombre del archivo
        new_filename = f"smol_holders_{current_date}.csv"
        new_filepath = os.path.join(download_path, new_filename)
        
        # Si ya existe un archivo con ese nombre, agregar la hora
        if os.path.exists(new_filepath):
            current_time = datetime.now().strftime("%H-%M-%S")
            new_filename = f"smol_holders_{current_date}_{current_time}.csv"
            new_filepath = os.path.join(download_path, new_filename)
        
        # Renombrar el archivo
        os.rename(latest_file, new_filepath)
        print(f"Archivo renombrado exitosamente a: {new_filename}")
        print(f"Ubicación: {new_filepath}")
        
        return new_filepath
        
    except Exception as e:
        print(f"Error al renombrar el archivo: {str(e)}")
        return None

# Ejemplo de uso
if __name__ == "__main__":
    # Puedes llamar la función sin argumentos para usar el directorio por defecto
    renamed_file = rename_latest_csv()
    
    # O especificar un directorio diferente
    # renamed_file = rename_latest_csv("C:\\otra\\ruta\\diferente")