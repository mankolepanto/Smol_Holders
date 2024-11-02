from seleniumbase import Driver
import time
from selenium.webdriver.common.by import By


driver = Driver (uc= True)

try:
    driver.get ('https://arbiscan.io/exportData?type=tokenholders&contract=0x9e64d3b9e8ec387a9a58ced80b71ed815f8d82b5&decimal=18')
    driver.sleep (4)
    driver.uc_gui_click_captcha ()
    # Encuentra el elemento que quieres hacer clic
    element = driver.find_element(By.CSS_SELECTOR, "#ContentPlaceHolder1_btnSubmit")

    # Ejecuta el clic con JavaScript
    driver.execute_script("arguments[0].click();", element)
    driver.save_screenshot("error.png")

finally:
    time.sleep (10)
    driver.quit ()

