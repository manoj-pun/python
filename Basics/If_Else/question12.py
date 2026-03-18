# Write a function shipping_cost(weight, destination, is_express) with
# these rules: Domestic: weight <= 1 kg → base 5.00 1 < weight <= 5 →
# base 10.00 weight > 5 → base 20.00 International: multiply domestic
# base by 3 Express surcharge: add 50% to the final cost if is_express
# is True Test: (0.5,'domestic',False), (3,'international',True),
# (7,'domestic',True)

def shipping_cost(weight, destination, is_express):
    # Determine base cost
    if destination.lower() == "domestic":
        if weight <= 1:
            base = 5.00
        elif weight <= 5:
            base = 10.00
        else:
            base = 20.00
    elif destination.lower() == "international":
        # First calculate domestic base, then multiply by 3
        if weight <= 1:
            base = 5.00
        elif weight <= 5:
            base = 10.00
        else:
            base = 20.00
        base *= 3
    else:
        raise ValueError("Destination must be 'domestic' or 'international'")
    
    # Apply express surcharge (50% extra) if applicable
    if is_express:
        final_cost = base * 1.5
    else:
        final_cost = base
    
    return round(final_cost, 2)  # Return with 2 decimal places


# Test cases
test_cases = [
    (0.5, 'domestic', False),
    (3, 'international', True),
    (7, 'domestic', True)
]

for weight, dest, express in test_cases:
    cost = shipping_cost(weight, dest, express)
    print(f"Weight: {weight}kg, {dest}, express={express} → ${cost:.2f}")
