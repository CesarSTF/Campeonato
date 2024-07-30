from abc import ABC, abstractmethod
from enum import Enum
from datetime import date


class Persona(ABC):
    def __init__(self, nombre, apellido, identificador, edad, sexo, celular):
        self.nombre = nombre
        self.apellido = apellido
        self.identificador = identificador
        self.edad = edad
        self.sexo = sexo
        self.celular = celular

    @abstractmethod
    def registrarse(self):
        pass

    @abstractmethod
    def inscribirse(self):
        pass


class Jugador(Persona):
    def __init__(self, nombre, apellido, identificador, edad, sexo, celular, equipo, estado):
        super().__init__(nombre, apellido, identificador, edad, sexo, celular)
        self.equipo = equipo
        self.estado = estado

    def registrarse(self):
        print(f'Jugador {self.nombre} registrado.')

    def inscribirse(self):
        print(f'Jugador {self.nombre} inscrito en el equipo {self.equipo}.')


class Administrador(Persona):
    def __init__(self, nombre, apellido, identificador, edad, sexo, celular):
        super().__init__(nombre, apellido, identificador, edad, sexo, celular)

    def registrarse(self):
        print(f'Administrador {self.nombre} registrado.')

    def inscribirse(self):
        print(f'Administrador {self.nombre} inscrito.')

    def eliminar_jugador(self, jugador, equipo):
        equipo.equipo_list.remove(jugador)
        print(f'Jugador {jugador.nombre} eliminado del equipo {equipo.nombre_equipo}.')

    def agregar_jugador(self, jugador, equipo):
        equipo.equipo_list.append(jugador)
        print(f'Jugador {jugador.nombre} agregado al equipo {equipo.nombre_equipo}.')

    def agregar_equipo(self, equipo, campeonato):
        campeonato.equipo_list.append(equipo)
        print(f'Equipo {equipo.nombre_equipo} agregado al campeonato.')

    def eliminar_equipo(self, equipo, campeonato):
        campeonato.equipo_list.remove(equipo)
        print(f'Equipo {equipo.nombre_equipo} eliminado del campeonato.')

    def definir_juego(self, calendario):
        print(f'Juego definido para el calendario {calendario.fecha}.')
        return calendario.fecha


class Arbitro:
    def __init__(self, deporte, partido_asignado):
        self.deporte = deporte
        self.partido_asignado = partido_asignado

    def asignar_partido(self, partido):
        self.partido_asignado = partido
        print(f'Arbitro asignado al partido {partido.fecha}.')


class Equipo:
    def __init__(self, nombre_equipo, id_equipo):
        self.nombre_equipo = nombre_equipo
        self.id_equipo = id_equipo
        self.equipo_list = []
        self.puntos = 0

    def __str__(self):
        return f'Equipo {self.nombre_equipo} con ID {self.id_equipo}'


class Campeonato:
    def __init__(self, nombre, fecha_inicio, fecha_fin):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.equipo_list = []

    def registrar_equipo(self, equipo):
        self.equipo_list.append(equipo)
        print(f'Equipo {equipo.nombre_equipo} registrado en el campeonato {self.nombre}.')

    def registrar_jugador(self, jugador, equipo):
        if equipo in self.equipo_list:
            equipo.equipo_list.append(jugador)
            print(f'Jugador {jugador.nombre} registrado en el equipo {equipo.nombre_equipo}.')
        else:
            print(f'Equipo {equipo.nombre_equipo} no registrado en el campeonato {self.nombre}.')

    def calcular_resultado(self):
        print(f'Calculando resultado del campeonato {self.nombre}...')
        return 0.0

    def calcular_posiciones(self):
        posiciones = sorted(self.equipo_list, key=lambda x: x.puntos, reverse=True)
        print(f'Tabla de posiciones del campeonato {self.nombre}:')
        for idx, equipo in enumerate(posiciones):
            print(f'{idx + 1}. {equipo.nombre_equipo} - {equipo.puntos} puntos')
        return posiciones


