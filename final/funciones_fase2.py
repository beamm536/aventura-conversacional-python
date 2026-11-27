from rich.panel import Panel
from rich.text import Text
from rich import print
from rich.prompt import Prompt
from rich.align import Align
from rich.console import Console
from rich.live import Live
from rich.table import Table
import time
import random
import explosion_starship



# -------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------FUNCIONES CONTEXTO HISTORIA-------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------

def pista_angulo_entrada():
    pista_texto = Text()
    pista_texto.append("📂 ARCHIVO TÉCNICO // REGISTROS DE PRUEBAS\n\n", style="bold cyan")
    pista_texto.append("Los registros históricos de pruebas indican que el pasillo seguro de reentrada se sitúa estrictamente entre los ", style="white")
    pista_texto.append("-0.8°", style="bold yellow")
    pista_texto.append(" y los ", style="white")
    pista_texto.append("-2.0°", style="bold yellow")
    pista_texto.append(".\n\nLos ingenieros recuerdan que el punto de máximo rendimiento aerodinámico y menor estrés térmico suele encontrarse ", style="white")
    pista_texto.append("ligeramente por debajo de la mitad de ese rango...", style="italic green")

    # Mostramos el panel estilizado en la terminal
    print(Panel(pista_texto, title="[cyan]MANUAL DE VUELO DE LA STARSHIP[/cyan]", border_style="cyan", padding=(1, 2)))

# -------------------------------------------------------------------------------------------------------------------------------------

def comunicado_mcc():
    comunicado = Text()
    comunicado.append("📡 COMUNICADO OFICIAL // MISIÓN STARSHIP\n\n", style="bold cyan")
    comunicado.append("Ángulo de entrada validado y fijado con éxito. Trayectoria estabilizada dentro del pasillo óptimo.\n\n", style="white")
    comunicado.append("Todas las estaciones de control confirman estado nominal. Pasamos de inmediato al ", style="white")
    comunicado.append("monitoreo en tiempo real del escudo térmico", style="bold green")
    comunicado.append(" ante el incremento de fricción atmosférica.", style="white")

    # Mostramos el panel en la terminal
    print(Panel(comunicado, title="[green]MCC - CONTROL DE MISIÓN[/green]", border_style="green", padding=(1, 2)))

# -------------------------------------------------------------------------------------------------------------------------------------

# EN CASO DE QUE EL USUARIO CONTINUE CON UN VALOR, QUE NO SEA EL IDEAL ENTONCES QUE EL ESCUDO TERMICO SE VEA AFECTADO PERO FINALEMENTE ATERRICE
def comunicado_mcc_con_susto():
    comunicado = Text()

    comunicado.append("📡 COMUNICADO OFICIAL // MISIÓN STARSHIP\n\n", style="bold cyan")
    comunicado.append("Trayectoria asegurada, aunque el control de telemetría advierte sobre un esfuerzo térmico elevado debido a la imprecisión del ángulo.\n\n", style="yellow")
    comunicado.append("Aceptamos el riesgo. Pasamos con precaución al ", style="white")
    comunicado.append("monitoreo en tiempo real del escudo térmico", style="bold green")
    comunicado.append(".", style="white")

    print(Panel(comunicado, title="[yellow]CONTROL DE MISIÓN (MCC) - AVISO[/yellow]", border_style="yellow", padding=(1, 2)))



# -------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------CONTEXTO MONITOREO ESCUDO----------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------

