from module_1_number_parser import valider_nombre
from module_4_output_formatter import format_output

def main():
    print("🔢 Convertisseur de nombres en lettres 🇫🇷")
    print("Entrez un nombre (ou 'exit' pour quitter)")

    while True:
        saisie = input(">>> ")
        if saisie.lower() in ("exit", "quit"):
            print("👋 À bientôt !")
            break
        try:
            data = valider_nombre(saisie)
            print("📝 Résultat :", format_output(data))
        except ValueError as e:
            print("❌", e)

if __name__ == "__main__":
    main()
from module_1_number_parser import valider_nombre
from module_4_output_formatter import format_output

def main():
    print("🔢 Convertisseur de nombres en lettres 🇫🇷")
    print("Entrez un nombre (ou 'exit' pour quitter)")

    while True:
        saisie = input(">>> ")
        if saisie.lower() in ("exit", "quit"):
            print("👋 À bientôt !")
            break
        try:
            data = valider_nombre(saisie)
            print("📝 Résultat :", format_output(data))
        except ValueError as e:
            print("❌", e)

if __name__ == "__main__":
    main()
