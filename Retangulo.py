'''
 Criar uma classe 'Retangulo' que tenha os atributos
'lagura' e 'altura'. Implementando métodos para calcular a
área e o perímetro do 'Retângulo'.
'''

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        area = self.largura * self.altura
        return area
    
    def calcular_perimetro(self):
        perimetro = 2 * (self.largura + self.altura)
        return perimetro
    
largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
        

retangulo = Retangulo(largura, altura)
print('A largura do retangulo é: ', retangulo.largura)
print('A altura do retangulo é: ', retangulo.altura)    
        
        
        


