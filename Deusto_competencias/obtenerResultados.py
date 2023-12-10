import re
import os
import webScrappingDeusto

#ERRORES POR IDIOMAS
asignaturas = [145302, 145303, 145306, 145308, 145301, 145200, 145304, 145305, 145307, 145309,
                145311, 145310, 145314, 145315, 145318, 145312, 145009, 145022, 145005, 145313, 145021, 145024, 145028,
                    145003, 145006, 145316, 145317, 
                145320, 145321,  145322, 145324, 145329, 145323, 145325, 145326, 145328, 145327, 
                145336, 145395, 145396, 145355, #145160, 
                    145397, 145359, 145337, 145333, 145338, 145356, 145347, #145296, 
                    145331, 145332, 145330
               
               
               ]

webScrappingDeusto.obtenerCompSinSeparar(asignaturas)


mapaCompAsignaturas = {}

with open (f"{os.path.dirname(os.path.abspath(__file__))}\\resultado.txt", "r") as f:
    lineas = f.readlines()
    f.close()

for linea in lineas:
    mapaCompEspecificas = {}
    mapaCompGenerales = {}
    compEspecificasLista = []
    listaCompEsp = []
    lineaSeparada = linea.split(";")

    for trozo in lineaSeparada:
        #if re.search(r"CE\d+", trozo) or re.search(r"C.E.\d+", trozo) or re.search(r"CE-\d+", trozo) or re.search(r"CE \d+", trozo) or re.search(r'CE\d\.', trozo):
        compEspecificasLista = re.split(r"(CE\d+)|(C.E.\d+.)|(CE-\d+)|(CE \d+)|(CE\d\.)", trozo)
        compEspecificasLista = [elem for elem in compEspecificasLista if elem]
        
    for parte in compEspecificasLista:
        index = compEspecificasLista.index(parte)
        compEspecificasLista[index] = parte.strip(". \n:-*")
    

    for comp in compEspecificasLista:
        if re.search(r"CE\d", comp) or re.search(r"C.E.\d+", comp) or re.search(r"CE-\d+", comp) or re.search(r"CE \d+", comp) or re.search(r'CE\d\.', comp):
            indexCE = compEspecificasLista.index(comp)
            listaCompEsp.append(compEspecificasLista[indexCE+1])
            compEspecificasLista.pop(indexCE)

    mapaCompEspecificas["CE"] = listaCompEsp
    mapaCompAsignaturas[lineaSeparada[0]] = mapaCompEspecificas

with open (f"{os.path.dirname(os.path.abspath(__file__))}\\compAsignaturas.csv", "w") as f:
    for key in mapaCompAsignaturas:
        compFormateadas = f"{key};"
        for compEsp in mapaCompAsignaturas[key]["CE"]:
            compFormateadas += f"{compEsp};"
        f.write(f"{compFormateadas}\n")
        compFormateadas = ""
    f.close()

os.remove(f"{os.path.dirname(os.path.abspath(__file__))}\\resultado.txt")