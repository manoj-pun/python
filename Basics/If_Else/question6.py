# Write a function income_tax(income) that calculates tax using these
# brackets: 0 – 10,000 → 0% tax 10,001 – 40,000 → 10% on amount
# above 10,000 40,001 – 80,000 → 3,000 + 20% on amount above 40,000
# Above 80,000 → 11,000 + 30% on amount above 80,000 Test:
# income_tax(8000), income_tax(25000), income_tax(60000),
# income_tax(100000)

def income_tax(income):
    if 0 <= income <= 10000:
        return 0
    elif 10001 <= income <= 40000:
        tax = (10/100) * (income - 10000)
        return tax
    elif 40001 <= income <= 80000:
        tax = 3000 + ((20/100) * (income - 40000))
        return tax
    else:
        tax = 11000 + ((30/100) * (income - 80000))
        return tax
    
print(income_tax(8000))    
print(income_tax(25000))   
print(income_tax(60000))  
print(income_tax(100000))  