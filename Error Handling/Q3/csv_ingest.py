def parse_amount(raw):
    try:
        return float(raw)
    except ValueError:
        return None
    
def column_total(value):
    try:
    
        return sum(value)
    except TypeError:
        return print(f"Column has a non-numeric value")
    

print(parse_amount("1999.50"))
print(parse_amount("N/A"))
print(column_total([100,250,75]))
print(column_total([100,"250",75]))