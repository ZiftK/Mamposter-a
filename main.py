from rich.console import Console
from rich.table import Table
import pandas as pd
import richTables as rt
from obj_viv import Planta, Muro, Losa
console = Console()

if True:#*Enlistado de variables

    ##RH Cantidad de acero longitudinal y refuerzo transversal
    ##fc´ -> resostemcia a compresión
    ##fy´-> resistencia a compresión del acero
    ##bc -> base del castillo
    ##hc -> lado largo del castillo
    ##s -> separación de los estribos

    ##RH Orden
    #1.-área de losa
    #2.-área libre entre piso
    #3.-espesor de los muros
    #4.-peso de losa asotea
    #5.-peso de losa entre piso
    #6.-longitud total de planta alta y baja
    #7.-peso por metro lineal del muro
 
    pass

if __name__ == "__main__":

    file = pd.read_csv("MAMPOSTERIA\\ExcelTables\\tabladeentrada2.csv")

    frame = pd.DataFrame(file)

    
    muros = []

    for index in range(frame.shape[0]):

        

        fy = frame.loc[index,"fy"]
        fyc = frame.loc[index, "fyc"]
        bc =  frame.loc[index, "bc"]
        hc =  frame.loc[index, "hc"]
        fc = frame.loc[index, "fc"]
        

        castillo = Muro.Castillo(fy,fyc,bc,hc,fc,)

        id = frame.loc[index,"ID muro"]
        longitud = frame.loc[index,"longitud"]
        atributaria = frame.loc[index,"Area Tributaria"]
        fe = frame.loc[index,"FE"]
        peso_mc_material = frame.loc[index,"peso pieza"]
        altura_libre = frame.loc[index,"altura libre"]
        pesos_add = frame.loc[index,"peso add"]
        fm = frame.loc[index,"fm"]
        muro = Muro(id,longitud,fe,peso_mc_material,altura_libre,fm,castillo,atributaria,cm_muro=1.3,cv_muro=1.5,)

        muros.append(muro)

    losa = Losa(80,240, peso_add_m2 = 6.5+56+76+30+20) #losa azotea

    planta = Planta(muros,losa,100,70) #planta alta

    rt.printTabla1(planta)





    for index in range(frame.shape[0]):


    

        id = frame.loc[index,"ID muro"]
        longitud = frame.loc[index,"longitud"]
        atributaria = frame.loc[index,"Area Tributaria"]
        fe = frame.loc[index,"FE"]
        peso_mc_material = frame.loc[index,"peso pieza"]
        altura_libre = frame.loc[index,"altura libre"]
        pesos_add = frame.loc[index,"peso add"]
        fm = frame.loc[index,"fm"]
        muro = Muro(id,longitud,fe,peso_mc_material,altura_libre,fm,castillo,atributaria,cm_muro=1.3,cv_muro=1.5,)

        muros.append(muro)
    
    losa_entrepiso = Losa(80,240,peso_add_m2 = 38+5+40+50) #Losa entrepiso
    planta_alta = Planta(muros,losa_entrepiso,190,100) #planta baja

    
    rt.printTabla2(planta,planta)

        
    


    pass


