from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.markup import escape

console = Console()

# se usa para poner los paneles rich a los dialogos de nebula
def mensaje(texto, titulo="NEBULA", color="cyan"):
    console.print(Panel(texto, title=titulo, border_style=color))

# bucle para poner las opciones al usuario
def elegir(pregunta, opciones):
    while True:
        respuesta = Prompt.ask(pregunta).strip()
        if respuesta in opciones:
            return respuesta
        console.print("[red]Opción no válida. Inténtalo otra vez.[/red]")


# muestra las variables de la mision como el valor gnc y combustible. usa una tabla rich
def mostrar_estado(estado):
    tabla = Table(title="TELEMETRÍA SUPER HEAVY")
    tabla.add_column("Sistema", style="cyan")
    tabla.add_column("Estado", style="white")
    tabla.add_row("Combustible", f"{estado['combustible']} %")
    tabla.add_row("Integridad GNC", f"{estado['gnc']} %")
    tabla.add_row("Riesgo", f"{estado['riesgo']} puntos")
    tabla.add_row("Inventario", ", ".join(estado["inventario"]))
    console.print(tabla)


def preparar_recuperacion(estado):
    """
    Misión 1: preparar el propulsor.
    Las decisiones modifican variables y añaden elementos a la lista inventario.
    """
    # se muestra el mensaje dentro de la funcion mensaje
    mensaje(
        "Starship se ha separado correctamente.\n"
        "Super Heavy inicia su regreso. Quedan pocos minutos para decidir.\n"
        "MCC: podemos preparar sistemas antes de elegir la recuperación.",
        "FASE 1: PREPARACIÓN",
    )

    # opciones para el usuario. telemetria llama a la funcion con la tabla rich
    while True:
        console.print(
            "\n[bold]1.[/bold] Calibrar guiado GNC (consume 5 % combustible)\n"
            "[bold]2.[/bold] Revisar motores de aterrizaje (consume 5 % combustible)\n"
            "[bold]3.[/bold] Preparar brazos de Mechazilla\n"
            "[bold]4.[/bold] Consultar telemetría\n"
            "[bold]5.[/bold] Elegir maniobra de recuperación"
        )
        opcion = elegir("Tu decisión", ["1", "2", "3", "4", "5"])

        # todas las opciones no te dejan hacerlo dos veces. se guarda si esta hecho en un diccionario estado
        if opcion == "1":
            if estado["gnc_calibrado"]:
                console.print("[yellow]El GNC ya ha sido calibrado.[/yellow]")
            else:
                # quitamos 5 de combustile y anadimos 20 a gnc porque lo hemos calibrado
                estado["combustible"] -= 5
                estado["gnc"] += 20
                # usamos true y false para ver si el usuario ha hecho la accion
                estado["gnc_calibrado"] = True
                estado["inventario"].append("GNC calibrado")
                mensaje("Sensores sincronizados. La precisión de guiado ha mejorado.")

        elif opcion == "2":
            if estado["motor_revisado"]:
                console.print("[yellow]La revisión de motores ya está hecha.[/yellow]")
            else:
                estado["combustible"] -= 5
                estado["motor_revisado"] = True
                estado["inventario"].append("Motores revisados")
                mensaje("Presiones correctas. Motor listo para la maniobra de frenado.")

        elif opcion == "3":
            if estado["brazos_preparados"]:
                console.print("[yellow]Mechazilla ya está preparada.[/yellow]")
            else:
                estado["brazos_preparados"] = True
                estado["riesgo"] -= 10
                estado["inventario"].append("Torre sincronizada")
                mensaje("MCC: brazos de Mechazilla preparados para el atrapado.")

        # muestra la tabla rich
        elif opcion == "4":
            mostrar_estado(estado)

        else:
            return

# define la funcion para decidir el final. es una funcion que recibe 2 parametros - el diccionario estado (que el usuario ha creado eligiendo respuestas) y tipo ()
def final_super_heavy(estado, tipo):
    # un diccionario de tuples con todas las posibilidades que puede salir. 
    finales = {
        "final_2": (
            "FINAL 2 — IMPACTO EN TORRE",
            "El propulsor no logra alinearse con los brazos de Mechazilla.\n"
            "Impacta contra la estructura de Starbase. Misión de recuperación fallida.",
            "red"
        ),
        "final_3": (
            "FINAL 3 — AMERIZAJE FORZOSO",
            "La maniobra de emergencia no consigue estabilizar el propulsor.\n"
            "Super Heavy cae al Golfo de México y se pierde.",
            "red"
        ),
        "final_4": (
            "FINAL 4 — RECUPERACIÓN PARCIAL",
            "Super Heavy logra un amerizaje suave cerca de la plataforma marítima.\n"
            "El propulsor sobrevive, pero necesitará una revisión completa.",
            "yellow"
        ),
        "super_heavy_recuperado": (
            "SUPER HEAVY RECUPERADO",
            "Mechazilla atrapa el propulsor correctamente.\n"
            "¡Operación completada! Ahora continúa la misión de Starship.",
            "green"
        ),
    }
    # asignamos una variable a cada valor en el tuple para seguirlo
    titulo, descripcion, color = finales[tipo]

    # muestra el final dependiendo de lo que ha eligido el usuario
    mensaje(descripcion, titulo, color)
    mostrar_estado(estado)
    # devuelve el identificador a la funcion principal
    return tipo

