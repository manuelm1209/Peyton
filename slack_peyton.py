# Importar selenium
from selenium import webdriver
# Importar techado para ingresar datos
from selenium.webdriver.common.keys import Keys
# Importar para esperar a que cargue la pagina
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class chat_slack:

    def __init__(self, user, password, reporte_slack):
        self.user = user
        self.password = password
        self.reporte_slack = reporte_slack

        # ruta driver chromedriver
        driver = webdriver.Chrome(executable_path=r"/Users/mac/dchrome/chromedriver")
        driver.get("https://slack.com/signin#/")
        # Longin

        espacio_trabajo = driver.find_element_by_xpath("// *[ @ id = 'domain']")
        espacio_trabajo.send_keys("imprimetuestilo")
        espacio_trabajo.send_keys(Keys.ENTER)
        usuario = driver.find_element_by_xpath("//*[@id='email']")
        usuario.send_keys(self.user)
        clave = driver.find_element_by_xpath("//*[@id='password']")
        clave.send_keys(self.password)
        clave.send_keys(Keys.ENTER)
        driver.get("https://app.slack.com/client/T010NH1AFH9/C014LC5JE0N")
        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='undefined']/p")))
        finally:
            espacio_texto = driver.find_element_by_xpath("//*[@id='undefined']/p")
            espacio_texto.send_keys("Acabo de subir los siguentes artículos:\n")
            for i in range(len(reporte_slack)):
                espacio_texto = driver.find_element_by_xpath("//*[@id='undefined']/p")
                espacio_texto.send_keys(str(i + 1) + ". " + reporte_slack[i][0] + " con nombre: " + reporte_slack[i][1] + ".\n")




        driver.quit()


