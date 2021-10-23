from pandas import read_excel
import re

data="C:\\Users\\sribecky\\Documents\\PythonProjects\\Auto_Permiso\\Datos_Permiso.xlsx"

dato_excel=read_excel(data)
base=dato_excel["Resultado"].tolist()
nombre=base[0]
apellido=base[1]
dni=base[2]
nro_tramite=base[3]
genero=base[4]
cuil=base[5]
area_celular=base[6]
celular=base[7]
mail=base[8]
domicilio=base[9]
domicilio2=base[10]
cp=base[11]
provincia=base[12]
localidad=base[13]
cuit_empleador=base[14]
actividad=base[15]
patente=base[16]
#inicio=base[17]
dom_laboral=base[18]
dom_laboral2=base[19]
cp_laboral=base[20]
dom_lab_prov=base[21]
dom_lab_loc=base[22]
empleador=base[23]
tel_empleador=base[24]


def change_date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3/\\2/\\1', dt)
dt1 = str(base[17].date())

inicio=change_date_format(dt1)