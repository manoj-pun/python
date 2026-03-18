# Write a function bmi_category(weight_kg, height_m) that computes
# BMI (weight / height**2) and returns a category string: BMI < 18.5 →
# 'Underweight' 18.5 – 24.9 → 'Normal' 25.0 – 29.9 → 'Overweight' 30
# and above → 'Obese' Test: bmi_category(50, 1.70), bmi_category(70,
# 1.75), bmi_category(90, 1.70)

def bmi_category(weight_kg, height_m):
    """
    Calculate BMI and return the corresponding category.
    
    BMI formula: weight (kg) / height (m)²
    
    Categories:
    - Under 18.5       → 'Underweight'
    - 18.5 to 24.9     → 'Normal'
    - 25.0 to 29.9     → 'Overweight'
    - 30.0 and above   → 'Obese'
    """
    if height_m <= 0:
        return "Invalid height (must be positive)"
    
    bmi = weight_kg / (height_m ** 2)
    # Round to 1 decimal place (common medical practice)
    bmi = round(bmi, 1)
    
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25.0:          # 18.5 ≤ bmi < 25.0
        return "Normal"
    elif bmi < 30.0:          # 25.0 ≤ bmi < 30.0
        return "Overweight"
    else:                     # bmi ≥ 30.0
        return "Obese"


# Test cases
print(bmi_category(50, 1.70))   # → Underweight
print(bmi_category(70, 1.75))   # → Normal
print(bmi_category(90, 1.70))   # → Obese