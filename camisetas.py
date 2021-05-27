# Importar selenium
import selenium
from selenium import webdriver

import os
# Importar techado para ingresar datos
from selenium.webdriver.common.keys import Keys
# Para poner un sleep para esperar que cargue las páginas
import time
# Importar para esperar a que cargue la pagina
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class cargar_camisetas:

    def __init__(self, user, password, archivos_txt, contador):
        self.user = user
        self.password = password
        self.archivos_txt = archivos_txt
        self.contador = contador

        # Leer arcrivo txt con encodign ISO-8859-1 para leer tíldes.
        with open((archivos_txt[contador][0] + "/" + archivos_txt[contador][1]), "r", encoding='ISO-8859-1') as archivo_txt:

            # ruta driver chromedriver
            driver = webdriver.Chrome(executable_path=r"/Users/mac/dchrome/chromedriver")
            driver.get("https://imprimetuestilo.com/wp-login")
            # Longin
            usuario = driver.find_element_by_id("user_login")
            usuario.send_keys(self.user)
            clave = driver.find_element_by_id("user_pass")
            clave.send_keys(self.password)
            clave.send_keys(Keys.ENTER)
            driver.get("https://imprimetuestilo.com/wp-admin/post.php?post=40183&action=edit")
            try:
                element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title")))
            finally:

                # Subir imagene principal.
                img_producto = driver.find_element_by_id("set-post-thumbnail")
                img_producto.click()
                time.sleep(2)

                if os.path.isfile(archivos_txt[contador][0] + "/" + archivos_txt[contador][1][:-4] + "-1.jpg"):
                    driver.find_element_by_xpath("//input[ @ type = 'file']").send_keys(
                        (archivos_txt[contador][0] + "/" + archivos_txt[contador][1][:-4] + "-1.jpg"))
                    time.sleep(1)
                    boton_establecer_imagen = driver.find_element_by_xpath(
                        "// *[ @ id = '__wp-uploader-id-0'] / div[4] / div / div[2] / button")
                    # Esperar hasta que el boton esté enable.
                    while not (boton_establecer_imagen.is_enabled()):
                        time.sleep(1)
                    texto = driver.find_element_by_id("attachment-details-alt-text")
                    texto.clear()
                    archivo_txt.seek(0)
                    texto.send_keys("Diseño " + archivo_txt.readlines()[1][:-1])
                    texto = driver.find_element_by_id("attachment-details-title")
                    texto.clear()
                    archivo_txt.seek(0)
                    texto.send_keys(archivo_txt.readlines()[1][:-1])
                    texto = driver.find_element_by_id("attachment-details-caption")
                    texto.clear()
                    archivo_txt.seek(0)
                    texto.send_keys("Camiseta personalizada " + archivo_txt.readlines()[1][:-1])
                    texto = driver.find_element_by_id("attachment-details-description")
                    texto.clear()
                    archivo_txt.seek(0)
                    texto.send_keys("Camiseta " + archivo_txt.readlines()[1][:-1])

                    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                    # boton_establecer_imagen = driver.find_element_by_xpath(
                    #     "// *[ @ id = '__wp-uploader-id-0'] / div[4] / div / div[2] / button")
                    # boton_establecer_imagen.click()
                elif os.path.isfile(archivos_txt[contador][0] + "/" + archivos_txt[contador][1][:-4] + "-1.png"):
                    driver.find_element_by_xpath("//input[ @ type = 'file']").send_keys(
                        (archivos_txt[contador][0] + "/" + archivos_txt[contador][1][:-4] + "-1.png"))
                    time.sleep(1)
                    boton_establecer_imagen = driver.find_element_by_xpath(
                        "// *[ @ id = '__wp-uploader-id-0'] / div[4] / div / div[2] / button")
                    # Esperar hasta que el boton esté enable.
                    while not (boton_establecer_imagen.is_enabled()):
                        time.sleep(1)
                    texto = driver.find_element_by_id("attachment-details-alt-text")
                    texto.clear()
                    archivo_txt.seek(0)
                    texto.send_keys("Diseño " + archivo_txt.readlines()[1][:-1])
                    texto = driver.find_element_by_id("attachment-details-title")
                    texto.clear()
                    archivo_txt.seek(0)
                    texto.send_keys(archivo_txt.readlines()[1][:-1])
                    texto = driver.find_element_by_id("attachment-details-caption")
                    texto.clear()
                    archivo_txt.seek(0)
                    texto.send_keys("Camiseta personalizada " + archivo_txt.readlines()[1][:-1])
                    texto = driver.find_element_by_id("attachment-details-description")
                    texto.clear()
                    archivo_txt.seek(0)
                    texto.send_keys("Camiseta " + archivo_txt.readlines()[1][:-1])


                    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                    # boton_establecer_imagen = driver.find_element_by_xpath(
                    #     "// *[ @ id = '__wp-uploader-id-0'] / div[4] / div / div[2] / button")
                    # boton_establecer_imagen.click()
                else:
                    reporte_errores = "*** ERROR ***\nNo se encontró la imagen principal Camiseta: " + archivos_txt[contador][1][:-4] + "-1"
                    print(reporte_errores)
                    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()


                # Añadir imágenes a la galeria del producto
                archivo_txt.seek(0)
                if int(archivo_txt.readlines()[2][:-1]) > 1:
                    archivo_txt.seek(0)
                    for i in range(int(archivo_txt.readlines()[2][:-1]) - 1):
                        time.sleep(1)
                        img_galeria = driver.find_element_by_xpath("//*[@id='woocommerce-product-images']/div/p/a")
                        img_galeria.click()
                        time.sleep(2)
                        if os.path.isfile(archivos_txt[contador][0] + "/" + archivos_txt[contador][1][:-4] + "-" + str(
                                    i + 2) + ".jpg"):
                            driver.find_element_by_xpath("//input[ @ type = 'file']").send_keys(
                                archivos_txt[contador][0] + "/" + archivos_txt[contador][1][:-4] + "-" + str(
                                    i + 2) + ".jpg")
                            time.sleep(1)
                            boton_establecer_imagen2 = driver.find_element_by_xpath(
                                "/ html / body / div[17] / div[1] / div / div / div[4] / div / div[2] / button")
                            # Esperar hasta que el boton esté enable.
                            while not (boton_establecer_imagen2.is_enabled()):
                                time.sleep(1)
                            texto = driver.find_element_by_xpath(
                                "/html/body/div[17]/div[1]/div/div/div[3]/div[2]/div/div[3]/div[2]/span[1]/input")
                            texto.clear()
                            archivo_txt.seek(0)
                            texto.send_keys("Diseño " + archivo_txt.readlines()[1][:-1])
                            texto = driver.find_element_by_xpath(
                                "/html/body/div[17]/div[1]/div/div/div[3]/div[2]/div/div[3]/div[2]/span[2]/input")
                            texto.clear()
                            archivo_txt.seek(0)
                            texto.send_keys(archivo_txt.readlines()[1][:-1])
                            texto = driver.find_element_by_xpath(
                                "/html/body/div[17]/div[1]/div/div/div[3]/div[2]/div/div[3]/div[2]/span[3]/textarea")
                            texto.clear()
                            archivo_txt.seek(0)
                            texto.send_keys("Camiseta personalizada " + archivo_txt.readlines()[1][:-1])
                            texto = driver.find_element_by_xpath(
                                "/html/body/div[17]/div[1]/div/div/div[3]/div[2]/div/div[3]/div[2]/span[4]/textarea")
                            texto.clear()
                            archivo_txt.seek(0)
                            texto.send_keys("Camiseta " + archivo_txt.readlines()[1][:-1])

                            # webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                            boton_establecer_imagen2 = driver.find_element_by_xpath(
                                "/ html / body / div[17] / div[1] / div / div / div[4] / div / div[2] / button")
                            boton_establecer_imagen2.click()

                        elif os.path.isfile(archivos_txt[contador][0] + "/" + archivos_txt[contador][1][:-4] + "-" + str(
                                        i + 2) + ".png"):

                            driver.find_element_by_xpath("//input[ @ type = 'file']").send_keys(
                                archivos_txt[contador][0] + "/" + archivos_txt[contador][1][:-4] + "-" + str(
                                    i + 2) + ".png")
                            time.sleep(1)
                            boton_establecer_imagen2 = driver.find_element_by_xpath(
                                "/ html / body / div[17] / div[1] / div / div / div[4] / div / div[2] / button")
                            # Esperar hasta que el boton esté enable.
                            while not (boton_establecer_imagen2.is_enabled()):
                                time.sleep(1)
                            texto = driver.find_element_by_xpath(
                                "/html/body/div[17]/div[1]/div/div/div[3]/div[2]/div/div[3]/div[2]/span[1]/input")
                            texto.clear()
                            archivo_txt.seek(0)
                            texto.send_keys("Diseño " + archivo_txt.readlines()[1][:-1])
                            texto = driver.find_element_by_xpath(
                                "/html/body/div[17]/div[1]/div/div/div[3]/div[2]/div/div[3]/div[2]/span[2]/input")
                            texto.clear()
                            archivo_txt.seek(0)
                            texto.send_keys(archivo_txt.readlines()[1][:-1])
                            texto = driver.find_element_by_xpath(
                                "/html/body/div[17]/div[1]/div/div/div[3]/div[2]/div/div[3]/div[2]/span[3]/textarea")
                            texto.clear()
                            archivo_txt.seek(0)
                            texto.send_keys("Camiseta personalizada " + archivo_txt.readlines()[1][:-1])
                            texto = driver.find_element_by_xpath(
                                "/html/body/div[17]/div[1]/div/div/div[3]/div[2]/div/div[3]/div[2]/span[4]/textarea")
                            texto.clear()
                            archivo_txt.seek(0)
                            texto.send_keys("Camiseta " + archivo_txt.readlines()[1][:-1])


                            boton_establecer_imagen2 = driver.find_element_by_xpath(
                                "/ html / body / div[17] / div[1] / div / div / div[4] / div / div[2] / button")
                            boton_establecer_imagen2.click()
                        else:
                            reporte_errores = "*** ERROR ***\nNo se encontró la imagen secundaria Camiseta: " + "/" + archivos_txt[contador][1][:-4] + "-" + str(i + 2)
                            print(reporte_errores)
                            webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()


                driver.execute_script("window.scroll(0, 0)")

                nuevo_borrador = driver.find_element_by_xpath("//*[@id='duplicate-action']/a")
                nuevo_borrador.click()


                # Subir imagene principal.

                img_producto = driver.find_element_by_id("set-post-thumbnail")
                img_producto.click()
                time.sleep(2)

                try:
                    time.sleep(3)


                    archivo_txt.seek(0)
                    lista_fotos = driver.find_element_by_xpath(
                        "/ html / body / div[17] / div[1] / div / div / div[3] / div[2] / div / ul / li["+ archivo_txt.readlines()[2][:-1] +"]")
                    lista_fotos.click()
                    boton_establecer_imagen = driver.find_element_by_xpath(
                        "/html/body/div[17]/div[1]/div/div/div[4]/div/div[2]/button")
                    boton_establecer_imagen.click()
                except:
                    time.sleep(3)


                    archivo_txt.seek(0)
                    lista_fotos = driver.find_element_by_xpath(
                        "/ html / body / div[16] / div[1] / div / div / div[3] / div[2] / div / ul / li[" +
                        archivo_txt.readlines()[2][:-1] + "]")
                    lista_fotos.click()
                    boton_establecer_imagen = driver.find_element_by_xpath(
                        "/html/body/div[16]/div[1]/div/div/div[4]/div/div[2]/button")
                    boton_establecer_imagen.click()


                # Subir imagen secundaria.

                archivo_txt.seek(0)
                if int(archivo_txt.readlines()[2][:-1]) > 1:
                    archivo_txt.seek(0)
                    cuenta_imagen = int(archivo_txt.readlines()[2][:-1]) - 1
                    archivo_txt.seek(0)
                    for i in range(int(archivo_txt.readlines()[2][:-1]) - 1):


                        time.sleep(1)
                        img_galeria = driver.find_element_by_xpath("//*[@id='woocommerce-product-images']/div/p/a")
                        time.sleep(1)
                        img_galeria.click()
                        time.sleep(2)
                        try:
                            time.sleep(2)
                            buscar_tallas = driver.find_element_by_xpath(
                                "/html/body/div[16]/div[1]/div/div/div[3]/div[2]/div/div[1]/div[2]/input")
                            while not (buscar_tallas.is_enabled()):
                                time.sleep(1)
                            buscar_tallas = driver.find_element_by_xpath(
                                "/html/body/div[16]/div[1]/div/div/div[3]/div[2]/div/div[1]/div[2]/input")
                            buscar_tallas.send_keys("a")
                            buscar_tallas.clear()
                            time.sleep(3)

                            lista_fotos = driver.find_element_by_xpath("/ html / body / div[16] / div[1] / div / div / div[3] / div[2] / div / ul / li[" + str(cuenta_imagen) + "]")
                            lista_fotos.click()
                            cuenta_imagen = cuenta_imagen - 1
                            boton_establecer_imagen = driver.find_element_by_xpath("/ html / body / div[16] / div[1] / div / div / div[4] / div / div[2] / button")
                            boton_establecer_imagen.click()
                        except:
                            time.sleep(2)
                            buscar_tallas = driver.find_element_by_xpath(
                                "/html/body/div[17]/div[1]/div/div/div[3]/div[2]/div/div[1]/div[2]/input")
                            while not (buscar_tallas.is_enabled()):
                                time.sleep(1)
                            buscar_tallas = driver.find_element_by_xpath(
                                "/html/body/div[17]/div[1]/div/div/div[3]/div[2]/div/div[1]/div[2]/input")
                            buscar_tallas.send_keys("a")
                            buscar_tallas.clear()
                            time.sleep(3)

                            lista_fotos = driver.find_element_by_xpath("/ html / body / div[17] / div[1] / div / div / div[3] / div[2] / div / ul / li[" + str(cuenta_imagen) + "]")
                            time.sleep(1)
                            lista_fotos.click()
                            cuenta_imagen = cuenta_imagen - 1
                            boton_establecer_imagen = driver.find_element_by_xpath("/ html / body / div[17] / div[1] / div / div / div[4] / div / div[2] / button")
                            boton_establecer_imagen.click()


                # Subir tallas hombre
                time.sleep(1)
                img_galeria = driver.find_element_by_xpath("//*[@id='woocommerce-product-images']/div/p/a")
                img_galeria.click()
                time.sleep(2)
                try:
                    buscar_tallas = driver.find_element_by_xpath(
                        "/html/body/div[16]/div[1]/div/div/div[3]/div[2]/div/div[1]/div[2]/input")
                    while not (buscar_tallas.is_enabled()):
                        time.sleep(1)
                    buscar_tallas = driver.find_element_by_xpath(
                        "/html/body/div[16]/div[1]/div/div/div[3]/div[2]/div/div[1]/div[2]/input")
                    buscar_tallas.clear()
                    buscar_tallas.send_keys("Tallas camiseta hombre")
                    time.sleep(3)
                    lista_fotos = driver.find_element_by_xpath(
                        "/ html / body / div[16] / div[1] / div / div / div[3] / div[2] / div / ul / li[1]")
                    lista_fotos.click()
                    boton_establecer_imagen = driver.find_element_by_xpath(
                        "/ html / body / div[16] / div[1] / div / div / div[4] / div / div[2] / button")
                    boton_establecer_imagen.click()
                    time.sleep(1)
                except:
                    buscar_tallas = driver.find_element_by_xpath(
                        "/html/body/div[17]/div[1]/div/div/div[3]/div[2]/div/div[1]/div[2]/input")
                    while not (buscar_tallas.is_enabled()):
                        time.sleep(1)
                    buscar_tallas = driver.find_element_by_xpath(
                        "/html/body/div[17]/div[1]/div/div/div[3]/div[2]/div/div[1]/div[2]/input")
                    buscar_tallas.clear()
                    buscar_tallas.send_keys("Tallas camiseta hombre")
                    time.sleep(3)
                    lista_fotos = driver.find_element_by_xpath(
                        "/ html / body / div[17] / div[1] / div / div / div[3] / div[2] / div / ul / li[1]")
                    lista_fotos.click()
                    boton_establecer_imagen = driver.find_element_by_xpath(
                        "/ html / body / div[17] / div[1] / div / div / div[4] / div / div[2] / button")
                    boton_establecer_imagen.click()
                    time.sleep(1)

                # Subir tallas mujer
                img_galeria = driver.find_element_by_xpath("//*[@id='woocommerce-product-images']/div/p/a")
                img_galeria.click()
                time.sleep(2)
                try:
                    buscar_tallas = driver.find_element_by_xpath(
                        "/html/body/div[16]/div[1]/div/div/div[3]/div[2]/div/div[1]/div[2]/input")
                    while not (buscar_tallas.is_enabled()):
                        time.sleep(1)
                    buscar_tallas = driver.find_element_by_xpath(
                        "/html/body/div[16]/div[1]/div/div/div[3]/div[2]/div/div[1]/div[2]/input")
                    buscar_tallas.clear()
                    buscar_tallas.send_keys("Tallas Camiseta Mujer")
                    time.sleep(3)
                    lista_fotos = driver.find_element_by_xpath(
                        "/ html / body / div[16] / div[1] / div / div / div[3] / div[2] / div / ul / li[1]")
                    lista_fotos.click()
                    boton_establecer_imagen = driver.find_element_by_xpath(
                        "/ html / body / div[16] / div[1] / div / div / div[4] / div / div[2] / button")
                    boton_establecer_imagen.click()
                    time.sleep(1)
                except:
                    buscar_tallas = driver.find_element_by_xpath(
                        "/html/body/div[17]/div[1]/div/div/div[3]/div[2]/div/div[1]/div[2]/input")
                    while not (buscar_tallas.is_enabled()):
                        time.sleep(1)
                    buscar_tallas = driver.find_element_by_xpath(
                        "/html/body/div[17]/div[1]/div/div/div[3]/div[2]/div/div[1]/div[2]/input")
                    buscar_tallas.clear()
                    buscar_tallas.send_keys("Tallas Camiseta Mujer")
                    time.sleep(3)
                    lista_fotos = driver.find_element_by_xpath(
                        "/ html / body / div[17] / div[1] / div / div / div[3] / div[2] / div / ul / li[1]")
                    lista_fotos.click()
                    boton_establecer_imagen = driver.find_element_by_xpath(
                        "/ html / body / div[17] / div[1] / div / div / div[4] / div / div[2] / button")
                    boton_establecer_imagen.click()
                    time.sleep(1)


                # Guardar borrador
                time.sleep(1)
                driver.execute_script("window.scroll(0, 0)")
                time.sleep(1)


                # Marcar tantas categorías como lineas hayan en el archivo txt desde la linea 4 [3].
                archivo_txt.seek(0)
                for i in range(len(archivo_txt.readlines()) - 4):
                    archivo_txt.seek(0)
                    categorias = driver.find_element_by_id("in-product_cat-" + archivo_txt.readlines()[i + 4][:-1])
                    categorias.click()
                archivo_txt.seek(0)
                tags = driver.find_element_by_id("new-tag-product_tag")
                tags.send_keys(archivo_txt.readlines()[3][:-1])
                tags.send_keys(Keys.ENTER)


                titulo = driver.find_element_by_id("title")
                titulo.clear()
                archivo_txt.seek(0)
                titulo.send_keys(archivo_txt.readlines()[1][:-1])
                time.sleep(1)


                guardar_borrador = driver.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[1]/input")
                guardar_borrador.click()
                time.sleep(5)
                guardar_borrador = driver.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[1]/input")
                while not (guardar_borrador.is_enabled()):
                    time.sleep(1)

                print("fin del codigo camisetas")
                time.sleep(2)


                driver.quit()




