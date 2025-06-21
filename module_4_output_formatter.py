from module_3_large_number_handler import convert_thousands_and_up, convert_decimal

def format_output(data):
    entier_str = convert_thousands_and_up(abs(data["entier"]))
    decimal_str = f" virgule {convert_decimal(data['decimal'])}" if data["decimal"] else ""
    prefix = "moins " if data["negatif"] else ""
    return f"{prefix}{entier_str}{decimal_str}"