def starship_losetas_termicas_ascii():
    print(Align.center(r"""




                                                                                                                                                      _________________
                                                                                                                                                __________        __________
                                                                                                                                             _______/__              __\________
                                                                                                                                          //________                    _________\\
                                                                                                                                        .//_____.                           _____\\_
                                                                                                                                      _..__..                                  ..__.._\\
                                                                                                                                   .__.....         _____________________   _   .......\\\
                                                                                                                                 .........                                        .......\.
                                                                                                                               ///.......                    |                    ........\\\
                                                                                                                              //........                     |                     .........\\
                                                                                                                             ///.....                                               ... .....\\\
                                                                                                                           |\+/....     ||                   .                    /|       ..\\/+
                                                                                                                            __.          |               __________               |           +_
                                                                                                                                         |  ___       ______    ______.      ___  |
                                                                                                                                        /       _  ////_            __\\\.\__      \\
                                                                                                                                       /          ////                \\\\.         \\
                                                                                                                                     //         .///.                   \\\.         \\
                                                                                                                                    //         ////.____________________\\\\\         \\            /
                                                                                                                        ___         /         ////./..               .._\..\\\         \         ___/        \
                                                                                                              /                    /         ////./_+.            ...../+_\.\\\         \                    \
                                                                                                              /                   /         ////.....++._____________.+......\\\.        \\                  |
                                                                                                                                 /      .___//.______________________________.\\___..     \.
                                                                                                                              ____  ._______/..................................________.. ____
                                                                                                                           ______\\____..__.._//....//................\\....\___.__..___+/_______
                                                                                                          +           ________   \|..__________....//..................\\.....__________.._.   _______           ++
                                                                                                      ___+\\      _________     //|..+............/......................\\..........._..\\\.    __________      //__ _
                                                                                                     ///  \\ ________         /////.............../.......................\...............\\\\         ________ //  _\\\
                                                                                                    //     \\____            ////. ..............\\......................//............... \\\\            ____||     \\\
                                                                                                  ///      //.  _+          ////           .......\\\...................///................ \\\\_         \_   \\\     \\\
                                                                                                ////      /// /|_/ +______/////            ........\\\................///..................   \\\_______+ \__\ \\\      \\___
                                                                                             //////      ///| ||\  +\\_____//             ..........\\\..............///....................    \______/+  //|  \\\      \\_\\\
                                                                                           _///////     ///    \\   _____                 .........../________________/................... .       _____   //    \\\      \\\\\\__
                                                                                     ______:::+///     ///     //|                       ...........///______________\\\....................              ||\\     \\      \\\:::___+__
                                                                                   /__/+:::::::|/     //      ///||           \\         ..........///................\\\..................../            |\\\\     \\     \|\::::::.\\_\
                                                                                __/////.:::::::/|    //      /////             \\       ..........///..................\\\\................///.           \\\\\\     \\    |\\::::::::\\\\\\
                                                                              ______//.:::::::/.  __||      /////               \\      .........///....................\\\\..............//....           \\\\\      ||+_  .\:::::::.\\\\\\_\
                                                                           _____///:|..:::::://____+\||    /////                 \\.....________///.......................\\\________...../.....            \\\\\     ||+____.\::::::::\:\\\_____
                                                                         ___//__:..\\\::::::// _     ||   /////                  /|/____________//......................../______________+/.....             \\\\\   /||    _.\|:::::::|/::____\\__
                                                                       ////////......\+.::://        \++___//                   ////...____.......\\.....................//.......____..\\\\.....              \\____+/        \\::::++:...:.:\\__\\\\
                                                                    ____////........./|...//         ///___   \               ./////  .............\\..................///...............\\\\\.              /   ___\\|        .\\::::\:..:::::.\\\\\\_.
                                                                 _________......./_.//../://        ////      \\             /////.  ...............\\................//..................\\\\\..           //      \\\\        \\:\:.\\:+::.......\_______
                                                               ________.........//./|....:|        ///         \\           /////     ...............\\______________//....................\\\\\..         //         \\\        \\:::.:::|\........._____\__
                                                            _//_____............//.:/.::://       ///           \+___________//        ...............________________.......................\\\__________+/           \\\       \\:::.|::\\\..........._____\\
                                                          //__/___.............////__.:|//       ///            //___________\\      ........................................................./_____._____\\            \\\       \\||:\_\.||.............___\____
                                                       /__/////................// ......//      ///            ///          \\\\      ......................................................////....      \\\            \\\      .\::::::.\\................__\\\__
                                                    ____/___/.................///.....///  _____\\            ///            \\.\    ................../______________.....................////.....       \\\            ||_____..\\\.::...\\.................\___\\\.
                                                   ./_____...................///..... ./  /___   \\          ///  /_______+   \\|\  ..................///____________+...................../|/...._.______. \\\          //   ___\ .\\..:::.\\\...................__\____
                                                ____/_//.....................//......///  /      \\         ///   +_____      ./||  ..................|\_____________\....................||\\......|_____+   \\         //      \..\\|.::::.\\......................\______
                                             ________.......................///..... .|| //       \\   _____//     +_____+   .///   ...................._____________||....................\\\\...+_+__.+      \\_____  //       \\..|:..:::.\\\......................._______
                                          _________.........................//.....//// //        |||+_____ \\   _____ __   ////   ...................+_____________/||......................\\\..._.__.__.   /| _____+++/        \\.\:\\.:::.\\\.........................____\\.
                                        __/_____...........................///.....//:/ /         ||||       \\            ////    ...................+_______________........................\\\.......     .||       |||         ..\\\||.::.\\\...........................__\\____
                                     //___/___............................/// ....||://|         ////        \\\          ////    .............................................................\\\.......   ///        \\\\        .\.\:||.:::.\\\.............................______\
                                    ///___/.................___...........///......:// |        /////         \\\__________/      ..............................................................\\_________.//          \\\\        ..\\:::.:::.\\...........___.................\___\__
                                 ._///___....................._____......///.......:|/ |       /////           \\____     \\\    ...............................................................//......____/            \\\\       ...||::..::.\\\......_____......................___\___
                              /_____//............................___....//........:|  +      /////                        \\\    .........____../+____...+...../____../____..++....______.....//..........              \\\\\     .+..|::::.:::.\\....___............................\_____\
                            ///____.......\.............................///.......::|  /_______\/                           \\\   .......//___\\./+/___...+\\..//......////_...______.........//...........                \|_______\..|:::::::::\\:....................................._____\\
                           /|///_................../....................// .......:||  ____   \\\                            \\\ ........\____//.+/___..______.______..\+____.///___\........//..............              ///   ____..||::::::::.\\....................|...................\\\\\
                           .|||........................................///.......::|  /+       \\                             \\\++.._____+___.\\\........................///....___\\+...++//.............                ///      .\..|\::::::::\|\........................................\|||
                           ||||.......................................///........:|| //        \\\                           /|||+..............\\\......................////.............+||||............               ///        \\.||::::::::.\\:......................................:||||
                           ||||.......................................///.......::|| /          |//      \                  ///// ...............\\\....................////................\\\\............      /      \\\|         ...|:::::.::::\\.......................................|||||
                          .||||......................................///........:.| .          /++       \\               .///// .................\\\..................////..................\\\\............    //       \\\        ....|:::::::::.\\\......................................:||||
                          ||||.......................+...............//.........:|||          //          \\             .///// ...................\\\................///.....................\\\\............. //           \        ...||:::::.:::.\\.......................................||||
                          ||||......................................///..........||          //            \\           __////  ....................\\/_______________//.......................\\\__...........//            \\       ....|:::::.::::\\\......................................||||.
                         |||||........_............................///.........:.|          //      _ __    \______________+.. .....................///.._..____._._.\\\\.......................:______________/.   +__       \\      ....|:::::..:::.\\\...........................__........:||||
                         ||||......................................///..........||  |      //   /_______    ////__         \\\. ..................////................\\\\....................///..........__\\\    _______++  \\      |..||:::::.::::.\\......................................||||
                        |||||.....................................///.\\......::||  .  ___++    ++____     ////             \\\..................////..................\\\\...................//.............\\\\     ++_ _     ++____ ....|:::::..::::\\\.....................................||||
                        |||||.....................................//.::\...++.::|   /____ +\     +__      ////               \\\................////.....................\\\\................//...............\\\\     __ _     |+______...|:::++::./::..\.....................................|||||
                        .||||....................................|||:|/:...||::||   /_     \\            ////                 \\\..............////.....+.______.__++.....\\\..............///..................\\\            //     ._\..\|:::|::::\\::||....................................:||||
                        |||||..................................../||:|/...:|:::||  /        \\          ////                   \\/_____________+/.......+_._________.......\\_____________\//...................\\\\           //       \..||:::|::::\:::\|.....................................||||
                       |||||....................................///::/:...||:::|  //        \\         _//|                   .///..._._.___.__\\\.........+__._+.........///.___..___..__\\\\.................. |\\_         //        .\..|:::||.:::\::\\\....................................\|||.
                       .||||..............____.................///:::/....|:::|| //          \__________\\||                 .///...............\\\\......._.............////..............\\\\.................|||/__________/         .\\.|::::|.:::::::\\\.................____..............:||||
                       .|||..................._................///::/:...:|:::|| |           /__         \\\                ./// ................\\\\...................////.................\\\................|///.       __\\        ..|..|:::\:::::\:::\\................_...................||||
                       ||||...................................///:::/....||:::|| |          ////          \\ \             //// ..................\\\\.................///....................\\\...............///..       \ \\\       .....:::::|::::::::\\\...................................||||
                      .||||......................|............//:::+.....|::::|  |         ///            \\\\\         ...///.....................\\\\...............///......................\\\............////...         \\\        .|..|::::|:::::+::::\\..................................|||||
                      ./|||......................|...........///::::.....|::::|  ||       ///         _+   \\\| +_________/// ......................\\\:____:::::____+//........................\\__________..|//......        \\\       .|..|::::|::::::::::\\...........|.....................::|||\
                      //|\....__..........___________________//+.++..+...|:::||   \      ///   +________    \\+   ___.....\\\\.....................///::::::::::::::::\\\......................://::.::.__....//.....+_______   \\\      /|..||:::||:::::++:+\\__________________.............:::://\\
                     |+___+._________________________________  __+ ..::::|:::/|   +_______//     +__++              .......\\\....................//:::::::::::::::::::::\.....................//::::::..............  +___     \\________...||::::::::_. ___/ _______________________________________+
                     \____  _____ __                              ____::_::._/   /___     \      +____             .........\\.................../::::::::::::::::::::::::\\..................//:::::::..............  \_ _+     /     ___\...\_:::__:__\\                              ______________+
                                                                  //_:::::|      /..      \\                      ............\\\.............../:::.:::::::::::::::::::::::\...............://:::::::...............           //        \\     |:_::|/\|
                                                                  \\\\::::|     //.        \\                     ............\\\..__........_.///:.:::::::::::::::::::::::\\.__...._..._..://:::::::::...............          /          \     |:\\:////
                                                                   \\\:::.|    //          \\\                    .............:\_:_.::_::._:___:..:::::::::::::::::::::::::::__:::::::__::::::::::::::...............         //          \\    |.:\////
                                                                    \\\::.|    /            \\                    ...........:::::...::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::................       //            \|   |..||//
"""))


