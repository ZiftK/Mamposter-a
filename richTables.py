from rich.table import Table as tb
from rich.console import Console as cr
from obj_viv import Planta, Muro

from msg import Flag


def printTabla1(planta : Planta):

    # Lista de nombres de columnas
    column_names = ["ID muro", "longitud", "FE","Area Transvesal", "Area Tributaria","fy", "fyc", "f'c","f'm"]

    # Crear una tabla con las columnas
    table = tb(show_header=True, header_style="bold magenta", *column_names,title="\n\nDatos de muros")


    muro : Muro
    # Agregar las filas a la tabla
    for muro in planta.muros:
        
        table.add_row\
            (f"{muro.id}",\
            f"{muro.longitud}",\
            f"{muro.fe}",\
            f"{muro.getAreaTransversal()}", \
            f"{muro.at_muros}",\
            f"{muro.castillo.fy/10000}", \
            f"{muro.castillo.fyc/10000}", \
            f"{muro.castillo.fc/10000}", \
            f"{muro.fm/10000}",)

    # Imprimir la tabla
    console = cr()
    console.print(table)

    pass


#__________________COMPARACION___________________________
def printTabla_planta_alta_comp(planta_alta : Planta):
    muro : Muro
    #Lista de nombres de columnas
    column_names= ["Pu","PR","VER SI CUMPLE"]
    # Crear una tabla con las columnas
    table = tb(show_header=True, header_style="bold magenta",*column_names,title="\n\nComparacion de Pu y PR En Planta Alta")

    
    
    
    for muro in planta_alta.muros:

        
        table.add_row(f"{muro.getPu()}",f"{muro.getPr()}",f"{muro.getCompPrPu()}")

    #Imprimir la tabla
    console = cr()
    console.print(table)

def printTabla_planta_baja_comp(planta_baja : Planta,planta_alta : Planta):

    planta_baja+=planta_alta
    muro : Muro
    #Lista de nombres de columnas
    column_names= ["Pu","PR","VER SI CUMPLE"]
    # Crear una tabla con las columnas
    table = tb(show_header=True, header_style="bold magenta",*column_names,title="\n\nComparacion de Pu y PR En Planta Baja")

    
    
    
    for muro in planta_baja.muros:

        
        table.add_row(f"{muro.getPu()}",f"{muro.getPr()}",f"{muro.getCompPrPu()}")

    #Imprimir la tabla
    console = cr()
    console.print(table)

#_____________________CALCULO DE PU________________________________

def printTabla_planta_alta_pu(planta_alta : Planta):
    muro : Muro
    #Lista de nombres de columnas
    column_names= ["ID Muro","Pu"]
    # Crear una tabla con las columnas
    table = tb(show_header=True, header_style="bold magenta",*column_names,title="\n\nValores de Pu de cada muro")

    for muro in planta_alta.muros:

        
        table.add_row(f"{muro.id}",f"{muro.getPu()}")


def printTabla_planta_baja_pu(planta_baja : Planta, planta_alta : Planta):
    planta_baja+= planta_alta
    muro : Muro
    #Lista de nombres de columnas
    column_names= ["ID Muro","Pu"]
    # Crear una tabla con las columnas
    table = tb(show_header=True, header_style="bold magenta",*column_names,title="\n\nValores de Pu de cada muro")

    for muro in planta_baja.muros:

        
        table.add_row(f"{muro.id}",f"{muro.getPu()}")


#____________________CARGA VIVA, CARGA MUERTA___________________________________________________
def printTabla_planta_alta_cvcm(planta_baja : Planta, planta_alta: Planta):
    muro : Muro 
    #Lista de nombres de columnas
    column_names= ["ID Muro","Carga Muerta","Carga Viva"]
    #Crear Una Tabla Con Columnas
    table = tb(show_header=True,header_style="bold magenta",*column_names,title="\n\nValores de Carga Viva y de Carga Muerta para cada muro")
    for muro in planta_alta.muros:

        
        table.add_row(f"{muro.id}",f"{muro.getPesoCm()}",f"{muro.getPesoCv}")

def printTabla_planta_bajacvcm(planta_baja : Planta, planta_alta: Planta):
    planta_baja+planta_alta
    muro : Muro 
    #Lista de nombres de columnas
    column_names= ["ID Muro","Carga Muerta","Carga Viva"]
    #Crear Una Tabla Con Columnas
    table = tb(show_header=True,header_style="bold magenta",*column_names,title="\n\nValores de Carga Viva y de Carga Muerta para cada muro")
    for muro in planta_baja.muros:

        
        table.add_row(f"{muro.id}",f"{muro.getPesoCm()}",f"{muro.getPesoCv}")



#_______________Peso Muro____________________
def printTabla_planta_alta_pesomuro(planta_alta: Planta):
    muro : Muro 
    #Lista de nombres de columnas
    column_names= ["ID Muro","Peso de Muro"]
    #Crear Una Tabla Con Columnas
    table = tb(show_header=True,header_style="bold magenta",*column_names,title="Peso del Muro")
    for muro in planta_alta.muros:

        
        table.add_row(f"{muro.id}",f"{muro.getPesoML()}")


def printTabla_planta_baja_pesomuro(planta_baja : Planta,planta_alta: Planta):
    planta_baja+= planta_alta
    muro : Muro 
    #Lista de nombres de columnas
    column_names= ["ID Muro","Peso de Muro"]
    #Crear Una Tabla Con Columnas
    table = tb(show_header=True,header_style="bold magenta",*column_names,title="Peso del Muro")
    for muro in planta_alta.muros:

        
        table.add_row(f"{muro.id}",f"{muro.getPesoML()}")


#_____________PV____________________________
def printTabla_planta_alta_pv(planta_alta: Planta):
    
    muro : Muro 
    #Lista de nombres de columnas
    column_names= ["ID Muro","Pv"]
    #Crear Una Tabla Con Columnas
    table = tb(show_header=True,header_style="bold magenta",*column_names)
    for muro in planta_alta.muros:

        
        table.add_row(f"{muro.id}",f"{muro.getPesoML()}")