class cargar_hoodies:


    def __init__(self, user, password, archivos_txt, contador):
        self.user = user
        self.password = password
        self.archivos_txt = archivos_txt
        self.contador = contador

        # Leer arcrivo txt con encodign ISO-8859-1 para leer tíldes.
        with open((archivos_txt[contador][0] + "/" + archivos_txt[contador][1]), "r", encoding='ISO-8859-1') as archivo_txt:

            # ruta driver chromedriver
            driver = webdriver.Chrome(executable_path=r"/Users/mac/dchrome/chromedriver")
            driver.get("https://imprimetuestilo.com/wp-login")
            # Longin
            usuario = driver.find_element_by_id("user_login")
            usuario.send_keys(self.user)
            clave = driver.find_element_by_id("user_pass")
            clave.send_keys(self.password)
            clave.send_keys(Keys.ENTER)
            driver.get("https://imprimetuestilo.com/wp-admin/post.php?post=40859&action=edit")
            try:
                element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title")))
            finally:

                # Subir imagene principal.
                img_producto = driver.find_element_by_id("set-post-thumbnail")
                img_producto.click()
                time.sleep(2)

                if os.path.isfile(archivos_txt[contador][0] + "/" + archivos_txt[contador][1][:-4] + "-1.jpg"):
                    driver.find_element_by_xpath("//input[ @ type = 'file']").send_keys(
                        (archivos_txt[contador][0] + "/" + archivos_txt[contador][1][:-4] + "-1.jpg"))
                    time.sleep(1)
                    boton_establecer_imagen = driver.find_element_by_xpath(
                        "// *[ @ id = '__wp-uploader-id-0'] / div[4] / div / div[2] / button")
                    # Esperar hasta que el boton esté enable.
                    while not (boton_establecer_imagen.is_enabled()):
                        time.sleep(1)
                    texto = driver.find_element_by_id("attachment-details-alt-text")
                    texto.clear()
                    archivo_txt.seek(0)
                    texto.send_keys("Diseño " + archivo_txt.readlines()[1][:-1])
                    texto = driver.find_element_by_id("attachment-details-title")
                    texto.clear()
                    archivo_txt.seek(0)
                    texto.send_keys(archivo_txt.readlines()[1][:-1])
                    texto = driver.find_element_by_id("attachment-details-caption")
                    texto.clear()
                    archivo_txt.seek(0)
                    texto.send_keys("Hoodie personalizado " + archivo_txt.readlines()[1][:-1])
                    texto = driver.find_element_by_id("attachment-details-description")
                    texto.clear()
                    archivo_txt.seek(0)
                    texto.send_keys("Hoodie " + archivo_txt.readlines()[1][:-1])

                    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                    # boton_establecer_imagen = driver.find_element_by_xpath(
                    #     "// *[ @ id = '__wp-uploader-id-0'] / div[4] / div / div[2] / button")
                    # boton_establecer_imagen.click()
                elif os.path.isfile(archivos_txt[contador][0] + "/" + archivos_txt[contador][1][:-4] + "-1.png"):
                    driver.find_element_by_xpath("//input[ @ type = 'file']").send_keys(
                        (archivos_txt[contador][0] + "/" + archivos_txt[contador][1][:-4] + "-1.png"))
                    time.sleep(1)
                    boton_establecer_imagen = driver.find_element_by_xpath(
                        "// *[ @ id = '__wp-uploader-id-0'] / div[4] / div / div[2] / button")
                    # Esperar hasta que el boton esté enable.
                    while not (boton_establecer_imagen.is_enabled()):
                        time.sleep(1)
                    texto = driver.find_element_by_id("attachment-details-alt-text")
                    texto.clear()
                    archivo_txt.seek(0)
                    texto.send_keys("Diseño " + archivo_txt.readlines()[1][:-1])
                    texto = driver.find_element_by_id("attachment-details-title")
                    texto.clear()
                    archivo_txt.seek(0)
                    texto.send_keys(archivo_txt.readlines()[1][:-1])
                    texto = driver.find_element_by_id("attachment-details-caption")
                    texto.clear()
                    archivo_txt.seek(0)
                    texto.send_keys("Hoodie personalizado " + archivo_txt.readlines()[1][:-1])
                    texto = driver.find_element_by_id("attachment-details-description")
                    texto.clear()
                    archivo_txt.seek(0)
                    texto.send_keys("Hoodie " + archivo_txt.readlines()[1][:-1])

                    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                    # boton_establecer_imagen = driver.find_element_by_xpath(
                    #     "// *[ @ id = '__wp-uploader-id-0'] / div[4] / div / div[2] / button")
                    # boton_establecer_imagen.click()
                else:
                    reporte_errores = "*** ERROR ***\nNo se encontró la imagen principal Camiseta: " + \
                                      archivos_txt[contador][1][:-4] + "-1"
                    print(reporte_errores)
                    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

                # Añadir imágenes a la galeria del producto
                archivo_txt.seek(0)
                if int(archivo_txt.readlines()[2][:-1]) > 1:
                    archivo_txt.seek(0)
                    for i in range(int(archivo_txt.readlines()[2][:-1]) - 1):
                        time.sleep(1)
                        img_galeria = driver.find_element_by_xpath("//*[@id='woocommerce-product-images']/div/p/a")
                        img_galeria.click()
                        time.sleep(2)
                        if os.path.isfile(archivos_txt[contador][0] + "/" + archivos_txt[contador][1][:-4] + "-" + str(
                                i + 2) + ".jpg"):
                            driver.find_element_by_xpath("//input[ @ type = 'file']").send_keys(
                                archivos_txt[contador][0] + "/" + archivos_txt[contador][1][:-4] + "-" + str(
                                    i + 2) + ".jpg")
                            time.sleep(1)
                            boton_establecer_imagen2 = driver.find_element_by_xpath(
                                "/ html / body / div[17] / div[1] / div / div / div[4] / div / div[2] / button")
                            # Esperar hasta que el boton esté enable.
                            while not (boton_establecer_imagen2.is_enabled()):
                                time.sleep(1)
                            texto = driver.find_element_by_xpath(
                                "/html/body/div[17]/div[1]/div/div/div[3]/div[2]/div/div[3]/div[2]/span[1]/input")
                            texto.clear()
                            archivo_txt.seek(0)
                            texto.send_keys("Diseño " + archivo_txt.readlines()[1][:-1])
                            texto = driver.find_element_by_xpath(
                                "/html/body/div[17]/div[1]/div/div/div[3]/div[2]/div/div[3]/div[2]/span[2]/input")
                            texto.clear()
                            archivo_txt.seek(0)
                            texto.send_keys(archivo_txt.readlines()[1][:-1])
                            texto = driver.find_element_by_xpath(
                                "/html/body/div[17]/div[1]/div/div/div[3]/div[2]/div/div[3]/div[2]/span[3]/textarea")
                            texto.clear()
                            archivo_txt.seek(0)
                            texto.send_keys("Hoodie personalizado " + archivo_txt.readlines()[1][:-1])
                            texto = driver.find_element_by_xpath(
                                "/html/body/div[17]/div[1]/div/div/div[3]/div[2]/div/div[3]/div[2]/span[4]/textarea")
                            texto.clear()
                            archivo_txt.seek(0)
                            texto.send_keys("Hoodie " + archivo_txt.readlines()[1][:-1])

                            # webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                            boton_establecer_imagen2 = driver.find_element_by_xpath(
                                "/ html / body / div[17] / div[1] / div / div / div[4] / div / div[2] / button")
                            boton_establecer_imagen2.click()

                        elif os.path.isfile(archivos_txt[contador][0] + "/" + archivos_txt[contador][1][:-4] + "-" + str(
                                i + 2) + ".png"):

                            driver.find_element_by_xpath("//input[ @ type = 'file']").send_keys(
                                archivos_txt[contador][0] + "/" + archivos_txt[contador][1][:-4] + "-" + str(
                                    i + 2) + ".png")
                            time.sleep(1)
                            boton_establecer_imagen2 = driver.find_element_by_xpath(
                                "/ html / body / div[17] / div[1] / div / div / div[4] / div / div[2] / button")
                            # Esperar hasta que el boton esté enable.
                            while not (boton_establecer_imagen2.is_enabled()):
                                time.sleep(1)
                            texto = driver.find_element_by_xpath(
                                "/html/body/div[17]/div[1]/div/div/div[3]/div[2]/div/div[3]/div[2]/span[1]/input")
                            texto.clear()
                            archivo_txt.seek(0)
                            texto.send_keys("Diseño " + archivo_txt.readlines()[1][:-1])
                            texto = driver.find_element_by_xpath(
                                "/html/body/div[17]/div[1]/div/div/div[3]/div[2]/div/div[3]/div[2]/span[2]/input")
                            texto.clear()
                            archivo_txt.seek(0)
                            texto.send_keys(archivo_txt.readlines()[1][:-1])
                            texto = driver.find_element_by_xpath(
                                "/html/body/div[17]/div[1]/div/div/div[3]/div[2]/div/div[3]/div[2]/span[3]/textarea")
                            texto.clear()
                            archivo_txt.seek(0)
                            texto.send_keys("Hoodie personalizado " + archivo_txt.readlines()[1][:-1])
                            texto = driver.find_element_by_xpath(
                                "/html/body/div[17]/div[1]/div/div/div[3]/div[2]/div/div[3]/div[2]/span[4]/textarea")
                            texto.clear()
                            archivo_txt.seek(0)
                            texto.send_keys("Hoodie " + archivo_txt.readlines()[1][:-1])

                            boton_establecer_imagen2 = driver.find_element_by_xpath(
                                "/ html / body / div[17] / div[1] / div / div / div[4] / div / div[2] / button")
                            boton_establecer_imagen2.click()
                        else:
                            reporte_errores = "*** ERROR ***\nNo se encontró la imagen secundaria Camiseta: " + "/" + \
                                              archivos_txt[contador][1][:-4] + "-" + str(i + 2)
                            print(reporte_errores)
                            webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

                driver.execute_script("window.scroll(0, 0)")

                nuevo_borrador = driver.find_element_by_xpath("//*[@id='duplicate-action']/a")
                nuevo_borrador.click()

                # Subir imagene principal.

                img_producto = driver.find_element_by_id("set-post-thumbnail")
                img_producto.click()
                time.sleep(2)

                try:
                    time.sleep(3)

                    archivo_txt.seek(0)
                    lista_fotos = driver.find_element_by_xpath(
                        "/ html / body / div[17] / div[1] / div / div / div[3] / div[2] / div / ul / li[" +
                        archivo_txt.readlines()[2][:-1] + "]")
                    lista_fotos.click()
                    boton_establecer_imagen = driver.find_element_by_xpath(
                        "/html/body/div[17]/div[1]/div/div/div[4]/div/div[2]/button")
                    boton_establecer_imagen.click()
                except:
                    time.sleep(3)

                    archivo_txt.seek(0)
                    lista_fotos = driver.find_element_by_xpath(
                        "/ html / body / div[16] / div[1] / div / div / div[3] / div[2] / div / ul / li[" +
                        archivo_txt.readlines()[2][:-1] + "]")
                    lista_fotos.click()
                    boton_establecer_imagen = driver.find_element_by_xpath(
                        "/html/body/div[16]/div[1]/div/div/div[4]/div/div[2]/button")
                    boton_establecer_imagen.click()

                # Subir imagen secundaria.

                archivo_txt.seek(0)
                if int(archivo_txt.readlines()[2][:-1]) > 1:
                    archivo_txt.seek(0)
                    cuenta_imagen = int(archivo_txt.readlines()[2][:-1]) - 1
                    archivo_txt.seek(0)
                    for i in range(int(archivo_txt.readlines()[2][:-1]) - 1):

                        time.sleep(1)
                        img_galeria = driver.find_element_by_xpath("//*[@id='woocommerce-product-images']/div/p/a")
                        time.sleep(1)
                        img_galeria.click()
                        time.sleep(2)
                        try:
                            time.sleep(2)
                            buscar_tallas = driver.find_element_by_xpath(
                                "/html/body/div[16]/div[1]/div/div/div[3]/div[2]/div/div[1]/div[2]/input")
                            while not (buscar_tallas.is_enabled()):
                                time.sleep(1)
                            buscar_tallas = driver.find_element_by_xpath(
                                "/html/body/div[16]/div[1]/div/div/div[3]/div[2]/div/div[1]/div[2]/input")
                            buscar_tallas.send_keys("a")
                            buscar_tallas.clear()
                            time.sleep(3)

                            lista_fotos = driver.find_element_by_xpath(
                                "/ html / body / div[16] / div[1] / div / div / div[3] / div[2] / div / ul / li[" + str(
                                    cuenta_imagen) + "]")
                            lista_fotos.click()
                            cuenta_imagen = cuenta_imagen - 1
                            boton_establecer_imagen = driver.find_element_by_xpath(
                                "/ html / body / div[16] / div[1] / div / div / div[4] / div / div[2] / button")
                            boton_establecer_imagen.click()
                        except:
                            time.sleep(2)
                            buscar_tallas = driver.find_element_by_xpath(
                                "/html/body/div[17]/div[1]/div/div/div[3]/div[2]/div/div[1]/div[2]/input")
                            while not (buscar_tallas.is_enabled()):
                                time.sleep(1)
                            buscar_tallas = driver.find_element_by_xpath(
                                "/html/body/div[17]/div[1]/div/div/div[3]/div[2]/div/div[1]/div[2]/input")
                            buscar_tallas.send_keys("a")
                            buscar_tallas.clear()
                            time.sleep(3)

                            lista_fotos = driver.find_element_by_xpath(
                                "/ html / body / div[17] / div[1] / div / div / div[3] / div[2] / div / ul / li[" + str(
                                    cuenta_imagen) + "]")
                            time.sleep(1)
                            lista_fotos.click()
                            cuenta_imagen = cuenta_imagen - 1
                            boton_establecer_imagen = driver.find_element_by_xpath(
                                "/ html / body / div[17] / div[1] / div / div / div[4] / div / div[2] / button")
                            boton_establecer_imagen.click()


                # Guardar borrador
                time.sleep(1)
                driver.execute_script("window.scroll(0, 0)")
                time.sleep(1)

                # Marcar tantas categorías como lineas hayan en el archivo txt desde la linea 4 [3].
                archivo_txt.seek(0)
                for i in range(len(archivo_txt.readlines()) - 4):
                    archivo_txt.seek(0)
                    categorias = driver.find_element_by_id("in-product_cat-" + archivo_txt.readlines()[i + 4][:-1])
                    categorias.click()
                archivo_txt.seek(0)
                tags = driver.find_element_by_id("new-tag-product_tag")
                tags.send_keys(archivo_txt.readlines()[3][:-1])
                tags.send_keys(Keys.ENTER)

                titulo = driver.find_element_by_id("title")
                titulo.clear()
                archivo_txt.seek(0)
                titulo.send_keys(archivo_txt.readlines()[1][:-1])
                time.sleep(1)

                guardar_borrador = driver.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[1]/input")
                guardar_borrador.click()
                time.sleep(5)
                guardar_borrador = driver.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[1]/input")
                while not (guardar_borrador.is_enabled()):
                    time.sleep(1)

                print("fin del codigo Hoodie")
                time.sleep(2)

                driver.quit()




