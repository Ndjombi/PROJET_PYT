
NOMBRES = {
    0: "zéro", 1: "un", 2: "deux", 3: "trois", 4: "quatre", 5: "cinq",
    6: "six", 7: "sept", 8: "huit", 9: "neuf", 10: "dix", 11: "onze",
    12: "douze", 13: "treize", 14: "quatorze", 15: "quinze", 16: "seize",
    20: "vingt", 30: "trente", 40: "quarante", 50: "cinquante",
    60: "soixante", 70: "soixante-dix", 80: "quatre-vingt", 90: "quatre-vingt-dix"
}

MULTIPLES = {1000: "mille", 1000000: "million", 1000000000: "milliard"}

    def __init__(self, nombre):
        self.nombre = nombre

    def convertir(self):
        if "." in str(self.nombre):
            partie_entiere, partie_decimale = str(self.nombre).split(".")
            return f"{self._convertir_entier(int(partie_entiere))} virgule {self._convertir_decimale(partie_decimale)}"
        return self._convertir_entier(int(self.nombre))

    def _convertir_entier(self, n):
        """Convertit un nombre entier en lettres."""
        if n < 0:
            return "moins " + self._convertir_entier(-n)
        if n in self.NOMBRES:
            return self.NOMBRES[n]
        if n < 100:
            dizaine, unité = divmod(n, 10)
            texte = self.NOMBRES[dizaine * 10]
            if unité:
                texte += "-" + self.NOMBRES[unité]
            return texte
        if n < 1000:
            centaine, reste = divmod(n, 100)
            texte = "cent" if centaine == 1 else self.NOMBRES[centaine] + " cent"
            if reste:
                texte += " " + self._convertir_entier(reste)
            return texte
        for valeur, mot in self.MULTIPLES.items():
            if n < valeur * 1000:
                nb, reste = divmod(n, valeur)
                texte = self._convertir_entier(nb) + " " + mot
                if reste:
                    texte += " " + self._convertir_entier(reste)
                return texte

    def _convertir_decimale(self, decimal):
        """Convertit la partie décimale comme un nombre entier."""
        return self._convertir_entier(int(decimal))

