import math
import turtle
MEDIO_ANGULO = 180

#Clase abstracta que representa figuras geométricas:
class Figura:

    def area(self):
        pass

    def perimetro(self):
        pass

    def dibujo(self):
        pass


# Clase para la forma círculo:
class Circulo(Figura):

    def __init__(self,r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

    def perimetro(self):
        return 2 * math.pi * self.r

    def dibujo(self):
        turtle.TurtleScreen._RUNNING = True
        t = turtle.Turtle()
        t.circle(self.r)
        turtle.exitonclick()


# Clase para la forma Triángulo:
class Triangulo(Figura):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c)) 

    def perimetro(self):
        return self.a + self.b + self.c

    def dibujar(self):
        area = self.area()
        R = (self.a * self.b * self.c) / (4 * area)
        alfa = math.degrees(math.asin(self.c / (2 * R)))
        beta = math.degrees(math.asin(self.a / (2 * R)))
        gamma = MEDIO_ANGULO - alfa - beta
        turtle.TurtleScreen._RUNNING = True
        t = turtle.Turtle()
        t.forward(self.a)
        t.right(gamma - MEDIO_ANGULO)
        t.forward(self.c)
        t.right(beta - MEDIO_ANGULO)
        t.forward(self.b)
        turtle.exitonclick()


# Clase para la forma Triángulo equilátero que hereda de Triángulo:
class TrianguloEquilatero(Triangulo):

    def __init__(self, a):
        super().__init__(a, a, a)


# Clase para la forma rectángulo:
class Rectangulo(Figura):

    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def area(self):
        return self.a * self.b

    def perimetro(self):
        return 2 * self.a + 2 * self.b

    def dibujar(self):
        ANGULO = 90
        turtle.TurtleScreen._RUNNING = True
        t = turtle.Turtle()
        t.forward(self.a)
        t.right(- ANGULO)
        t.forward(self.b)
        t.right(- ANGULO)
        t.forward(self.a)
        t.right(- ANGULO)
        t.forward(self.b)
        turtle.exitonclick()


#Clase cuadrado que hereda de rectángulo:
class Cuadrado(Rectangulo):

    def __init__(self, a):
        super().__init__(a, a)

# Clase Pruebafiguras

class Pruebasfiguras:
	def __init__(self):
		self.formas=[]

	def menu(self):
		print()
		menu=[
			['Escoja la Figura:'],
			['1. Circulo'],
			['2. Triángulo'],
			['3. Triángulo Equilatero'],            
			['4. Rectángulo'],
			['5. Cuadrado'],
			['6. Cerrar']
		]
 
		for x in range(6):
			print(menu[x][0])
 
		opcion=int(input("Introduzca la opción deseada: "))
		if opcion==1:
			self.circu()
		elif opcion==2:
			self.trian()
		elif opcion==3:
			self.tequi()
		elif opcion==4:
			self.rect()
		elif opcion==5:
			self.cuadr()            
		elif opcion==6:
			print("Saliendo...")
			exit() 
		# volvemos a llamar al menú
		self.menu()

    # def círculo
	def circu(self):

		cx=Circulo(int(input("escriba el radio del círculo aquí: ")))
		print("Área y perimetro del círculo:", (cx.area(), (cx.perimetro())))

	# def triángulo
	def trian(self):
		tx=Triangulo(int(input("lado a ")),int(input("lado b: ")),int(input("lado c: ")))
		print("Área y perimetro del Triángulo:", (tx.area(), (tx.perimetro())))

	# def triángulo equilátero
	def tequi(self):
		te=TrianguloEquilatero(int(input("lado a ")))
		print("Área y perimetro del Triángulo Equilátero:", (te.area(), (te.perimetro())))		
 
	# def rectángulo
	def rect(self):
		rx=Rectangulo(int(input("lado a ")),int(input("lado b: ")))
		print("Área y perimetro del Rectángulo:", (rx.area(), (rx.perimetro())))	

	# def cuadrado
	def cuadr(self):
		cx=Cuadrado(int(input("lado a ")))
		print("Área y perimetro del cuadrado:", (cx.area(), (cx.perimetro())))



pruebas = Pruebasfiguras()
pruebas.menu()
pruebas.circu()
pruebas.trian()
pruebas.tequi()
pruebas.cuadr()
pruebas.rect()
