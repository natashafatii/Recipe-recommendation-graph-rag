def convert_units(amount, from_unit, to_unit):
    conversions = {
        ('cups', 'ml'): 240,
        ('tbsp', 'ml'): 15,
        ('tsp', 'ml'): 5
    }
    return amount * conversions.get((from_unit, to_unit), 1)

def check_allergies(ingredients, allergies):
    return any(allergy in str(ingredients).lower() for allergy in allergies)