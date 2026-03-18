# Python allows chained comparisons like 10 < x < 20. Write a function
# classify_temperature(temp) that returns: 'Freezing' if temp < 0 'Cold' if
# 0 <= temp < 10 'Cool' if 10 <= temp < 20 'Warm' if 20 <= temp < 30 'Hot'
# if 30 <= temp < 40 'Extreme' if temp >= 40 Use chained comparisons
# wherever possible.


def classify_temperature(temp):
    if temp < 0:
        return 'Freezing'
    elif 0 <= temp < 10:
        return 'Cold'
    elif 10 <= temp < 20:
        return 'Cool'
    elif 20 <= temp < 30:
        return 'Warm'
    elif 30 <= temp < 40:
        return 'Hot'
    else:  
        return 'Extreme'

# Test the function
print(classify_temperature(-5))    
print(classify_temperature(5))     
print(classify_temperature(15))    
print(classify_temperature(25))    
print(classify_temperature(35))    
print(classify_temperature(45))    