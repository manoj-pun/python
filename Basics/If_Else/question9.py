# Write a function process_order(item, quantity, in_stock, is_member)
# that: - If item is not in_stock → return 'Out of stock' - Else if quantity
# <= 0 → return 'Invalid quantity' - Else compute price = quantity * 100 -
# If is_member → apply 15% discount - Else if quantity >= 10 → apply
# 10% bulk discount - Else → no discount - Return the final price as a
# float


def process_order(item, quantity, in_stock, is_member):
    if not in_stock:
        return 'Out of stock'
    
    # Check quantity validity
    if quantity <= 0:
        return 'Invalid quantity'
    
    # Calculate base price
    price = quantity * 100
    
    # Apply discounts
    if is_member:
        # 15% member discount
        price = price * 0.85  
    elif quantity >= 10:
        # 10% bulk discount for non-members
        price = price * 0.90 
    
    return float(price)

# Test cases
print(process_order("item1", 5, True, False))   
print(process_order("item1", 10, True, False))  
print(process_order("item1", 5, True, True))    
print(process_order("item1", 10, True, True))  
print(process_order("item1", 0, True, False))   
print(process_order("item1", 5, False, False))  
