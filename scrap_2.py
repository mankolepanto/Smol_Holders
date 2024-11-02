from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import logging
import sys

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

def main():
    # Configurar la ruta de descarga
    download_path = os.path.abspath("./Smol_Holders")
    os.makedirs(download_path, exist_ok=True)
    logging.info(f'Directorio de descarga: {download_path}')

    driver = None  # Inicializar driver aquí para su uso posterior

    try:
        # Crear el driver con opciones específicas para GitHub Actions
        driver = Driver(uc=True, undetected=True, headless=True)
        driver.download_path = download_path
        
        logging.info("Iniciando el proceso de scraping...")
        
        # Navegar a la URL
        driver.get("https://arbiscan.io/exportData?type=tokenholders&contract=0x9e64d3b9e8ec387a9a58ced80b71ed815f8d82b5&decimal=18")
        
        logging.info("Esperando que se cargue la página...")
        time.sleep(30)  # Aumentar el tiempo de espera
        
        # Esperar y hacer clic en el botón
        download_button = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_btnSubmit"))
        )
        
        logging.info("Intentando la descarga...")
        driver.execute_script("arguments[0].click();", download_button)
        
        # Esperar a que se complete la descarga
        time.sleep(10)
        logging.info("Descarga completada exitosamente")
        
    except Exception as e:
        logging.error(f"Error durante la ejecución: {str(e)}")
        logging.error(f"URL actual: {driver.current_url if driver else 'No se pudo obtener la URL'}")
        raise e
        
    finally:
        if driver:  # Verificar que el driver no sea None antes de cerrar
            driver.save_screenshot("error.png")
            driver.quit()
        logging.info("Proceso finalizado")

if __name__ == "__main__":
    main()