# -------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------
    

def angulo_entry_corridor(respuesta_angulo_entrada):
    #conversion del tipo del dato recibido en el input
    angulo = float(respuesta_angulo_entrada)
    angulo_ideal = -1.3

    while angulo != angulo_ideal:

        if angulo > -0.8:
            print("[bold red]ALERTA![/bold red] ÁNGULO DEMASIADO PLANO. La nave corre el riesgo de rebotar fuera de la atmósfera. Necesitas picar el morro un poco más hacia abajo (valores más negativos).")
            print()
        elif angulo < -2.0:
            print("[bold red]¡FALLO ESTRUCTURAL INMINENTE![/bold red] Las fuerzas G y el calor extremo han sobrecargado el escudo térmico. La nave no ha soportado la fricción. [italic]Prueba con un valor menos pronunciado.[/italic]")
            print()
        elif -1.4 <= angulo <= -1.2:
            # aunque el angulo sea optimo no es el mas seguro, por lo que le daremos al usaurio
            # una oportunidad de confirmacion o bien de cambio del angulo antes de la confirmacion final
            print("[bold yellow]¡ÁNGULO ÓPTIMO![/bold yellow] ............................... Estás en el rango de máxima precisión.")
            print()

            confirmacion = Prompt.ask("[bold cyan]> ¿Quieres confirmar este ángulo y continuar o prefieres buscar el punto exacto? (escribe 'confirmar' o 'probar')[/bold cyan]").strip().lower()

            if confirmacion == "confirmar":
                print("[yellow]Decisión aceptada. Bloqueando mandos y fijando trayectoria...[/yellow]")
                print()
                
                print("[bold red]⚠ ¡ADVERTENCIA DE ÚLTIMA HORA![/bold red] Las temperaturas del faldón térmico trasero han rozado el umbral crítico durante la compresión atmosférica...")
                print("[italic cyan]Los sistemas de refrigeración secundaria trabajan al 150% para compensar la desviación de décimas...[/italic cyan]")
                print("[green]✔ Estabilizando parámetros térmicos... Uf, por muy poco. ¡La nave ha resistido![/green]\n")
                print()

                comunicado_mcc_con_susto()
                # salimos de la funcion y devolvemos ANGULO que es el parametro que vamos a usar para el panel de control
                return angulo
            else: 
                print("[yellow]Continuamos con la búsqueda del punto exacto...[/yellow]")
                print()

        else:
            print("[bold cyan]TRAYECTORIA ESTABLE, PERO MEJORABLE.[/bold cyan] Estás dentro del pasillo seguro, pero los sistemas indican que el perfil aerodinámico no es el más eficiente")
            print()
        
        nuevo_valor = Prompt.ask("[bold green]> Introduce otro ángulo[/bold green]")
        angulo = float(nuevo_valor)

    print("[bold green]¡ÁNGULO IDEAL DE MÁXIMA PRECISIÓN CLAVADO![/bold green]")
    comunicado_mcc()

    return angulo 


