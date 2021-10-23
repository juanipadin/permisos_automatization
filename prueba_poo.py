from selenium import webdriver
import Datos

url= 'https://formulario-ddjj.argentina.gob.ar/certificado/caba/categoria/5'

class Inicio:

    def click (elemento):
        driver = webdriver.Chrome().get(url)
        return (driver.find_element_by_xpath(elemento).click())

    def input (ubicacion,dato):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        return driver.find_element_by_xpath(ubicacion).send_keys(dato)

Inicio.input("""//*[@id="nombre"]""",Datos.nombre)



Inicio.click("""//*[@id="accordion"]/div/div/div[2]/label""")


#completar=["""//*[@id="nombre"]""","""//*[@id="apellido"]""","""//*[@id="dni"]""","""//*[@id="dni_confirm"]""","""//*[@id="nro_tramite"]"""]
#Datos=Datos.tolist()

#for completars in completar:
#    print(completars)
