"""
Agenda de peliculas.
Módulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.


NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:
        Los diccionarios de pelicula tienen las siguientes parejas de clave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que día de la semana se planea ver la película
"""


def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int,
                   clasificacion: str, hora: int, dia: str) -> dict:
    """Crea un diccionario que representa una nueva película con toda su información
       inicializada.
    Parámetros:
        nombre (str): Nombre de la pelicula agendada.
        genero (str): Generos de la pelicula separados por comas.
        duracion (int): Duracion en minutos de la pelicula
        anio (int): Anio de estreno de la pelicula
        clasificacion (str): Clasificacion de restriccion por edad
        hora (int): Hora a la cual se planea ver la pelicula, esta debe estar entre
                    0 y 2359
        dia (str): Dia de la semana en el cual se planea ver la pelicula.
    Retorna:
        dict: Diccionario con los datos de la pelicula
    """

    pelicula = {
        "nombre": nombre,  # nombre de la pelicula
        "genero": genero,  # genero o tipo de pelicula
        "duracion": duracion,  # duracion en minutos
        "anio": anio,  # año de estreno
        "clasificacion": clasificacion,  # quien puede ver la pelicula
        "hora": hora,  # hora en formato 24h
        "dia": dia  # dia en que se verá
    }
    return pelicula  # retorna el diccionario creado


def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict,  p5: dict) -> dict:
    """Encuentra en cual de los 5 diccionarios que se pasan por parametro esta la
       pelicula cuyo nombre es dado por parametro.
       Si no se encuentra la pelicula se debe retornar None.
    Parametros:
        nombre_pelicula (str): El nombre de la pelicula que se desea encontrar.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: Diccionario de la pelicula cuyo nombre fue dado por parametro.
        None si no se encuentra una pelicula con ese nombre.
    """

    # busca una pelicula comparando el nombre con cada diccionario
    if p1["nombre"] == nombre_pelicula:
        return p1
    elif p2["nombre"] == nombre_pelicula:
        return p2
    elif p3["nombre"] == nombre_pelicula:
        return p3
    elif p4["nombre"] == nombre_pelicula:
        return p4
    elif p5["nombre"] == nombre_pelicula:
        return p5
    else:
        return None  # si no encuentra ninguna retorna none


def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    """Encuentra la pelicula de mayor duracion entre las peliculas recibidas por
       parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: El diccionario de la pelicula de mayor duracion
    """

    # se asume que la primera es la mas larga
    mas_larga = p1

    # se compara con cada una
    if p2["duracion"] > mas_larga["duracion"]:
        mas_larga = p2
    if p3["duracion"] > mas_larga["duracion"]:
        mas_larga = p3
    if p4["duracion"] > mas_larga["duracion"]:
        mas_larga = p4
    if p5["duracion"] > mas_larga["duracion"]:
        mas_larga = p5

    # retorna la pelicula mas larga
    return mas_larga


def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    """Calcula la duracion promedio de las peliculas que entran por parametro.
       Esto es, la duración total de todas las peliculas dividida sobre el numero de peliculas.
       Retorna la duracion promedio en una cadena de formato 'HH:MM' ignorando los posibles decimales.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        str: la duracion promedio de las peliculas en formato 'HH:MM'
    """

    # suma todas las duraciones
    total_minutos = p1["duracion"] + p2["duracion"] + \
        p3["duracion"] + p4["duracion"] + p5["duracion"]

    # calcula el promedio
    promedio_minutos = total_minutos // 5

    # convierte a horas y minutos
    horas = promedio_minutos // 60
    minutos = promedio_minutos % 60

    # formatea horas
    if horas < 10:
        horas_str = "0" + str(horas)
    else:
        horas_str = str(horas)

    # formatea minutos
    if minutos < 10:
        minutos_str = "0" + str(minutos)
    else:
        minutos_str = str(minutos)

    # retorna en hh:mm
    return horas_str + ":" + minutos_str


def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    """Busca entre las peliculas cuales tienen como año de estreno una fecha estrictamente
       posterior a la recibida por parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        anio (int): Anio limite para considerar la pelicula como estreno.
    Retorna:
        str: Una cadena con el nombre de la pelicula estrenada posteriormente a la fecha recibida.
        Si hay mas de una pelicula, entonces se retornan los nombres de todas las peliculas
        encontradas separadas por comas. Si ninguna pelicula coincide, retorna "Ninguna".
    """

    # guarda los nombres de películas que cumplen
    estrenos = ""

    # revisa cada pelicula
    if p1["anio"] > anio:
        estrenos = estrenos + p1["nombre"]

    if p2["anio"] > anio:
        if estrenos != "":
            estrenos = estrenos + ", "
        estrenos = estrenos + p2["nombre"]

    if p3["anio"] > anio:
        if estrenos != "":
            estrenos = estrenos + ", "
        estrenos = estrenos + p3["nombre"]

    if p4["anio"] > anio:
        if estrenos != "":
            estrenos = estrenos + ", "
        estrenos = estrenos + p4["nombre"]

    if p5["anio"] > anio:
        if estrenos != "":
            estrenos = estrenos + ", "
        estrenos = estrenos + p5["nombre"]

    # si no hay ninguna
    if estrenos == "":
        return "Ninguna"
    else:
        return estrenos


def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    """Indica cuantas peliculas de clasificación '18+' hay entre los diccionarios recibidos.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        int: Numero de peliculas con clasificacion '18+'
    """

    contador = 0  # cuenta cuantas cumplen

    if p1["clasificacion"] == "18+":
        contador = contador + 1
    if p2["clasificacion"] == "18+":
        contador = contador + 1
    if p3["clasificacion"] == "18+":
        contador = contador + 1
    if p4["clasificacion"] == "18+":
        contador = contador + 1
    if p5["clasificacion"] == "18+":
        contador = contador + 1

    return contador