# -------------------------------------------------------------------------------------------------------------------------------------

def monitorizacion_tiempo_real():
    #monitorizacion tiempo real 
    terminal = "\n> Accediendo al flujo de datos en directo del Sector 4..."
    print(Panel(terminal, title="[cyan]TERMINAL - TELEMETRÍA EN VIVO[/cyan]", border_style="cyan"))

    table = Table(title="Monitoreo Térmico - Sector 4 (Losetas de Sílice)")
    table.add_column("Segundo", justify="center")
    table.add_column("Temperatura (°C)", justify="right")
    table.add_column("Estado del Escudo", justify="center")

    #recarga cada segundo
    with Live(table, refresh_per_second=1):
        for segundo in range(1, 9):
            time.sleep(1)
            
            if segundo <= 3:
            #nominal 
                temperatura = random.uniform(1150.0, 1300.0)
                estado = "[green]NOMINAL[/green]"
            elif segundo <= 6:
                #advertencia
                temperatura = random.uniform(1310.0, 1440.0)
                estado = "[bold yellow]ADVERTENCIA[/bold yellow]"
            else:
                # critico
                temperatura = random.uniform(1455.0, 1550.0)
                estado = "[bold red]¡CRÍTICO![/bold red]"

            table.add_row(f"T+{segundo}s", f"{temperatura:,.1f} °C", estado)

    print("\n[bold cyan]Monitoreo completado.[/bold cyan] Has visto cómo la temperatura escala rápidamente hacia el peligro...")


# -----------------------------------------------------------------

def game_over():
    print(
        Panel(
            r"""
                                                                        _____                                                 _____                    
        _____           _____                ___________           _____\    \               ____    _______    ______   _____\    \ ___________       
   _____\    \_       /      |_             /           \         /    / |    |          ____\_  \__ \      |  |      | /    / |    |\          \      
  /     /|     |     /         \           /    _   _    \       /    /  /___/|         /     /     \ |     /  /     /|/    /  /___/| \    /\    \     
 /     / /____/|    |     /\    \         /    //   \\    \     |    |__ |___|/        /     /\      ||\    \  \    |/|    |__ |___|/  |   \_\    |    
|     | |_____|/    |    |  |    \       /    //     \\    \    |       \             |     |  |     |\ \    \ |    | |       \        |      ___/     
|     | |_________  |     \/      \     /     \\_____//     \   |     __/ __          |     |  |     | \|     \|    | |     __/ __     |      \  ____  
|\     \|\        \ |\      /\     \   /       \ ___ /       \  |\    \  /  \         |     | /     /|  |\         /| |\    \  /  \   /     /\ \/    \ 
| \_____\|    |\__/|| \_____\ \_____\ /________/|   |\________\ | \____\/    |        |\     \_____/ |  | \_______/ | | \____\/    | /_____/ |\______| 
| |     /____/| | ||| |     | |     ||        | |   | |        || |    |____/|        | \_____\   | /    \ |     | /  | |    |____/| |     | | |     | 
 \|_____|     |\|_|/ \|_____|\|_____||________|/     \|________| \|____|   | |         \ |    |___|/      \|_____|/    \|____|   | | |_____|/ \|_____| 
        |____/                                                         |___|/           \|____|                              |___|/                    
""",
            border_style="red",
        )
    )



