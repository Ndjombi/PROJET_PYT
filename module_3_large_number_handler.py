from module_2_core_converter import convert_hundreds, convert_units

def convert_thousands_and_up(n):
    if n < 1000:
        return convert_hundreds(n)
    milliers, reste = divmod(n, 1000)
    if milliers == 1:
        prefix = "mille"
    else:
        prefix = f"{convert_hundreds(milliers)} mille"
    if reste == 0:
        return prefix
    return f"{prefix} {convert_hundreds(reste)}"

def convert_decimal(decimal_list):
    return " ".join(convert_units(d) for d in decimal_list)
