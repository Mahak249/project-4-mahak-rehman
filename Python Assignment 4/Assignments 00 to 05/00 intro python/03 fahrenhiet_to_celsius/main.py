def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0 / 9.0

print("Welcome to the Fahrenheit to Celsius Converter!")
f = float(input("Enter temperature in Fahrenheit: "))
c = fahrenheit_to_celsius(f)
print(f"Temperature: {f}F = {c}C")