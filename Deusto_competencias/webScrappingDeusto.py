import bs4
import requests
import unidecode
import re
import os

def obtenerCompSinSeparar(asignaturas):

    for codAsig in asignaturas:

        idiomaAct = "es.ES"
        anoAcad = 2023
        url = f"https://gaude.deusto.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&idiomaPais={idiomaAct}&_anoAcademico={anoAcad}&_codAsignatura={codAsig}"


        respuesta = requests.get(url)
        soup = bs4.BeautifulSoup(respuesta.text,'lxml')
        texto = soup.body.get_text(' ', strip=True)

        texto = unidecode.unidecode(texto)
        #textoSplit = re.split(r"COMPETENCIAS ESPECÍFICAS.*?:|Competencias específicas.*?:|Competencias Específicas.*?:|ESPECÍFICAS|competencias específicas.*?:|Competencias específicas", texto)
        textoSplit = re.split(r"Resultados de aprendizaje en tA\(c\)rminos de competencias|Resultados de aprendizaje en terminos de competencias", texto)

        textoSplitFinal = textoSplit[1].split("Contenidos")

        competencias = textoSplitFinal[0].strip()

        with open(f"{os.path.dirname(os.path.abspath(__file__))}\\resultado.txt", "a") as f:
            f.write(f"{codAsig};{unidecode.unidecode(competencias)}\n")
            f.close()


    print("finalizado")
