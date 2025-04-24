from machine import Pin, I2C
import ssd1306
from icones import heart, sword
from display_utils import printIcon, buildIcon


      
      
# Configura I2C no barramento 0 (com GP4 = SDA e GP5 = SCL)
i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)

# Cria objeto do display OLED 128x32
display = ssd1306.SSD1306_I2C(128, 32, i2c)

icon = heart

display.fill(0)


rowLenght = len(icon[0])
i = 1
for row in icon:
    if len(row) != rowLenght:
        print("Erro: Linhas do icone tem tamanhos diferentes!")
        print("Tamanho esperado por linha: " + str(rowLenght))
        print("Tamanho encontrado na linha " + str(i) + ": " + str(len(row)))
        break
    i += 1
else:
    # Se tudo estiver correto, realiza a rotação do ícone
    rows = len(icon)
    columns = rowLenght
    iconToPrint = buildIcon(icon)

    x0, y0 = (64-(16)), 0  # ajusta posição na tela
    display.fill(0)  # Limpa a tela antes de desenhar

    printIcon(display, iconToPrint, x0,y0)
    display.show()
