UNITS = ["zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf"]
TENS = ["", "dix", "vingt", "trente", "quarante", "cinquante", "soixante",
        "soixante-dix", "quatre-vingt", "quatre-vingt-dix"]
SPECIALS = {11: "onze", 12: "douze", 13: "treize", 14: "quatorze", 15: "quinze", 16: "seize"}

def convert_units(n):
    return UNITS[n]

def convert_tens(n):
    if n in SPECIALS:
        return SPECIALS[n]
    elif n < 10:
        return convert_units(n)
    elif n < 20:
        return f"dix-{convert_units(n - 10)}"
    else:
        dizaine, unite = divmod(n, 10)
        if unite == 1 and dizaine in [7, 9]:
            return f"{TENS[dizaine]} et un"
        return f"{TENS[dizaine]}-{convert_units(unite)}" if unite else TENS[dizaine]

def convert_hundreds(n):
    centaine, reste = divmod(n, 100)
    if centaine == 0:
        return convert_tens(reste)
    base = "cent" if centaine == 1 else f"{UNITS[centaine]} cent"
    if reste == 0:
        if centaine > 1:
            base += "s"
        return base
    return f"{base} {convert_tens(reste)}"
