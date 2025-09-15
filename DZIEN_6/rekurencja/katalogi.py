import os

def pokaz_katalog(path:str, poziom:int=0):
    #Rekurencyjnie wypisuje katalogi i pliki
    try:
        for element in os.listdir(path):
            pelna_sciezka = os.path.join(path, element)
            print(" "*poziom+f"{element}")
            if os.path.isdir(pelna_sciezka):
                pokaz_katalog(pelna_sciezka, poziom+1)
    except PermissionError:
        pass

pokaz_katalog(".")
