def celsiusToKelvin(celsius):
    answer = celsius + 273.15
    return answer

# Koden kan också skrivas utan variabeln answer se nedan:

def celsiusToKelvin(celsius):
    return celsius + 273.15

# Nedan följer ett anrop av funktionen.

temp = float(input("Ange temperatur i grader Celsius: "))
print("Temperaturen är", celsiusToKelvin(temp), "Kelvin")

# Utskriften blir som följer.

#Ange temperatur i grader Celsius: 10
#Temperaturen är 283.15 Kelvin