# -----------------------------------------------------------------

def opcion1_exito():
    print("\n[bold green]✔ PURGA COMPLETADA CON ÉXITO[/bold green]")
    print("El nitrógeno líquido refrigera el sector 4 al instante. Trayectoria nominal y sistemas intactos.")
    print("[cyan]>>> Iniciando Fase 3: Descenso y Aterrizaje en condiciones óptimas...[/cyan]")


def opcion2_descenso_con_correccion():
    print("\n[bold yellow]⚠ MANIOBRA DE BALANCEO EJECUTADA[/bold yellow]")
    print("Logras disipar el calor extremo rotando el fuselaje, pero la maniobra aerodinámica te ha desviado 12 km de la ruta prevista.")
    print("[yellow]Los ordenadores de vuelo recalculan el descenso consumiendo combustible extra de reserva.[/yellow]")
    print("[cyan]>>> Iniciando Fase 3: Descenso con corrección de rumbo...[/cyan]")

def opcion3_modo_emergencia():
    print("\n[bold red]❌ ¡FALLO CATASTRÓFICO DEL ESCUDO TÉRMICO![/bold red]")
    print("Al mantener el rumbo sin purgar ni refrigerar, la temperatura en el sector 4 ha superado los [bold]1,650 °C[/bold].")
    print("Las losetas de sílice se han desintegrado por completo y el plasma supercaliente ha perforado el acero inoxidable del faldón estructural.")
    
    #contexto FIN DE PARTIDA
    game_over_texto = Text()
    game_over_texto.append("💀 MISIÓN FRACASADA // STARSHIP DESTRUIDA\n\n", style="bold white")
    game_over_texto.append("La telemetría se ha interrumpido de forma permanente. El MCC confirma la pérdida total de la nave tras desintegrarse en las capas altas de la atmósfera.\n\n", style="red")
    game_over_texto.append("Has subestimado la fricción atmosférica, comandante. Fin de la simulación.", style="italic yellow")
    
    print(Panel(game_over_texto, title="[red]GAME OVER[/red]", border_style="red", padding=(1, 2)))

    input("\n[ Presiona Enter para contemplar el destino de la Starship... ]")

    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    # funcion explosion
    explosion_starship.reproducir_gif_colores("./imgs/explosion.gif")

    input("\n[ Presiona Enter para ver el resumen de la misión... ]")

    # funcion game over
    game_over()


# -------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------
def consola_reajuste_sistemas(angulo):
    print("\n[bold cyan]🔧 CONSOLA DE REAJUSTE TÁCTICO[/bold cyan]")
    print("El tiempo se agota. Define la directriz de vuelo para la reentrada final:\n")

    while True:
        print(
            "[bold cyan]"
            "╔════════════════════════════════════════════════════════════════╗\n"
            "║             SELECCIONA LA ESTRATEGIA DE DESCENSO               ║\n"
            "╠════════════════════════════════════════════════════════════════╣\n"
            "║  [1] Estrategia Conservadora (Máxima protección y seguridad)   ║\n"
            "║  [2] Estrategia Agresiva (Descenso rápido / Alto riesgo)       ║\n"
            "║  [3] Estrategia Táctica (Protocolo estándar automatizado)      ║\n"
            "╚════════════════════════════════════════════════════════════════╝"
            "[/bold cyan]"
        )

        opcion_reajuste = Prompt.ask("\n[bold green]> Selecciona tu directriz (1, 2 o 3)[/bold green]").strip()

        if opcion_reajuste in ["1", "2", "3"]:
            break
        
        print("\n[red]❌ Opción no válida. Introduce 1, 2 o 3.[/red]\n")

    # Variables de estado según la estrategia
    temp_escudo = "980 °C (Estabilizado)"
    combustible = "84%"
    flaps = "Operativos (Activos)"

    match opcion_reajuste:
        case "1":
            print("\n[green]✔ Protocolo de seguridad activado.[/green] Los sistemas priorizan la amortiguación térmica.")
            temp_escudo = "[bold green]720 °C (Ultra seguro)[/bold green]"
            estrategia_final = "conservador"
        
        case "2":
            print("\n[yellow]⚠ ¡Modo agresivo seleccionado![/yellow] Los motores se inclinan al límite para ganar velocidad.")
            flaps = "[bold yellow]Forzados al 110%[/bold yellow]"
            estrategia_final = "agresivo"
        
        case "3":
            print("\n[cyan]✔ Protocolo estándar de la misión fijado.[/cyan] Dejando el control en manos de la IA de abordo.")
            estrategia_final = "equilibrado"

    print("\n[bold cyan]Actualizando telemetría de cabina...[/bold cyan]\n")

    # Dibujamos el panel actualizado
    tabla_actualizada = Table(show_header=False, box=None, padding=(0, 2))
    tabla_actualizada.add_column("Parametro", style="bold cyan")
    tabla_actualizada.add_column("Estado / Valor", style="bold white")

    tabla_actualizada.add_row("Ángulo de Reentrada:", f"{angulo}° (Fijado)")
    tabla_actualizada.add_row("Temperatura Escudo:", temp_escudo)
    tabla_actualizada.add_row("Integridad Losetas:", "[green]100% - Óptimo[/green]")
    tabla_actualizada.add_row("Combustible (Propelente):", combustible)
    tabla_actualizada.add_row("Sistemas de Vuelo:", "[green]NOMINALES[/green]")
    tabla_actualizada.add_row("Alerones (Flaps):", flaps)

    print(Panel(
        tabla_actualizada,
        title="[bold green]STARSHIP // TELEMETRÍA ACTUALIZADA[/bold green]",
        subtitle="[italic]Listo para Fase 3: Descenso[/italic]",
        border_style="green",
        padding=(1, 2)
    ))

    # Devolvemos el tipo de estrategia para usarla en el final del juego
    return estrategia_final


