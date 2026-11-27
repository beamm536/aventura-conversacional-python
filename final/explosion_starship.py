import os
import time
from PIL import Image

ASCII_CHARS = [" ", ".", "*", "+", "o", "O", "8", "#", "@", "█"]

def transformar_frame_a_ascii_con_color(image, nuevo_ancho=80):
    ancho_original, alto_original = image.size
    proporcion = alto_original / ancho_original / 1.65
    nuevo_alto = int(nuevo_ancho * proporcion)
    
    imagen_redimensionada = image.resize((nuevo_ancho, nuevo_alto)).convert("RGB")
    pixels = list(imagen_redimensionada.getdata())
    
    lineas_coloreadas = []
    for y in range(nuevo_alto):
        linea_actual = ""
        for x in range(nuevo_ancho):
            r, g, b = pixels[y * nuevo_ancho + x]
            r = min(255, int(r * 2.8))
            g = min(255, int(g * 2.8))
            b = min(255, int(b * 2.8))
            brillo = (r + g + b) // 3
            
            if brillo < 15:
                linea_actual += " "
                continue
                
            caracter = ASCII_CHARS[brillo * len(ASCII_CHARS) // 256]
            color_ansi = f"\033[38;2;{r};{g};{b}m"
            reset_ansi = "\033[0m"
            linea_actual += f"{color_ansi}{caracter}{reset_ansi}"
            
        lineas_coloreadas.append(linea_actual)
    return "\n".join(lineas_coloreadas)

def reproducir_gif_colores(ruta_gif):
    try:
        with Image.open(ruta_gif) as im:
            for frame_index in range(im.n_frames):
                im.seek(frame_index)
                frame_ascii = transformar_frame_a_ascii_con_color(im, nuevo_ancho=80)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(frame_ascii)
                time.sleep(0.07)
    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta_gif}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# --- PROTECCIÓN PARA QUE NO SE EJECUTE AL IMPORTAR ---
if __name__ == "__main__":
    print("¡La Starship entra en caída libre!")
    input("Pulsa Enter para ver la explosión...")
    reproducir_gif_colores("./imgs/explosion.gif")
    print("\n¡La nave se ha desintegrado por completo!")