class crear_pagina_afiliado:

    def __init__(self, user, password):
        self.user = user
        self.password = password

        # ruta driver chromedriver
        driver = webdriver.Chrome(executable_path=r"/Users/mac/dchrome/chromedriver")
        driver.get("https://imprimetuestilo.com/wp-login")
        # Longin
        usuario = driver.find_element_by_id("user_login")
        usuario.send_keys(self.user)
        clave = driver.find_element_by_id("user_pass")
        clave.send_keys(self.password)
        clave.send_keys(Keys.ENTER)
        driver.get("https://imprimetuestilo.com/wp-admin/post-new.php?post_type=page")

        url_afiliado = input("Ingresa la dirección de la página. https://imprimetuestilo.com/")
        nombre_tienda = input("Ingresa el nombre de la tienda: ")
        nombre_imagen = input("Ingresa el nombre del logo con la extención: ")
        titulo_pagina = driver.find_element_by_xpath("// *[ @ id = 'post-title-0']")
        titulo_pagina.send_keys(url_afiliado)

        elementor = driver.find_element_by_xpath("//*[@id='elementor-switch-mode-button']/span[2]")
        elementor.click()

        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "elementor-panel-elements-search-input")))
        finally:
            agregar_bloque = driver.find_element_by_xpath("// *[ @ id = 'elementor-add-new-section'] / div / div[2] / div[2]")
            agregar_bloque.click()
            # ir a pestaña "Mis Plantillas"
            mis_plantillas = driver.find_element_by_xpath(
                "// *[ @ id = 'elementor-template-library-header-menu'] / div[3]")
            mis_plantillas.click()



        time.sleep(10)
        driver.quit()