def confirmacion_comienzo_fase_descenso(angulo):
    evaluacion_panel = Prompt.ask(
        "[bold cyan]> ¿Consideras que los valores del panel de control son seguros para iniciar la Fase de Descenso? (escribe 'si' o 'no')[/bold cyan]"
    ).strip().lower()

    if evaluacion_panel in ["si", "sí", "s"]:
        print("\n[bold green]✔ ¡Orden de descenso autorizada![/bold green] Los motores se reorientan y la nave adopta la actitud de caída controlada.")
        print("[cyan]>>> Transicionando a la Fase 3: Descenso y Maniobra de Flip de aterrizaje...[/cyan]\n")
        # Aquí llamarías a tu función de la Fase 3:
        # fase_3_descenso()
        
    elif evaluacion_panel in ["no", "n"]:
        print("\n[bold yellow]⚠ Has decidido abortar temporalmente el descenso por precaución.[/bold yellow]")
        print("Los ingenieros en tierra revisan los sistemas de nuevo, pero el tiempo se agota y la atmósfera sigue comprimiéndose...")
        
        reintento = Prompt.ask("[bold green]> ¿Quieres forzar el descenso ahora o intentar un reajuste de emergencia? (forzar / reajustar)[/bold green]").strip().lower()
        if reintento == "forzar":
            print("\n[yellow]⚠ Descenso forzado autorizado. Los sistemas trabajan al límite.[/yellow]")
            input("\n[ Presiona Enter para iniciar el aterrizaje... ]")

            final_agresivo()

        else:
            print("\n[yellow]Reajustando estabilizadores de última hora. La tensión en cabina es máxima...[/yellow]")

            estrategia = consola_reajuste_sistemas(angulo)
            input("\n[ Presiona Enter para iniciar finalmente la Fase de Descenso... ]")
            
            # Redirigimos al final correspondiente según lo que haya votado en la consola
            if estrategia == "conservador":
                final_conservador()
            elif estrategia == "agresivo":
                final_agresivo()
            elif estrategia == "equilibrado":
                final_tactico()

         
            
    else:
        print("\n[italic]Respuesta no reconocida. Los ordenadores de vuelo interpretan silencio operativo y continúan el descenso automáticamente por protocolo de seguridad.[/italic]")
        input("[ Presiona Enter para finalizar la secuencia... ]")
        final_tactico()
    

# -------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------
def final_conservador():
    texto_fin = Text()
    texto_fin.append("🌟 ¡ATERRIZAJE PERFECTO Y NOMINAL!\n\n", style="bold green")
    texto_fin.append("Gracias a la purga criogénica y el exceso de precaución, el escudo térmico ha permanecido intacto. La maniobra de 'flip and burn' se ejecuta con una precisión milimétrica.\n\n", style="white")
    texto_fin.append("La Starship posa sus patas sobre la plataforma de aterrizaje levantando una suave nube de polvo marciano/terrestre.\n", style="white")
    texto_fin.append("MCC (Control de Misión): '¡Lo habéis conseguido, muchachos! Una clase magistral de pilotaje espacial.'", style="italic cyan")

    print(Panel(texto_fin, title="[green]MISIÓN CUMPLIDA // ÉXITO TOTAL[/green]", border_style="green", padding=(1, 2)))


def final_agresivo():
    texto_fin = Text()
    texto_fin.append("⚡ ¡DESCENSO AL LÍMITE DE LA FÍSICA!\n\n", style="bold yellow")
    texto_fin.append("La Starship ha bajado como un meteorito ardiente. Los deflectores rugían bajo una fricción brutal y el casco crujía al límite de su resistencia estructural.\n\n", style="white")
    texto_fin.append("En el último segundo, los motores Raptor rugen con potencia máxima en un encendido salvaje que frena la mole de acero contra todo pronóstico.\n\n", style="white")
    texto_fin.append("MCC (Control de Misión): '¡Increíble! Ha estado a punto de desintegrarse, comandante, ¡pero ha colado la maniobra más arriesgada de la historia del programa!'", style="italic yellow")

    print(Panel(texto_fin, title="[yellow]MISIÓN CUMPLIDA // VICTORIA AGÓNICA[/yellow]", border_style="yellow", padding=(1, 2)))


