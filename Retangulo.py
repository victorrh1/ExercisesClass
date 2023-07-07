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
    
    def AreaTotal(self):
        area_total = self.calcular_area()
        return area_total
    
    def PerimetroTotal(self):
        perimetro_total = self.calcular_perimetro()
        return perimetro_total
    
largura = float(input('Digite a Largura: '))
altura = float(input('Digite a Altura: '))
        

retangulo = Retangulo(largura, altura)
print('A Area total do retângulo: ', retangulo.AreaTotal())
print('O Perímetro total do retângulo: ', retangulo.PerimetroTotal()) 
        
        
        


