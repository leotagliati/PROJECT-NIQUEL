from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from icones import heart, sword,skull
from display_utils import printIcon, buildIcon
import time
import random
      
# Configura I2C no barramento 0 (com GP4 = SDA e GP5 = SCK)
# LEMBRAR: Preciso fazer isso para cada Display OLED
i2c_0 = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
print("i2c_0:", i2c_0.scan())

# Estamos com um problema, como utilizar 2 displays OLED sendo que ambos possuem o mesmo endereço?

# i2c_1 = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)  # Barramento 1 (com GP10 = SDA e GP11 = SCK)
# print("i2c_1:", i2c_1.scan())

# Configura o botão
# botao = Pin(2, Pin.IN, Pin.PULL_UP)  # Botão conectado ao pino GP2

# # Cria objeto do display OLED 128x32
display_1 = SSD1306_I2C(128, 32, i2c_0)
# # display_2 = SSD1306_I2C(128, 32, i2c_1)

# # Configura buzzer na porta GP15
# buzzer = Pin(15, Pin.OUT)
# ledVitoria = Pin(16, Pin.OUT)  # LED de vitória na porta GP26
# ledDerrota = Pin(17, Pin.OUT)  # LED de derrota na porta GP27

# # Liga o buzzer por 1 segundo

# # -------- TESTE DE ICONE --------
# # icon = heart

# # display.fill(0)


# # rowLenght = len(icon[0])
# # i = 1
# # for row in icon:
# #     if len(row) != rowLenght:
# #         print("Erro: Linhas do icone tem tamanhos diferentes!")
# #         print("Tamanho esperado por linha: " + str(rowLenght))
# #         print("Tamanho encontrado na linha " + str(i) + ": " + str(len(row)))
# #         break
# #     i += 1
# # else:
# #    
# #     rows = len(icon)
# #     columns = rowLenght
# #     iconToPrint = buildIcon(icon)

# #     x0, y0 = (64-(16)), 0 
# #     display.fill(0)  

# #     printIcon(display, iconToPrint, x0,y0)
# #     display.show()
# # -------------------------------------------


# # Ícones disponíveis
# icon_map = {
#     "heart": heart,
#     "sword": sword,
#     "skull": skull
# }

# iconNames = list(icon_map.keys())
# icons = list(icon_map.values())


# # LEMBRAR: Preciso fazer isso para cada Display OLED
# def draw_single_reel(display, icon_list):
#     display.fill(0)
#     x_offsets = [0, 48, 96]  

#     for i, icon in enumerate(icon_list[:3]):
#         icon_rotated = buildIcon(icon)  
#         x = x_offsets[i]
#         y = 0
#         printIcon(display, icon_rotated, x, y)

#     display.show()

# def spin_reel(display ,duration_ms=2000, speed_ms=0):
#     start = time.ticks_ms()
#     current_icons = icons[:]

#     while time.ticks_diff(time.ticks_ms(), start) < duration_ms:
#         draw_single_reel(display, current_icons)
#         if speed_ms > 0:
#             time.sleep_ms(speed_ms)  # só dorme se for maior que 0
#         current_icons = current_icons[1:] + current_icons[:1]

#     return current_icons[:3]


# draw_single_reel(display_1, icons)  # Desenha os ícones iniciais
# # draw_single_reel(display_2, icons)  # Desenha os ícones iniciais
# # ledDerrota.value(0)
# # ledVitoria.value(0)

# while True:
#     if botao.value() == 0:
#         # ledVitoria.value(0)
#         # ledDerrota.value(0)
        
#         tempo_de_espera = random.randint(2000, 7000)
#         resultado1 = spin_reel(display_1,tempo_de_espera, 0)  # roda por 3 segundos, depois para
#         # resultado2 = spin_reel(display_2,tempo_de_espera, 0)  # roda por 3 segundos, depois para

#         resultado_nomes1 = [iconNames[icons.index(icon)] for icon in resultado1]
#         # resultado_nomes2 = [iconNames[icons.index(icon)] for icon in resultado2]

#         # print("Ícones finais:", resultado_nomes1)

#         # if resultado_nomes1[0] == "heart" and resultado_nomes2[0] == "heart": 
#         if resultado_nomes1[0] == "heart" :
#         # if resultado_nomes2[0] == "heart" :
#             print("Ganhou!")
#             # ledVitoria.value(1)
#             # buzzer.value(1)
#             # time.sleep(0.3)
#             # buzzer.value(0)
#             # time.sleep(0.1)
#             # buzzer.value(1)
#             # time.sleep(0.6)
#             # buzzer.value(0)
#             # time.sleep(0.6)
#             # time.sleep(2)
#             # ledVitoria.value(0)
#         else:
#             print("Tente novamente...")
#             # ledDerrota.value(1)
#             # buzzer.value(1)
#             # time.sleep(0.1)
#             # buzzer.value(0)
#             # time.sleep(0.1)
#             # buzzer.value(1)
#             # time.sleep(0.1)
#             # buzzer.value(0)
#             # time.sleep(2)
#             # ledDerrota.value(0)
#         time.sleep(0.5)