class Encuentro:
    def __init__(self, equipo1, equipo2, marcador1, marcador2):
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.marcador1 = marcador1
        self.marcador2 = marcador2

    def mostrar_marcador(self):
        return f'{self.equipo1.nombre_equipo} {self.marcador1} - {self.marcador2} {self.equipo2.nombre_equipo}'

    def registrar_resultado(self):
        if self.marcador1 > self.marcador2:
            self.equipo1.puntos += 3
        elif self.marcador1 < self.marcador2:
            self.equipo2.puntos += 3
        else:
            self.equipo1.puntos += 1
            self.equipo2.puntos += 1
        print(f'Resultado registrado: {self.mostrar_marcador()}')


class CalendarioJuego:
    def __init__(self, encuentro, fecha):
        self.encuentro = encuentro
        self.fecha = fecha

    def asignar_arbitro(self, arbitro):
        arbitro.asignar_partido(self)
        print(f'Arbitro asignado para el encuentro del {self.fecha}.')


class Estadistica:
    def __init__(self, punto_total, victoria, derrota, punto_favor, punto_contra, asistencia, tabla_posicion):
        self.punto_total = punto_total
        self.victoria = victoria
        self.derrota = derrota
        self.punto_favor = punto_favor
        self.punto_contra = punto_contra
        self.asistencia = asistencia
        self.tabla_posicion = tabla_posicion
        self.estadistica_list = []

    def calcular_estadistica(self):
        self.punto_total = self.punto_favor - self.punto_contra
        print(f'Estadística calculada: {self.punto_total} puntos totales.')

    def mostrar_estadistica(self):
        return f'Estadísticas: {self.punto_total} puntos, {self.victoria} victorias, {self.derrota} derrotas.'

    def calcular_posicion(self):
        self.tabla_posicion = sorted(self.estadistica_list, key=lambda x: x.punto_total, reverse=True)
        print('Posición calculada.')

    def mostrar_posicion(self):
        return f'Posición en la tabla: {self.tabla_posicion}'


class Juego(Enum):
    BASQUET = 1
    FUTBOL = 2
    PINGPONG = 3
    ATLETISMO = 4


class ModalidadJuego(Enum):
    INDIVIDUAL = 1
    EQUIPO = 2


class Fase(Enum):
    DEADSUBITA = 1
    FASEGRUPO = 2
    LIGA = 3
    ELIMINATORIA = 4
    GRUPO = 5


# Crear instancias de jugadores y equipos
jugador1 = Jugador("Juan", "Pérez", "123", 25, "M", "555-1234", "Equipo A", True)
jugador2 = Jugador("Pedro", "Gómez", "124", 24, "M", "555-5678", "Equipo A", True)
jugador3 = Jugador("Luis", "Martínez", "125", 26, "M", "555-9101", "Equipo B", True)
jugador4 = Jugador("Carlos", "López", "126", 27, "M", "555-1122", "Equipo B", True)

equipo1 = Equipo("Equipo A", "001")
equipo2 = Equipo("Equipo B", "002")

# Crear campeonatos
campeonato1 = Campeonato("Campeonato 1", date(2024, 1, 1), date(2024, 12, 31))
campeonato2 = Campeonato("Campeonato 2", date(2024, 6, 1), date(2024, 11, 30))

# Crear administrador
administrador1 = Administrador("Ana", "Gómez", "456", 30, "F", "555-5678")

# Agregar equipos a campeonatos
administrador1.agregar_equipo(equipo1, campeonato1)
administrador1.agregar_equipo(equipo1, campeonato2)  
administrador1.agregar_equipo(equipo2, campeonato1)
administrador1.agregar_equipo(equipo2, campeonato2)

# Agregar jugadores a equipos
administrador1.agregar_jugador(jugador1, equipo1)
administrador1.agregar_jugador(jugador2, equipo1)
administrador1.agregar_jugador(jugador3, equipo2)
administrador1.agregar_jugador(jugador4, equipo2)

# Crear encuentros
encuentro1 = Encuentro(equipo1, equipo2, 2, 2) 
encuentro2 = Encuentro(equipo1, equipo2, 1, 3) 

# Registrar resultados
encuentro1.registrar_resultado()
encuentro2.registrar_resultado()

# Calcular y mostrar posiciones
campeonato1.calcular_posiciones()
campeonato2.calcular_posiciones()
