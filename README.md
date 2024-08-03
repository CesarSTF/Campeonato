# Campeonato
![image](https://github.com/user-attachments/assets/f8c08dca-dd44-47e4-a954-19947e26ac07)


![image](https://github.com/user-attachments/assets/664da0a9-48ad-4ccf-8af4-10066b3ce877)

Sistema de Campeonatos Deportivos

Este proyecto es un sistema que soporta campeonatos deportivos, considerando deportes en equipo e individuales, inscripción en campeonatos, estadísticas (como tabla de posiciones y estadísticas individuales) y diferentes sistemas de campeonatos (ejemplo: liga, muerte súbita, grupos).

Clases y Enumeraciones

Persona (Abstract Class)
Descripción: Clase base abstracta para representar a una persona en el sistema.

Atributos:

nombre (str): Nombre de la persona.
apellido (str): Apellido de la persona.
identificador (str): Identificador único de la persona.
edad (int): Edad de la persona.
sexo (str): Sexo de la persona.
celular (int): Número de celular de la persona.
Métodos:

registrarse(): Método abstracto para registrar a la persona.
inscribirse(): Método abstracto para inscribir a la persona en un campeonato.
Jugador
Descripción: Clase que hereda de Persona y representa a un jugador.

Atributos:

equipo (str): Equipo al que pertenece el jugador.
estado (bool): Estado del jugador (activo o inactivo).
Métodos:

registrarse(): Registra al jugador.
inscribirse(): Inscribe al jugador en un equipo.
Administrador
Descripción: Clase que hereda de Persona y representa a un administrador.

Métodos:
registrarse(): Registra al administrador.
inscribirse(): Inscribe al administrador.
eliminar_jugador(jugador, equipo): Elimina a un jugador de un equipo.
agregar_jugador(jugador, equipo): Agrega a un jugador a un equipo.
agregar_equipo(equipo, campeonato): Agrega a un equipo a un campeonato.
eliminar_equipo(equipo, campeonato): Elimina a un equipo de un campeonato.
definir_juego(calendario): Define un juego en el calendario.
Arbitro
Descripción: Clase que representa a un árbitro.

Atributos:

deporte (str): Deporte en el que arbitra.
partido_asignado (str): Partido asignado al árbitro.
Métodos:

asignar_partido(partido): Asigna un partido al árbitro.
Equipo
Descripción: Clase que representa a un equipo.

Atributos:

nombre_equipo (str): Nombre del equipo.
id_equipo (str): Identificador único del equipo.
equipo_list (list): Lista de jugadores en el equipo.
puntos (int): Puntos del equipo.
Métodos:

__str__(): Devuelve una representación en string del equipo.
Campeonato
Descripción: Clase que representa un campeonato.

Atributos:

nombre (str): Nombre del campeonato.
fecha_inicio (date): Fecha de inicio del campeonato.
fecha_fin (date): Fecha de fin del campeonato.
equipo_list (list): Lista de equipos en el campeonato.
Métodos:

registrar_equipo(equipo): Registra a un equipo en el campeonato.
registrar_jugador(jugador, equipo): Registra a un jugador en un equipo del campeonato.
calcular_resultado(): Calcula el resultado del campeonato.
calcular_posiciones(): Calcula y muestra las posiciones de los equipos en el campeonato.
Encuentro
Descripción: Clase que representa un encuentro entre dos equipos.

Atributos:

equipo1 (Equipo): Primer equipo.
equipo2 (Equipo): Segundo equipo.
marcador1 (int): Marcador del primer equipo.
marcador2 (int): Marcador del segundo equipo.
Métodos:

mostrar_marcador(): Muestra el marcador del encuentro.
registrar_resultado(): Registra el resultado del encuentro.
CalendarioJuego
Descripción: Clase que representa el calendario de juegos.

Atributos:

encuentro (Encuentro): Encuentro en el calendario.
fecha (date): Fecha del encuentro.
Métodos:

asignar_arbitro(arbitro): Asigna un árbitro para el encuentro.
Estadistica
Descripción: Clase que representa las estadísticas de un campeonato.

Atributos:

punto_total (int): Puntos totales.
victoria (bool): Indica si es victoria.
derrota (bool): Indica si es derrota.
punto_favor (int): Puntos a favor.
punto_contra (int): Puntos en contra.
asistencia (int): Asistencia.
tabla_posicion (list): Tabla de posiciones.
estadistica_list (list): Lista de estadísticas.
Métodos:

calcular_estadistica(): Calcula las estadísticas.
mostrar_estadistica(): Muestra las estadísticas.
calcular_posicion(): Calcula la posición.
mostrar_posicion(): Muestra la posición.
Enumeraciones
Juego
Descripción: Enumeración para los diferentes tipos de juegos.

Valores:
BASQUET
FUTBOL
PINGPONG
ATLETISMO
ModalidadJuego
Descripción: Enumeración para las modalidades de juego.

Valores:
INDIVIDUAL
EQUIPO
Fase
Descripción: Enumeración para las diferentes fases de los campeonatos.

Valores:
DEADSUBITA
FASEGRUPO
LIGA
ELIMINATORIA
GRUPO
Ejemplos de Uso
Creación de Instancias

