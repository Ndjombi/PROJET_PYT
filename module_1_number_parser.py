import re

def nettoyer_saisie(nombre_str):
    nombre_str = nombre_str.strip().replace(";", "").replace(",", ".")
    if not re.match(r"^-?\d+(\.\d+)?$", nombre_str):
        raise ValueError("Entrée invalide : veuillez saisir un nombre valide.")
    return nombre_str

def decomposer_nombre(nombre_str):
    if "." in nombre_str:
        partie_entiere, partie_decimale = nombre_str.split(".")
    else:
        partie_entiere, partie_decimale = nombre_str, ""
    return int(partie_entiere), partie_decimale

def valider_nombre(nombre_str):
    nombre_str = nettoyer_saisie(nombre_str)
    partie_entiere, partie_decimale = decomposer_nombre(nombre_str)
    return {
        "original": nombre_str,
        "entier": partie_entiere,
        "decimal": [int(ch) for ch in partie_decimale] if partie_decimale else [],
        "negatif": nombre_str.startswith("-")
    }
