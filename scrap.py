##funciona

# import the required library
from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import glob

# Configurar la ruta de descarga (usando formato correcto para Windows)
download_path = os.path.abspath("./Smol_Holders")
os.makedirs(download_path, exist_ok=True)

print (f'directorio_1 = {download_path}')

# create a Driver instance with undetected_chromedriver (uc) and specific options
driver = Driver(uc=True, undetected=True)  # Aseguramos que undetected esté activado
# Establecer el directorio de descarga
driver.download_path = download_path

print(f"Directorio de descarga configurado: driver.download {driver.download_path}")

try:
    # navigate to the specified URL
    driver.get("https://arbiscan.io/exportData?type=tokenholders&contract=0x9e64d3b9e8ec387a9a58ced80b71ed815f8d82b5&decimal=18")
    
    # Esperar un tiempo considerable para que se cargue la página y se pase el Cloudflare
    print("Esperando que se cargue la página y se pase el Cloudflare...")
    time.sleep(15)  # Aumentamos el tiempo de espera inicial
    
    # Esperar a que el botón esté presente
    print("Buscando el botón de descarga...")
    download_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_btnSubmit"))
    )
    
    # Esperar un poco más para asegurarnos que la página está completamente cargada
    time.sleep(5)
    
    print("Intentando la descarga...")
    # Intentar el clic usando JavaScript
    driver.execute_script("""
        var button = document.getElementById('ContentPlaceHolder1_btnSubmit');
        if(button) {
            button.click();
        }
    """)


except Exception as e:
    print(f"Ocurrió un error: {str(e)}")
    # Tomar screenshot en caso de error
    driver.save_screenshot("error.png")
    # Imprimir la URL actual en caso de error
    print(f"URL actual: {driver.current_url}")

finally:
    time.sleep (8)
    driver.quit()