from rich.table import Table as tb
from rich.console import Console as cr
from obj_viv import Planta, Muro

from msg import Flag


def printTabla1(planta : Planta):

    # Lista de nombres de columnas
    column_names = ["ID muro", "longitud", "FE","Area Transvesal", "Area Tributaria","fy", "fyc", "f'c","f'm"]

    # Crear una tabla con las columnas
    table = tb(show_header=True, header_style="bold magenta", *column_names)


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

def printTabla2(planta_baja : Planta, planta_alta : Planta):
    muro : Muro
    #Lista de nombres de columnas
    column_names= ["Pu","PR","VER SI CUMPLE"]
    # Crear una tabla con las columnas
    table = tb(show_header=True, header_style="bold magenta",*column_names)

    
    
    
    for muro in planta_baja.muros:

        

        
        table.add_row(f"{muro.getPu()}",f"{muro.getPr()}",f"{muro.getCompPrPu()}")

    #Imprimir la tabla
    console = cr()
    console.print(table)
     

