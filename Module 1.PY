import re
from decimal import decimal

def nettoyer_saisie(nombre_str):
    ""supprime les espaces inutiles et verifie si l'entree est valide.
    nombre_str=nombre_str.strip().replace("";"")
    if not re.match(r"^-?\d+(\.\d+)?$",nombre_str):
        raise valueError("entree invalade: veuillez saisir un nombre valide.")
    return nombre_str
def decomposer_nombre(nombre_str):
    """ separe la partie entiere et la partie decimal."""
    if "." in nombre_str:
        partie_entiere, partie_decimale=nombre_str.split(".")
    else:
        partie_entiere, partie_decimale=nombre_str,""
    return int(partie_entiere), partie_decimale

 def valider_nombre(nombre_str):
        """verifie si le nombre est bien forme et prepare la conversion."""
        nombre_str=nettoyer_saisie(nombre_str)
        partie_entiere, partie_decimale=decomposer_nombre(nombre-str)

        return{
            "original": nombre_str,
            "entier": partie_entiere,
            "decimal":[int(chiffre)for chiffre in partie_decimale] if partie_decimale else[],
            "negatif": nombre_str.startswith("-")
        }

try:
            resultat=valide_nombre("  -1203.45")
            print(resultat)
except vaueError as e:
        print(e)