def final_tactico():
    texto_fin = Text()
    texto_fin.append("🎯 ATERRIZAJE TÁCTICO COMPLETADO\n\n", style="bold cyan")
    texto_fin.append("Confiando en los algoritmos de vuelo automatizados y los parámetros calculados por tierra, la nave describe una parábola perfecta sobre el cielo.\n\n", style="white")
    texto_fin.append("El encendido de aterrizaje se activa de forma automática, amortiguando el descenso de manera impecable y segura en el centro exacto de la zona designada.\n\n", style="white")
    texto_fin.append("MCC (Control de Misión): 'Telemetría perfecta. Protocolo completado con éxito. Bienvenidos a casa, equipo.'", style="italic green")

    print(Panel(texto_fin, title="[cyan]MISIÓN CUMPLIDA // PROTOCOLO ESTÁNDAR[/cyan]", border_style="cyan", padding=(1, 2)))
# -------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------

def mostrar_panel_telemetria(angulo):
    # Creamos una tabla interna para los datos clave de la nave
    tabla_datos = Table(show_header=False, box=None, padding=(0, 2))
    tabla_datos.add_column("Parametro", style="bold cyan")
    tabla_datos.add_column("Estado / Valor", style="bold white")

    # Añadimos los datos de la misión (puedes pasarle el ángulo con el que entró)
    tabla_datos.add_row("Ángulo de Reentrada:", f"{angulo}° (Fijado)")
    tabla_datos.add_row("Temperatura Escudo:", "980 °C (Estabilizado)")
    tabla_datos.add_row("Integridad Losetas:", "[green]100% - Óptimo[/green]")
    tabla_datos.add_row("Combustible (Propelente):", "84%")
    tabla_datos.add_row("Sistemas de Vuelo:", "[green]NOMINALES[/green]")
    tabla_datos.add_row("Alerones (Flaps):", "Operativos (Activos)")

    # Envolvemos la tabla dentro de un Panel con estilo de cabina
    panel_cabina = Panel(
        tabla_datos,
        title="[bold green]STARSHIP // TELEMETRÍA DE DESCENSO[/bold green]",
        subtitle="[italic]Fase 3: Maniobra de frenado atmosférico y aterrizaje[/italic]",
        border_style="green",
        padding=(1, 2)
    )

    print(panel_cabina)


# -----------------------------------------------------------------


def obtener_panel():
    return r"""
+------------------------------+------------------------------+------------------------------+
| O D I S E A                  | SISTEMAS DE REENTRADA        | MET  002:42:18               |
| CONTROL ORBITAL / OV-07      | CANAL 04  ::  TELEMETRIA     | ENLACE [|||||||||.] ESTABLE  |
+------------------------------+------------------------------+------------------------------+
|       VECTOR DE VUELO        |       HORIZONTE / IMU        |        ESCUDO TERMICO        |
|                              |                              | STARSHIP / VISTA VENTRAL     |
|          .--------.          |          .--------.          |              /\              |
|       .-'  .  |  . '-.       |       .-'    |     '-.       |             /..\             |
|      / .      |     . \      |      /       |        \      |            /::::\            |
|     /    .----+--.     \     |     /  -  -  +  -  -   \     |           /::##::\           |
|    |    /  *  |   \    |     |    |         |          |    |          /::####::\          |
|  --+---|------O----|---+--   |  --+=========O==========+--  |       __/:::####:::\__       |
|    |    \     |  /     |     |    | ~ ~ ~ ~ | ~ ~ ~ ~  |    |      /:/|:::####:::|\:\      |
|     \    '----+>'     /      |     \ ~ ~ ~ | ~ ~ ~ ~ /      |     /:/ |:::####:::| \:\     |
|      \ .      |    . /       |      \ ~ ~ ~|~ ~ ~ ~ /       |     '-' |:::####:::| '-'     |
|       '-._____|__.-'         |       '-.____|___.-'         |         |:::####:::|         |
|                              |                              |         |:::####:::|         |
| AZIMUT  128.4   INC  -06.2   | CABECEO -06.2  ALABEO +01.4  |         |:::####:::|         |
| VECTOR  >>> CORREDOR NOMINAL | ALTITUD 068.4 km  MACH 24.8  |         |:::####:::|         |
+------------------------------+------------------------------+------------------------------+
| TRAYECTORIA / DESCENSO       | PROPELENTE / RCS             |        /|:::####:::|\        |
|                              |                              |       /:|:::####:::|:\       |
| 100 + * .                    | LH2  [########......]  64.0% |      /::|::::##::::|::\      |
|     |     * .                | LOX  [#########.....]  71.2% |     /:::|::::::::::|:::\     |
|  60 +         * > .          | RCS  [###########...]  82.6% |    /____|__________|____\    |
|     |               . .      |                              |          \_O_O_O_/           |
|  20 +                    .   | PRESION   24.8 bar           | INTEGRIDAD [#########.] 96%  |
|     +--------------------    | CAUDAL    00.0 kg/s          | LOSETAS 1280 C  /  NOMINAL   |
|      0   DISTANCIA   800 km  | RESERVA   0842 kg            |                              |
+------------------------------+------------------------------+------------------------------+
| BUS A [OK]   BUS B [OK]      | O2  98%   CO2  0.04%         | CASCO  101.3 kPa  /  21.6 C  |
| POTENCIA  28.4 V / 16.2 A    | SOPORTE VITAL  ::  NOMINAL   | BALIZA  *  PORTADORA FIJA    |
+------------------------------+------------------------------+------------------------------+
    """.strip("\n")