# la rama de la capturacion del super heavy por la torre mechazilla
def maniobra_torre(estado):
    """Misión 2A: intentar capturar el propulsor en la torre."""
    mensaje(
        "MCC: estás a pocos kilómetros de Starbase.\n"
        "Elige la velocidad de aproximación al sistema de brazos.\n"
        "Una aproximación rápida consume menos combustible, pero aumenta el riesgo.",
        "FASE 2: MECHAZILLA",
    )
    console.print("1. Aproximación segura (consume 15 % combustible)")
    console.print("2. Aproximación rápida (consume 5 % combustible)")
    opcion = elegir("Velocidad", ["1", "2"])

    if opcion == "1":
        estado["combustible"] -= 15
        estado["riesgo"] = max(0, estado["riesgo"] - 5)
    else:
        estado["combustible"] -= 5
        estado["riesgo"] += 25
        estado["gnc"] -= 10
        mensaje("Aproximación rápida iniciada. El GNC pierde precisión por las vibraciones.", "ALERTA", "yellow")

    mostrar_estado(estado)

# aqui se accede al diccionario estado para ver lo que ha hecho el usuario. por ejemplo, si no existe el valor brazos_preparados (el usuario se lo ha saltado), usamos la funcion de final para mostrar el estado y el final
    if not estado["brazos_preparados"]:
        mensaje("¡Alerta! Los brazos de Mechazilla no estaban preparados.", "MCC", "red")
        return final_super_heavy(estado, "final_2")

    if estado["gnc"] < 65:
        mensaje(
            "El guiado GNC no puede mantener la trayectoria de aterrizaje.\n"
            "1. Intentar atrapar el cohete igualmente\n"
            "2. Desviarlo al océano",
            "FALLO DE GUIADO",
            "red",
        )
        opcion = elegir("Maniobra de emergencia", ["1", "2"])
        if opcion == "1":
            return final_super_heavy(estado, "final_2")
        return final_super_heavy(estado, "final_3")

    if estado["combustible"] < 30:
        mensaje("No queda suficiente combustible para estabilizar el descenso.", "MCC", "red")
        return final_super_heavy(estado, "final_3")

    if estado["riesgo"] > 35:
        mensaje("La velocidad de aproximación supera el margen de seguridad.", "MCC", "red")
        return final_super_heavy(estado, "final_2")

    return final_super_heavy(estado, "super_heavy_recuperado")



# si el usuario elige mandar el heavy al oceano
def maniobra_oceano(estado):
    """Misión 2B: elegir entre un amerizaje controlado o arriesgado."""
    mensaje(
        "MCC: se abandona la maniobra de torre.\n"
        "El propulsor apunta al Golfo de México.\n"
        "Ahora hay que controlar el descenso con los motores.",
        "FASE 2: OCÉANO",
    )
    console.print("1. Amerizaje controlado (consume 20 % combustible)")
    console.print("2. Descenso rápido (consume 5 % combustible)")
    opcion = elegir("Tipo de descenso", ["1", "2"])

    if opcion == "1":
        estado["combustible"] -= 20
        estado["riesgo"] = max(0, estado["riesgo"] - 5)
    else:
        estado["combustible"] -= 5
        estado["riesgo"] += 25

    if opcion == "1":
        mensaje("MCC: iniciando frenado progresivo. Descenso estable.", "TELEMETRÍA", "cyan")
    else:
        mensaje("MCC: descenso rápido. Aumenta el riesgo de perder el control.", "ALERTA", "yellow")

    # Requisitos: motor revisado, combustible, riesgo y guiado suficiente.
    if not estado["motor_revisado"]:
        mensaje("Los motores no se revisaron. El motor de frenado falla.", "FALLO DE MOTOR", "red")
        return final_super_heavy(estado, "final_3")

    if estado["combustible"] < 25 or estado["riesgo"] > 35 or estado["gnc"] < 60:
        mensaje("El aterrizaje pierde estabilidad. Se activa el desvío de emergencia.", "MCC", "red")
        return final_super_heavy(estado, "final_3")

    return final_super_heavy(estado, "final_4")

# la funcion inicial despues de eligir lanzar 
def recuperacion_super_heavy(nombre):
    # el estado inicial con los valores por defecto con los que empezamos
    estado = {
        "nombre": nombre,
        "combustible": 75,
        "gnc": 60,
        "riesgo": 20,
        "inventario": ["checklist de vuelo"],
        "gnc_calibrado": False,
        "motor_revisado": False,
        "brazos_preparados": False,
    }
    mensaje(
        f"[bold]Ingeniero {escape(nombre)}:[/bold]\n"
        "Super Heavy ha completado la separación de etapas.\n"
        "Starship continúa su ascenso, mientras el propulsor inicia el regreso.",
        "SEPARACIÓN COMPLETADA",
    )

    preparar_recuperacion(estado)

    mensaje(
        "1. Recuperar Super Heavy con los brazos de Mechazilla (torre)\n"
        "2. Intentar un amerizaje controlado en el océano",
        "ELEGIR MODO DE RECUPERACIÓN",
    )
    # dependiendo de lo que elige el usario se devuelve una de las 2 funciones. Las 2 accederan a los valores el el diccionario estado para determinar el final
    opcion = elegir("Ruta", ["1", "2"])
    if opcion == "1":
        return maniobra_torre(estado)
    return maniobra_oceano(estado)
