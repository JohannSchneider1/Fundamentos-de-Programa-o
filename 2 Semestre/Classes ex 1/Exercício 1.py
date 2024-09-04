class Retangulo:
    
    def __init__ (self,base,altura):
        self.base = base
        self.altura = altura
    
    def calcula_area(self)->float:
        return self.base*self.altura
        

def main():
    base = float(input('Digite um valor para base: '))
    altura = float(input('Digite um valor para a altura: '))

    retangulo1 = Retangulo(base,altura)
    area = retangulo1.calcula_area()
    print(area)

if __name__ == '__main__':
    main()

