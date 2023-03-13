from obj_viv import Planta, Losa, Muro
import pandas as  pd

from msg import Flag

if __name__ == "__main__":

    file = pd.read_csv("ExcelTables\\tabladeentrada2.csv")

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

    planta_alta = Planta(muros,losa,100,70) 

    muro : Muro
    for muro in planta_alta.muros:

        Flag(f"Pu: {muro.getPu()}",47)

        
    


    pass