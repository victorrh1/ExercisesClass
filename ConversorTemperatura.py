'''
Criar uma classe 'Conversor Temperatura', que tenha os metodos
'celsius para fahrenheit' e 'fahrenheit para celsius'. Esses metodos
devem converter temperaturas entre Celsius e Fahrenheit.
'''
class ConversorTemperatura:
    def celsius_para_fahrenheit(self, celsius):
        fahrenheit = (celsius * 9/5 + 32)
        return fahrenheit

    def fahrenheit_para_celsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return celsius
    
conversortemperatura = ConversorTemperatura()

celsius = 90
fahrenheit = conversortemperatura.celsius_para_fahrenheit(celsius)
print('Valor em Fahrenheit', fahrenheit)

fahrenheit = 95
celsius = conversortemperatura.fahrenheit_para_celsius(fahrenheit)
print('Valor em Celsius', celsius)