from selenium import webdriver
import Datos

url_GBA= 'https://formulario-ddjj.argentina.gob.ar/certificado/gba/categoria/5'
url_CABA= 'https://formulario-ddjj.argentina.gob.ar/certificado/caba/categoria/5'
url_BSAS= 'https://formulario-ddjj.argentina.gob.ar/certificado/buenos-aires/categoria/5'
recibo="C:\\Users\\sribecky\\Documents\\PythonProjects\\Auto_Permiso\\Citacion Cristaldo.jpg"


driver = webdriver.Chrome()
driver.maximize_window()
if Datos.dom_lab_prov == "GBA":
    driver.get(url_GBA)
elif Datos.dom_lab_prov == "CABA":
    driver.get(url_CABA)
elif Datos.dom_lab_prov == "Bs. As.":
    driver.get (url_BSAS)
driver.find_element_by_xpath("""//*[@id="accordion"]/div/div/div[2]/label""").click()
driver.find_element_by_xpath("""//*[@id="nombre"]""").send_keys(Datos.nombre)
driver.find_element_by_xpath("""//*[@id="apellido"]""").send_keys(Datos.apellido)
driver.find_element_by_xpath("""//*[@id="dni"]""").send_keys(Datos.dni)
driver.find_element_by_xpath("""//*[@id="dni_confirm"]""").send_keys(Datos.dni)
driver.find_element_by_xpath("""//*[@id="nro_tramite"]""").send_keys(Datos.nro_tramite)
driver.find_element_by_xpath("""//*[@id="nro_tramite_confirm"]""").send_keys(Datos.nro_tramite)
if Datos.genero == "Masculino":
    driver.find_element_by_xpath("""//*[@id="genero"]/option[3]""").click()
else:
    driver.find_element_by_xpath("""//*[@id="genero"]/option[2]""").click()
driver.find_element_by_xpath("""//*[@id="cuil"]""").send_keys(Datos.cuil)

driver.find_element_by_xpath("""//*[@id="cel_cod_area"]""").send_keys(Datos.area_celular)
driver.find_element_by_xpath("""//*[@id="cel_numero"]""").send_keys(Datos.celular)
driver.find_element_by_xpath("""//*[@id="email"]""").send_keys(Datos.mail)
driver.find_element_by_xpath("""//*[@id="email_confirm"]""").send_keys(Datos.mail)
driver.find_element_by_xpath("""//*[@id="domicilio_domicilio"]""").send_keys(Datos.domicilio)
driver.find_element_by_xpath("""//*[@id="domicilio_domicilio_info_adicional"]""").send_keys(Datos.domicilio2)
driver.find_element_by_xpath("""//*[@id="domicilio_cod_postal"]""").send_keys(Datos.cp)
if Datos.provincia == "CABA":
    driver.find_element_by_xpath("""//*[@id="domicilio_provincia_iso"]/option[10]""").click()
elif Datos.provincia == "GBA":
    driver.find_element_by_xpath("""//*[@id="domicilio_provincia_iso"]/option[2]""").click()
elif Datos.provincia == "Bs. As.":
    driver.find_element_by_xpath("""//*[@id="domicilio_provincia_iso"]/option[3]""").click()
else:
    driver.find_element_by_xpath("""//*[@id="domicilio_provincia_iso"]/option[46]""").click()
driver.find_element_by_xpath("""//*[@id="domicilio_localidad"]""").send_keys(Datos.localidad)
driver.find_element_by_xpath("""//*[@id="laboral_cuit_empleador"]""").send_keys(Datos.cuit_empleador)
driver.find_element_by_xpath("""//*[@id="actividad_profesional"]""").send_keys(Datos.actividad)

driver.find_element_by_xpath("""//*[@id="form-cuhc"]/div[25]/div[1]/label""").click()
driver.find_element_by_xpath("""//*[@id="patente_vehiculo1"]""").send_keys(Datos.patente)

driver.find_element_by_xpath("""//*[@id="laboral_fecha_inicio_actividad"]""").send_keys(Datos.inicio)
driver.find_element_by_xpath("""//*[@id="laboral_domicilio_domicilio"]""").send_keys(Datos.dom_laboral)
driver.find_element_by_xpath("""//*[@id="laboral_domicilio_domicilio_info_adicional"]""").send_keys(Datos.dom_laboral2)
driver.find_element_by_xpath("""//*[@id="laboral_domicilio_cod_postal"]""").send_keys(Datos.cp_laboral)
driver.find_element_by_xpath("""//*[@id="laboral_domicilio_provincia_iso"]/option[2]""").click()
driver.find_element_by_xpath("""//*[@id="laboral_domicilio_localidad"]""").send_keys(Datos.dom_lab_loc)
driver.find_element_by_xpath("""//*[@id="laboral_empresa"]""").send_keys(Datos.empleador)
driver.find_element_by_xpath("""//*[@id="laboral_telefono"]""").send_keys(Datos.tel_empleador)

driver.find_element_by_xpath("""//*[@id="laboral_archivo_comprobante"]""").send_keys(recibo)


driver.find_element_by_xpath("""//*[@id="form-cuhc"]/div[41]/div""").click()
driver.find_element_by_xpath("""//*[@id="form-cuhc"]/div[42]/div[1]/label""").click()