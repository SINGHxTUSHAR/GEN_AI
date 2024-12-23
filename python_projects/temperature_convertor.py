## func to convert the temp from one unit to another
def convert(temp,unit):
    if unit.lower() == 'c':
        return (temp * 9/5) + 32 , "F"
    elif unit.lower() == 'f':
        return (temp - 32) * 5/9 , "C"
    else:
        return "Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit."
    
temp = int(input("Enter the temperature: "))
unit = input("Enter the unit (C or F): ")
result = convert(temp, unit)
print(f"{temp}°{unit.upper()} is equal to {result[0]:.2f}°{result[1]}")