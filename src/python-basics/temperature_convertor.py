# This program converts a temperature from Fahrenheit to Celsius.
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


print("Enter the temperature to convert")
temp_f = float(input())
temp_c = fahrenheit_to_celsius(temp_f)
print(f"{temp_f}°F is {temp_c:.2f}°C")