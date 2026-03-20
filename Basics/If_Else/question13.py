# A cinema offers the following ticket pricing: Base price: 200 - Age < 5
# → FREE (return 0) - Age 5–12 → 50% discount - Age 60 and above →
# 40% discount - Students (is_student=True) aged 13–25 → 30%
# discount - Tuesday (day='Tuesday') → additional 20 off the final price
# for everyone - Members (is_member=True) get an extra 10% off the
# final price Discounts are applied in order: age discount first, then
# Tuesday, then membership. Write ticket_price(age, is_student, day,
# is_member).

def ticket_price(age, is_student, day, is_member):
    basePrice = 200
    
    if age < 5:
        return 0  
    
    elif 5 <= age <= 12:
        price = basePrice * 0.5  # 50% discount
    
    elif age >= 60:
        price = basePrice * 0.6  # 40% discount (pay 60% of base)
    
    elif is_student and 13 <= age <= 25:
        price = basePrice * 0.7  # 30% discount (pay 70% of base)
    
    else:  # Regular adult (26-59, not student special)
        price = basePrice
    
    # Step 2: Tuesday discount (additional 20 off the final price)
    if day == 'Tuesday':
        price = price - 20
    
    # Step 3: Member discount (extra 10% off the final price)
    if is_member:
        price = price * 0.9
    
    return max(0, price)  # Ensure price doesn't go below 0

# Test cases
print(ticket_price(3, False, 'Monday', False))    # 0 (free)
print(ticket_price(8, False, 'Monday', False))    # 100 (200 * 0.5)
print(ticket_price(20, True, 'Monday', False))    # 140 (200 * 0.7)
print(ticket_price(20, True, 'Tuesday', False))   # 120 (140 - 20)
print(ticket_price(20, True, 'Tuesday', True))    # 108 (120 * 0.9)
print(ticket_price(65, False, 'Monday', False))   # 120 (200 * 0.6)
print(ticket_price(30, False, 'Monday', False))   # 200 (regular)