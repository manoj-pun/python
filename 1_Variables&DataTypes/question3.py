# Write a temperature converter. Store 100 as a Celsius value. Convert it to Fahrenheit using (C 9/5) + 32 and to Kelvin using C + 273.15. Print all three values rounded to 2 decimal places
# using round() and also using an f-string format like {value:.2f}.

# Store Celsius value
celsius = 100

# Convert temperatures
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

# ----- Using round() -----
print("Using round():")
print("Celsius:", round(celsius, 2))
print("Fahrenheit:", round(fahrenheit, 2))
print("Kelvin:", round(kelvin, 2))

# ----- Using f-string formatting -----
print("\nUsing f-string formatting:")
print(f"Celsius: {celsius:.2f}")
print(f"Fahrenheit: {fahrenheit:.2f}")
print(f"Kelvin: {kelvin:.2f}")