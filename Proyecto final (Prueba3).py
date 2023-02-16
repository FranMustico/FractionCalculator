Ing = str(input("Deseas comenzar S/N: "))
while Ing == "S" or Ing == "s" or Ing=="si" or Ing=="Si" or Ing=="sI" or Ing=="sí" or Ing=="Sí":
    
    class Fraccion():
        def __init__(self, arriba, abajo):
            self.numerador = int(arriba)
            if abajo == 0:
                raise Exception("El denominador no puede ser 0")
            self.denominador = int(abajo)

        def __str__(self):
            return str(self.numerador) + "/" + str(self.denominador)

        def __eq__(self, otro):
            primerNum = self.numerador * otro.denominador
            segundoNum = otro.numerador * self.denominador
            return primerNum == segundoNum
    
        def MCD(self, a, b):
            temporal = 0
            while b != 0:
                temporal = b
                b = a % b
                a = temporal
            return a

        def MCM(self, a, b):
            return (a * b) / self.MCD(a, b)
    
        def __add__(self, otra):
            mcm = self.MCM(self.denominador, otra.denominador)
            diferencia_self = mcm/self.denominador
            diferencia_otra = mcm/otra.denominador
            numerador_resultado = (diferencia_self*self.numerador) + \
                (diferencia_otra*otra.numerador)
            return Fraccion(numerador_resultado, mcm)

        def __sub__(self, otra):
            mcm = self.MCM(self.denominador, otra.denominador)
            diferencia_self = mcm/self.denominador
            diferencia_otra = mcm/otra.denominador
            numerador_resultado = (diferencia_self*self.numerador) - \
                (diferencia_otra*otra.numerador)
            return Fraccion(numerador_resultado, mcm)
        
        def __gt__(self, otra):
            valor_division1=self.denominador/self.numerador
            valor_division2=otra.denominador/otra.numerador
            valor_mayor_que=valor_division1-valor_division2
            if valor_mayor_que>0:
                return False
            elif valor_mayor_que==0:
                return 1
            else:
                return True
        def __it__(self, otra):
            valor_division1=self.denominador/self.numerador
            valor_division2=otra.denominador/otra.numerador
            valor_mayor_que=valor_division1-valor_division2
            if valor_mayor_que>0:
                return True
            elif valor_mayor_que==0:
                return 1
            else:
                return False
        

        def __mul__(self, otra):
            return Fraccion(self.numerador*otra.numerador, self.denominador*otra.denominador)

        def __div__(self, otra):
            return Fraccion(self.numerador*otra.denominador, self.denominador*otra.numerador)

    try:
        Numer = int(input("Ingresa el numerador de la primera fracción "))
        Denom = int(input("Ingresa el denominador de la primera fracción "))
        
        Numer2 = int(input("Ingresa el numerador de la seguunda fracción "))
        Denom2 = int(input("Ingresa el denominador de la segunda fracción "))
        
        Fraccion1= Fraccion(Numer, Denom)
        Fraccion2 = Fraccion(Numer2, Denom2)
        try:
            operacion=input("¿Que operacion desea realizar?(*,/,-,+,>,<,)")
            if operacion=="multiplicación" or operacion=="multiplicacion" or operacion=="Multiplicacion" or operacion=="Multiplicación" or operacion=="*":
                Multiplicacion=Fraccion1.__mul__(Fraccion2)
                print("La multipliacion de sus fracciones es",Multiplicacion)
                Ing = str(input("¿Deseas hacer otra operacion? "))
                
            elif operacion=="división" or operacion=="division" or operacion=="Division" or operacion=="División" or operacion=="/":
                Division=Fraccion1.__div__(Fraccion2)
                print("La division de sus fracciones es", Division)
                Ing = str(input("¿Deseas hacer otra operacion? "))
                
            elif operacion=="resta" or operacion=="Resta" or operacion=="-":
                Resta=Fraccion1.__sub__(Fraccion2)
                print("La resta de sus fracciones es", Resta)
                Ing = str(input("¿Deseas hacer otra operacion? "))
                
            elif operacion=="Suma" or operacion=="suma" or operacion=="+":
                Suma=Fraccion1.__add__(Fraccion2)
                print("La suma de sus fracciones es", Suma)
                
                Ing = str(input("¿Deseas hacer otra operacion? "))
            elif operacion=="Mayor" or operacion=="mayor" or operacion=="Mayor que" or operacion=="Mayorque" or operacion=="mayor que" or operacion=="mayorque" or operacion==">":
                Mayor_que=Fraccion1.__gt__(Fraccion2)
                if Mayor_que==True:
                    print("La primera fraccion es mayor que que la segunda")
                    Ing = str(input("¿Deseas hacer otra operacion? "))
                elif Mayor_que==False:
                    print("La primera fraccion es menor que que la segunda")
                    Ing = str(input("¿Deseas hacer otra operacion? "))
                elif Mayor_que==1:
                    print("Las dos fracciones son iguales.")
                    Ing = str(input("¿Deseas hacer otra operacion? "))
                
            elif operacion=="menor" or operacion=="Menor" or operacion=="Menor que" or operacion=="Menorque" or operacion=="menor que" or operacion=="menorque" or operacion=="<":
                Menor_que=Fraccion1.__it__(Fraccion2)
                if Menor_que==True:
                    print("La primera fraccion es menor que que la segunda")
                    Ing = str(input("¿Deseas hacer otra operacion? "))
                elif Menor_que==False:
                    print("La primera fraccion es mayor que que la segunda")
                    Ing = str(input("¿Deseas hacer otra operacion? "))
                elif Menor_que==1:
                    print("Las dos fracciones son iguales.")
                    Ing = str(input("¿Deseas hacer otra operacion? "))
            else:
                print()
        except ValueError:
            print("Por favor ingresa un valor numerico entero")
        
    except ValueError:
        print("Por favor ingresa un valor numerico entero")
    
else:
    print("Hasta luego")