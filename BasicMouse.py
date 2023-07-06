class Mouse:
    def __init__(self, cor, altura, largura, profundidade, peso):
        self.cor = cor
        self.altura = altura
        self.largura = largura
        self.profundidade = profundidade
        self.peso = peso

    def Mouse_Func(self):
        if self.ClickL == 'ClickL':
            print('Click no Esquerdo')
        if self.ClickR == 'ClickR':
            print('Click no Direito')
        if self.ClickM == 'ClickM':
            print('Click no meio')
        else:
            print('Não clicar') 


mouse1 = Mouse("Preto", "5cm", "3cm", "2cm", "200g")
print(mouse1.cor)
print(mouse1.altura)
print(mouse1.largura)
print(mouse1.profundidade)
print(mouse1.peso)

mouse2 = Mouse("Azul", "9cm", "6cm", "5cm", "400g")
print(mouse2.cor)
print(mouse2.altura)
print(mouse2.largura)
print(mouse2.profundidade)
print(mouse2.peso)