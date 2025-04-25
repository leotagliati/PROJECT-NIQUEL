from machine import Pin, I2C
import ssd1306
from icones import heart, sword,skull
from display_utils import printIcon, buildIcon
import time
import random
      
# Configura I2C no barramento 0 (com GP4 = SDA e GP5 = SCL)
# LEMBRAR: Preciso fazer isso para cada Display OLED
i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)

# Configura o botão
botao = Pin(1, Pin.IN, Pin.PULL_UP)  # Botão conectado ao pino GP2

# Cria objeto do display OLED 128x32
display = ssd1306.SSD1306_I2C(128, 32, i2c)

# -------- TESTE DE ICONE --------
# icon = heart

# display.fill(0)


# rowLenght = len(icon[0])
# i = 1
# for row in icon:
#     if len(row) != rowLenght:
#         print("Erro: Linhas do icone tem tamanhos diferentes!")
#         print("Tamanho esperado por linha: " + str(rowLenght))
#         print("Tamanho encontrado na linha " + str(i) + ": " + str(len(row)))
#         break
#     i += 1
# else:
#    
#     rows = len(icon)
#     columns = rowLenght
#     iconToPrint = buildIcon(icon)

#     x0, y0 = (64-(16)), 0 
#     display.fill(0)  

#     printIcon(display, iconToPrint, x0,y0)
#     display.show()
# -------------------------------------------


# Ícones disponíveis
icon_map = {
    "heart": heart,
    "sword": sword,
    "skull": skull
}

iconNames = list(icon_map.keys())
icons = list(icon_map.values())


# LEMBRAR: Preciso fazer isso para cada Display OLED
def draw_single_reel(display, icon_list):
    display.fill(0)
    x_offsets = [0, 48, 96]  

    for i, icon in enumerate(icon_list[:3]):
        icon_rotated = buildIcon(icon)  
        x = x_offsets[i]
        y = 0
        printIcon(display, icon_rotated, x, y)

    display.show()

def spin_reel(duration_ms=2000, speed_ms=0):
    start = time.ticks_ms()
    current_icons = icons[:]

    while time.ticks_diff(time.ticks_ms(), start) < duration_ms:
        draw_single_reel(display, current_icons)
        if speed_ms > 0:
            time.sleep_ms(speed_ms)  # só dorme se for maior que 0
        current_icons = current_icons[1:] + current_icons[:1]

    return current_icons[:3]

while True:
    if botao.value() == 0:
        tempo_de_espera = random.randint(2000, 7000)
        resultado = spin_reel(tempo_de_espera, 0)  # roda por 3 segundos, depois para

        resultado_nomes = [iconNames[icons.index(icon)] for icon in resultado]

        print("Ícones finais:", resultado_nomes)

        if resultado_nomes[0] == "heart":
            print("🎉 Você ganhou com um coração no meio!")
        else:
            print("😢 Tente novamente...")

        time.sleep(0.5)