from number_parser import valider_saisie, separer_nombre
from core_converter import convertir_centaines
from large_number_handler import convertir_millions, convertir_decimaux
from output_formatter import assembler_nombre
def convertir_nombre_en_lettres(nombre):
    entier, decimal, signe=separer_nombre(nombre)
    texte_entier=convertir_millions(int(entier))
    texte_decimal=convertir_decimaux(decimal)
    return assembler_nombre(texte_entier, texte_decimal, signe)

if__name__=="__main__":
    nombre= input("entrez un nombre: ")
    if valider_saisie(nombre):
        print(convertir_nombre_en_lettres(nombre))
    else:
        print("Erreur:entree invalide")