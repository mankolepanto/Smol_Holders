from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import logging
import sys
from datetime import datetime

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

    driver = None
    try:
        # Crear el driver con opciones específicas para GitHub Actions
        driver = Driver(uc=True, undetected=True, headless=True)
        driver.download_path = download_path
        
        logging.info("Iniciando el proceso de scraping...")
        
        # Navegar a la URL
        driver.get("https://arbiscan.io/exportData?type=tokenholders&contract=0x9e64d3b9e8ec387a9a58ced80b71ed815f8d82b5&decimal=18")
        
        logging.info("Esperando que se cargue la página...")
        time.sleep(15)
        
        # Esperar y hacer clic en el botón
        download_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_btnSubmit"))
        )
        
        time.sleep(5)
        logging.info("Intentando la descarga...")
        
        driver.execute_script("""        
            var button = document.getElementById('ContentPlaceHolder1_btnSubmit');
            if(button) {
                button.click();
            }
        """)
        
        # Esperar a que se complete la descarga
        time.sleep(10)
        logging.info("Descarga completada exitosamente")
        
    except Exception as e:
        logging.error(f"Error durante la ejecución: {str(e)}")
        logging.error(f"URL actual: {driver.current_url if driver else 'No se pudo inicializar el driver'}")
        
    finally:
        if driver:
            # Capturar la pantalla en cualquier caso
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = os.path.join(download_path, f"error_{timestamp}.png")
            driver.save_screenshot(screenshot_path)
            logging.info(f"Captura de pantalla guardada en: {screenshot_path}")
            driver.quit()
        logging.info("Proceso finalizado")

if __name__ == "__main__":
    main()
