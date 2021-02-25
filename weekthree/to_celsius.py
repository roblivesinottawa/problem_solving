def toCelsius(x):
    """this function calculates the temperature from fahrenheit to celsius (0-100)"""
    return (x - 32) * 5 / 9

for x in range(0, 101, 10):
    print(f"From Fahrenheit = {x} to Celsius = {toCelsius(x)}")