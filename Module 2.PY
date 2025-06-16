UNITS = ["zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf"]
TENS = ["", "dix", "vingt", "trente", "quarante", "cinquante", "soixante", "soixante-dix", "quatre-vingt", "quatre-vingt-dix"]

def convert_units(number):
    """ Convertit les unités (0-9) """
    return UNITS[number]

def convert_tens(number):
    """ Convertit les dizaines (10-99) avec gestion des cas spéciaux """
    if number < 10:
        return convert_units(number)
    elif number < 20:
        return ["dix", "onze", "douze", "treize", "quatorze", "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf"][number - 10]
    elif number < 100:
        dizaine, unite = divmod(number, 10)
        if unite == 1 and dizaine in [7, 9]:  # Gestion des "soixante-et-onze", "quatre-vingt-et-un"
            return f"{TENS[dizaine]} et un"
        return f"{TENS[dizaine]}-{UNITS[unite]}" if unite else TENS[dizaine]