# -----------------------------------------------------------------


#le pasamos el parametro angulo que usaremos en la siguiente fase de mostrar un panel de control
def monitorear_escudo_termico(angulo):
    #aqui tenemos nuestro ascii de losetas termicas
    starship_losetas_termicas_ascii()

    intro_escudo = Text()
    intro_escudo.append("🔥 FASE: MONITOREO DEL ESCUDO TÉRMICO\n\n", style="bold red")
    intro_escudo.append("La Starship se adentra en las capas densas de la atmósfera. El plasma incandescente rodea la nave.\n", style="white")
    intro_escudo.append("Temperatura actual del faldón sotavento: ", style="white")
    intro_escudo.append("1,100 °C", style="bold yellow")
    intro_escudo.append("\n\nLos sensores de las losetas térmicas hexagonales empiezan a sufrir estrés térmico.", style="white")
    
    print(Panel(intro_escudo, title="[red]TELEMETRÍA TÉRMICA[/red]", border_style="red", padding=(1, 2)))

    #menu opciones
    print("\n[bold]¡ALERTA DE TELEMETRÍA![/bold] El sector 4 de losetas térmicas reporta un incremento de temperatura acelerado.")
    print("[1] Activar purga de refrigerante de emergencia en el sector 4")
    print("[2] Realizar un ligero balanceo (roll) para disipar calor en otra sección")
    print("[3] Mantener rumbo actual y confiar en la integridad estructural de las losetas")
    print("[4] MONITORIZACION TERMICA antes de decidir")

    eleccion = Prompt.ask("[bold green]> Selecciona una opción (1, 2, 3 o 4)[/bold green]").strip()


    if eleccion == "1":
        print("\n[green]✔ ¡Purgando refrigerante![/green] Las temperaturas descienden de inmediato a 980 °C. El escudo térmico se estabiliza con éxito.")
        print("[bold green]¡Has salvado las losetas del sector 4 de una fusión parcial![/bold green]")
        opcion1_exito()
        mostrar_panel_telemetria(angulo)
        #imprimimos el panel de control, ya que el panel es lo que nos lo devuelve en el return, pero no nos lo imprime
        print(obtener_panel())
        print()

        confirmacion_comienzo_fase_descenso(angulo)



    elif eleccion == "2":
        print("\n[yellow]⚠ Maniobra de balanceo ejecutada.[/yellow] El calor se redistribuye, pero la nave sufre un ápice de inestabilidad aerodinámica momentánea.")
        print("[yellow]El escudo aguanta, aunque los ingenieros en tierra han sufrido un microinfarto.[/yellow]")
        opcion2_descenso_con_correccion()

    elif eleccion == "3":
        print("\n[bold red]❌ ¡ERROR CRÍTICO![/bold red] Sin intervención, la temperatura superó el límite de las losetas de sílice.")
        print("[red]Se ha desprendido un segmento del escudo térmico en el sector 4. Daños estructurales leves en el faldón.[/red]")
        opcion3_modo_emergencia()

    elif eleccion == "4":
        #llamada funcion monitoreo en tiempo real
        monitorizacion_tiempo_real()

       
        decision_final = Prompt.ask("[bold green]> ¿Qué acción tomas ahora? (1: Purgar / 2: Balanceo / 3: Mantener rumbo / 4: MONITORIZACIO)[/bold green]").strip()
        
        if decision_final == "1":
            print("\n[green]✔ ¡Purgando refrigerante a tiempo![/green] Los datos en vivo te alertaron del pico crítico. Las temperaturas bajan y salvas la nave.")
        elif decision_final == "2":
            print("\n[yellow]⚠ Balanceo ejecutado tras el análisis.[/yellow] Maniobra ajustada con éxito.")
        elif decision_final == "3":
                print("\n[bold red]❌ ¡ERROR CRÍTICO! ❌[/bold red] Sin intervención, la temperatura superó el límite de las losetas de sílice")
                opcion3_modo_emergencia()
        else:
            print("\n[bold red]❌ Ignoraste los datos críticos.[/bold red] El sector 4 ha sufrido daños importantes por el calor extremo.")
    else:
        print("\n[italic]Opción no válida. La indecisión ha costado valiosos segundos, pero los sistemas automatizados han tomado el control a última hora.[/italic]")



