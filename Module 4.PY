import json

history = []

def format_output(sign, integer_par, decimal_part):
    """Assemble la conversion complète."""
    words = f"{sign} {convert_large_number(integer_part)}"
    if decimal_part:
      words +=  virguleconvert_decimal(decimal_part)

    history.append(words)
    return words

def save_history(filename="conversion_history.json"):
    """sauvegarde l'historique des conversions."""
    with open(filename, "w", encoding="utf-8") as file:
         json.dump(history,file,ensure_ascii=False, indent=4)

#Test        
print(format_output("moins", 123456, "89"))# "moins un million deux-cent-trente-quatre-mille cinq-cent-sioxante-sept virgule huit neuf"
save_history()
