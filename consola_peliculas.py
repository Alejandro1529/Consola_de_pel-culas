"""
Agenda de peliculas.
Modulo de interacci0n por consola.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.

"""
import modulo_peliculas as mod


def mostrar_informacion_pelicula(pelicula: dict) -> None:
    """Imprime los detalles de la pelicula
    Parametros:
        pelicula(dict): La pelicula de la cual se van a mostrar los detalles
        El diccionario que representa una pelicula contiene las siguientes parejas de
        llave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que dia de la semana se planea ver la pelicula
    """
    # obtiene los datos del diccionario
    nombre = pelicula["nombre"]
    genero = pelicula["genero"]
    duracion = pelicula["duracion"]
    anio = pelicula["anio"]
    clasificacion = pelicula["clasificacion"]
    hora = pelicula["hora"]
    dia = pelicula["dia"]

    # imprime informacion basica
    print("Nombre: " + nombre + " - Anio: " + str(anio) +
          " - Duracion: " + str(duracion) + "  mins")
    # imprime genero y clasificacion
    print("Genero: " + genero + " - Clasificacion: " + clasificacion)

    # formatea la hora
    if (hora//100 < 10):
        hora_formato = "0" + str(hora//100)
    else:
        hora_formato = str(hora//100)

    if (hora % 100 < 10):
        min_formato = "0" + str(hora % 100)
    else:
        min_formato = str(hora % 100)

    # imprime dia y hora
    print("Dia: " + dia + " Hora: " + hora_formato + ":" + min_formato)


def ejecutar_encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    """Ejecuta la opcion de encontrar la pelicula mas larga.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """

    print("Pelicula mas larga de la agenda: ")
    # llama funcion del modulo
    pelicula_larga = mod.encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)
    # muestra resultado
    mostrar_informacion_pelicula(pelicula_larga)


def ejecutar_consultar_duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    """Ejecuta la opcion de consultar la duracion promedio de las peliculas.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """

    # obtiene promedio y lo imprime
    promedio = mod.duracion_promedio_peliculas(p1, p2, p3, p4, p5)
    print("Duracion promedio de las peliculas de la agenda: " + promedio)


def ejecutar_encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    """ Ejecuta la opcion de buscar peliculas de estreno. Esto es: las peliculas que sean
        mas recientes que un anio dado.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """

    # pide el año al usuario
    anio_str = input("Ingrese el año limite para buscar estrenos: ")
    anio = int(anio_str)
    # busca estrenos
    estrenos = mod.encontrar_estrenos(p1, p2, p3, p4, p5, anio)
    print("Peliculas estrenadas despues de " + str(anio) + ": " + estrenos)


# llama la funcion
def ejecutar_cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    """Ejecuta la opcion de consultar cuantas peliculas de la agenda tienen clasificacion
    18+.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """

    # Llama a la función del módulo que hace el conteo y la imprime
    cantidad = mod.cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)
    print("Cantidad de peliculas con clasificacion 18+: " + str(cantidad))

# Esta función permite al usuario cambiar el día y la hora de una película


def ejecutar_reagendar_pelicula(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    """Ejecuta la opcion de reagendar una pelicula
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    print("Reagendar una pelicula de la agenda")

    # se pide el nombre de la pelicula5
    nombre = input(
        "Ingrese el nombre de la pelicula que desea reagendar: ").title()
    # se busca la pelicula en los diccionarios
    pelicula = mod.encontrar_pelicula(nombre, p1, p2, p3, p4, p5)

    if pelicula is None:  # si no existe
        print("No hay ninguna pelicula con este nombre")

    else:  # se piden los nuevos datos
        nueva_hora_str = input("Ingrese la nueva hora (formato 24h): ")
        nueva_hora = int(nueva_hora_str)
        nuevo_dia = input("Ingrese el nuevo dia de la semana: ")
        control_str = input(
            "¿Desea activar el control horario? (s/n): ").strip().lower()
        control_horario = control_str == "s"

        # se intenta reagendar llamando la funcion del módulo
        resultado = mod.reagendar_pelicula(
            pelicula, nueva_hora, nuevo_dia, control_horario, p1, p2, p3, p4, p5)

        if resultado:
            print("La pelicula '" + nombre + "' fue reagendada exitosamente para el " +
                  nuevo_dia + " a las " + nueva_hora_str + ".")
        else:
            print("No fue posible reagendar la pelicula. Verifique que no haya conflictos " +
                  " de horario o que se cumplan las restricciones de control horario.")

      # Esta función nos permite saber si una persona puede ver una película


def ejecutar_decidir_invitar(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    """Ejecuta la opcion de decidir si se puede invitar a alguien a ver una pelicula o no.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    print("Decidir si se puede invitar a alguien a ver una pelicula")
    # Se pide el nombre de la película
    nom_peli = input("Ingrese el nombre de la pelicula: ")
    # Se busca la película
    pelicula = mod.encontrar_pelicula(nom_peli, p1, p2, p3, p4, p5)

    if pelicula is None:  # si no existe
        print("No hay ninguna pelicula con este nombre")

    else:  # se piden los datos del invitado
        edad_str = input("Ingrese la edad del invitado: ")
        edad = int(edad_str)
        autorizacion_str = input(
            "¿El invitado cuenta con autorizacion de sus padres? (s/n): ").strip().lower()
        autorizacion = autorizacion_str == "s"

        # Se verifica si puede ver la película
        puede_invitar = mod.decidir_invitar(pelicula, edad, autorizacion)

        # Se muestra el resultado
        if puede_invitar:
            print("Si se puede invitar a la persona a ver '" + nom_peli + "'.")
        else:
            print("No se puede invitar a la persona a ver '" + nom_peli + "'.")


# Esta función inicia todo el programa
def iniciar_aplicacion():
    """Inicia la ejecución de la aplicación por consola.
    Esta funcion primero crea las cinco peliculas que se van a manejar en la agenda.
    Luego la funcion le muestra el menu al usuario y espera a que seleccione una opcion.
    Esta operacion se repite hasta que el usuario seleccione la opcion de salir.
    """
    # Se crean las 5 películas iniciales usando el módulo
    pelicula1 = mod.crear_pelicula(
        "Buscando A Nemo",  "Familiar, Animación", 101, 2003, 'Todos', 850, "Martes")
    pelicula2 = mod.crear_pelicula(
        "El Conjuro",  "Suspenso, Terror", 112, 2013, '16+', 1400, "Miércoles")
    pelicula3 = mod.crear_pelicula(
        "Blackfish",  "Documental, Drama", 83, 2013, '13+', 1100, "Lunes")
    pelicula4 = mod.crear_pelicula(
        "El Padrino",  "Drama, Crimen", 177, 1972, '18+', 1700, "Domingo")
    pelicula5 = mod.crear_pelicula(
        "Deadpool",  "Acción, Comedia", 108, 2016, '18+', 2030, "Sabado")

    ejecutando = True  # controla el ciclo del programa
    while ejecutando:  # bucle principal
        # muestra toda la agenda
        print("\n\nMi agenda de peliculas para la semana de receso" + "\n"+("-"*50))
        print("Pelicula 1")
        mostrar_informacion_pelicula(pelicula1)
        print("-"*50)

        print("Pelicula 2")
        mostrar_informacion_pelicula(pelicula2)
        print("-"*50)

        print("Pelicula 3")
        mostrar_informacion_pelicula(pelicula3)
        print("-"*50)

        print("Pelicula 4")
        mostrar_informacion_pelicula(pelicula4)
        print("-"*50)

        print("Pelicula 5")
        mostrar_informacion_pelicula(pelicula5)
        print("-"*50)

        # muestra el menu y guarda si sigue ejecutando
        ejecutando = mostrar_menu_aplicacion(
            pelicula1, pelicula2, pelicula3, pelicula4, pelicula5)
        # pausa antes de repetir
        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")


def mostrar_menu_aplicacion(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> bool:
    """Le muestra al usuario las opciones de ejecución disponibles.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorno:
        Esta funcion retorna True si el usuario selecciono una opcion diferente
        a la opcion que le permite salir de la aplicacion.
        Esta funcion retorna False si el usuario selecciono la opción para salir
        de la aplicacion.
    """
    # Muestra el menú y ejecuta la opción elegida
    print("Menu de opciones")
    print(" 1 - Consultar pelicula mas larga")
    print(" 2 - Consultar duracion promedio de las peliculas")
    print(" 3 - Consultar peliculas de estreno")
    print(" 4 - Consultar cuantas peliculas tienen clasificacion 18+")
    print(" 5 - Reagendar pelicula")
    print(" 6 - Verificar si se puede invitar a alguien")
    print(" 7 - Salir de la aplicacion")

    # El usuario elige una opción
    opcion_elegida = input("Ingrese la opcion que desea ejecutar: ").strip()

    continuar_ejecutando = True  # por defecto sigue

    # Dependiendo de la opción, llama una función
    if opcion_elegida == "1":
        ejecutar_encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)
    elif opcion_elegida == "2":
        ejecutar_consultar_duracion_promedio_peliculas(p1, p2, p3, p4, p5)
    elif opcion_elegida == "3":
        ejecutar_encontrar_estrenos(p1, p2, p3, p4, p5)
    elif opcion_elegida == "4":
        ejecutar_cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)
    elif opcion_elegida == "5":
        ejecutar_reagendar_pelicula(p1, p2, p3, p4, p5)
    elif opcion_elegida == "6":
        ejecutar_decidir_invitar(p1, p2, p3, p4, p5)
    elif opcion_elegida == "7":
        continuar_ejecutando = False
    else:
        print("La opcion " + opcion_elegida + " no es una opcion valida.")

    return continuar_ejecutando


# inicia el programa
iniciar_aplicacion()