def reagendar_pelicula(peli: dict, nueva_hora: int, nuevo_dia: str,
                       control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> bool:
    """Verifica si es posible reagendar la pelicula que entra por parametro. Para esto verifica
       si la nueva hora y el nuevo dia no entran en conflicto con ninguna otra pelicula,
       y en caso de que el usuario haya pedido control horario verifica que se cumplan
       las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula a reagendar
        nueva_hora (int): Nueva hora a la cual se quiere ver la pelicula
        nuevo_dia (str): Nuevo dia en el cual se quiere ver la pelicula
        control_horario (bool): Representa si el usuario quiere o no controlar
                                el horario de las peliculas.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        bool: True en caso de que se haya podido reagendar la pelicula, False de lo contrario.
    """

    # Verificar conflictos de horario con otras peliculas (mismo dia y misma hora de inicio)
    # No se compara la pelicula consigo misma
    if p1["nombre"] != peli["nombre"]:
        if p1["dia"] == nuevo_dia and p1["hora"] == nueva_hora:
            return False
    if p2["nombre"] != peli["nombre"]:
        if p2["dia"] == nuevo_dia and p2["hora"] == nueva_hora:
            return False
    if p3["nombre"] != peli["nombre"]:
        if p3["dia"] == nuevo_dia and p3["hora"] == nueva_hora:
            return False
    if p4["nombre"] != peli["nombre"]:
        if p4["dia"] == nuevo_dia and p4["hora"] == nueva_hora:
            return False
    if p5["nombre"] != peli["nombre"]:
        if p5["dia"] == nuevo_dia and p5["hora"] == nueva_hora:
            return False

    # Verificar superposicion horaria en el mismo dia con otras peliculas
    # Una pelicula ocupa desde su hora de inicio hasta hora_inicio + duracion

    nueva_hora_fin = nueva_hora + peli["duracion"]

    if p1["nombre"] != peli["nombre"] and p1["dia"] == nuevo_dia:
        hora_fin_p1 = p1["hora"] + p1["duracion"]
        if nueva_hora < hora_fin_p1 and nueva_hora_fin > p1["hora"]:
            return False
    if p2["nombre"] != peli["nombre"] and p2["dia"] == nuevo_dia:
        hora_fin_p2 = p2["hora"] + p2["duracion"]
        if nueva_hora < hora_fin_p2 and nueva_hora_fin > p2["hora"]:
            return False
    if p3["nombre"] != peli["nombre"] and p3["dia"] == nuevo_dia:
        hora_fin_p3 = p3["hora"] + p3["duracion"]
        if nueva_hora < hora_fin_p3 and nueva_hora_fin > p3["hora"]:
            return False
    if p4["nombre"] != peli["nombre"] and p4["dia"] == nuevo_dia:
        hora_fin_p4 = p4["hora"] + p4["duracion"]
        if nueva_hora < hora_fin_p4 and nueva_hora_fin > p4["hora"]:
            return False
    if p5["nombre"] != peli["nombre"] and p5["dia"] == nuevo_dia:
        hora_fin_p5 = p5["hora"] + p5["duracion"]
        if nueva_hora < hora_fin_p5 and nueva_hora_fin > p5["hora"]:
            return False

    # Aplicar control horario si esta activado

    if control_horario:
        genero = peli["genero"]
        dia_lower = nuevo_dia.lower()

        # No programar documentales a las 22:00 (2200) o más tarde
        if "Documental" in genero and nueva_hora >= 2200:
            return False

        # No programar dramas los viernes
        if "Drama" in genero and dia_lower == "viernes":
            return False

        # Entre semana: no antes de las 6:00 am ni a las 23:00 o más tarde
        dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes"]
        if dia_lower in dias_semana:
            if nueva_hora >= 2300 or nueva_hora < 600:
                return False

    # Si pasa las regulaciones, se reagenda
    peli["hora"] = nueva_hora
    peli["dia"] = nuevo_dia
    return True


def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool) -> bool:
    """Verifica si es posible invitar a la persona cuya edad entra por parametro a ver la
       pelicula que entra igualmente por parametro.
       Para esto verifica el cumplimiento de las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula que se desea ver con el invitado
        edad_invitado (int): Edad del invitado con quien se desea ver la pelicula
        autorizacion_padres (bool): Indica si el invitado cuenta con la autorizacion de sus padres
        para ver la pelicula
    Retorna:
        bool: True en caso de que se pueda invitar a la persona, False de lo contrario.
    """

    genero = peli["genero"]
    clasificacion = peli["clasificacion"]

    # Los mayores de 18 pueden ver cualquier pelicula
    if edad_invitado >= 18:
        return True

    # Los menores de 15 no pueden ver peliculas de terror
    if edad_invitado < 15 and "Terror" in genero:
        return False

    # Los de 10 o menos solo pueden ver pelicular del genero familiar
    if edad_invitado <= 10 and "Familiar" not in genero:
        return False

    # Si la edad no cumple la clasificacion, se requiere autorizacion de padres
    # Exepto en documentales

    if "Documental" not in genero:
        cumple_clasificacion = False

        if clasificacion == "Todos":
            cumple_clasificacion = True
        elif clasificacion == "7+" and edad_invitado >= 7:
            cumple_clasificacion = True
        elif clasificacion == "13+" and edad_invitado >= 13:
            cumple_clasificacion = True
        elif clasificacion == "16+" and edad_invitado >= 16:
            cumple_clasificacion = True
        elif clasificacion == "18+" and edad_invitado >= 18:
            cumple_clasificacion = True

        if not cumple_clasificacion and not autorizacion_padres:
            return False

    return True
