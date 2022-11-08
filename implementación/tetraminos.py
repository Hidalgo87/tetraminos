from abc import ABC, abstractmethod


class Tetramino(ABC):
    def __init__(self, tipo, estado_rotacion=0):
        self.tipo: str = tipo
        self.estado_rotacion: int = estado_rotacion

    @abstractmethod
    def rotar(self):
        if self.estado_rotacion >= 4:
            self.estado_rotacion = 0
        else:
            self.estado_rotacion += 1

    @abstractmethod
    def representar(self):
        pass


class TetraI(Tetramino):
    def __init__(self):
        super().__init__("O")

    def rotar(self):
        if self.estado_rotacion >= 4:
            self.estado_rotacion = 0
        else:
            self.estado_rotacion += 1

    def representar(self):
        pass


class TetraZ(Tetramino):
    def __init__(self):
        super().__init__("O")

    def rotar(self):
        if self.estado_rotacion >= 4:
            self.estado_rotacion = 0
        else:
            self.estado_rotacion += 1

    def representar(self):
        pass


class TetraT(Tetramino):
    def __init__(self):
        super().__init__("O")

    def rotar(self):
        if self.estado_rotacion >= 4:
            self.estado_rotacion = 0
        else:
            self.estado_rotacion += 1

    def representar(self):
        pass


class TetraJ(Tetramino):
    def __init__(self):
        super().__init__("O")

    def rotar(self):
        if self.estado_rotacion >= 4:
            self.estado_rotacion = 0
        else:
            self.estado_rotacion += 1

    def representar(self):
        pass


class TetraL(Tetramino):
    def __init__(self):
        super().__init__("O")

    def rotar(self):
        if self.estado_rotacion >= 4:
            self.estado_rotacion = 0
        else:
            self.estado_rotacion += 1

    def representar(self):
        pass


class TetraS(Tetramino):
    def __init__(self):
        super().__init__("O")

    def rotar(self):
        if self.estado_rotacion >= 4:
            self.estado_rotacion = 0
        else:
            self.estado_rotacion += 1

    def representar(self):
        pass


class TetraO(Tetramino):
    def __init__(self):
        super().__init__("O")

    def rotar(self):
        if self.estado_rotacion >= 4:
            self.estado_rotacion = 0
        else:
            self.estado_rotacion += 1

    def representar(self):
        pass


class Juego:
    def __init__(self, tipo1: str, tipo2: str):
        self.juego: list[Tetramino] = []
        self.trm1 = self.elegir_letra(tipo1)
        self.trm2 = self.elegir_letra(tipo2)

    def elegir_letra(self, tipo):
        if tipo == "O":
            return TetraO()
        elif tipo == "I":
            return TetraI()
        elif tipo == "Z":
            return TetraZ()
        elif tipo == "T":
            return TetraT()
        elif tipo == "J":
            return TetraJ()
        elif tipo == "L":
            return TetraL()
        elif tipo == "S":
            return TetraS()

    def buscar_tetramino(self, numero: int):
        if numero == 1:
            return self.trm1
        elif numero == 2:
            return self.trm2


class Representacion(ABC):
    def __init__(self, tipo: str, estado: int):
        pass

    def representar(self):
        pass


class Consola(Representacion):
    def __init__(self, tipo: str, estado: int):
        super().__init__(tipo, estado)
        self.juego = None
        opcion = self.mostrar()
        self.proceder(opcion)

    def proceder(self, opcion):
        if opcion == 1:
            tipo1 = input("Ingrese la letra que desea para el primer Tetramino")
            tipo2 = input("Ingrese la letra que desea para el segundo Tetramino")
            self.juego = Juego(tipo1, tipo2)

        elif opcion == 2:
            numero_elegido = int(input("Elija cual de los dos tetraminos desea rotar. El primero o el segundo."))
            trm = self.juego.buscar_tetramino(numero_elegido)
            trm.rotar()

    def mostrar(self):
        while True:
            print("""
            Elige una opción:
            1. Escoger figuras
            2. Rotar figuras
            """)
            opcion = int(input(""))
            return opcion


class Archivo(Representacion):
    pass


Representacion()
