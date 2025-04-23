from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import random
import time


botao = Pin(16, Pin.IN, Pin.PULL_DOWN)

# Configura I2C e OLED
i2c = I2C(0, scl=Pin(1), sda=Pin(0))
oled = SSD1306_I2C(128, 64, i2c)

# Lista de "símbolos"
simbolos = ["🍒", "🔔", "💎", "⭐", "7️⃣", "🍋"]

def gira_caça_niquel():
    # Limpa tela
    oled.fill(0)

    # Sorteia 3 símbolos aleatórios
    rolos = [random.choice(simbolos) for _ in range(3)]

    # Exibe no OLED
    texto = " ".join(rolos)
    oled.text("GIRANDO...", 10, 10)
    oled.show()
    time.sleep(0.5)

    oled.fill(0)
    oled.text("Resultado:", 0, 10)
    oled.text(texto, 0, 30)
    oled.show()

print("Caça-níquel pronto! Pressione o botão...")

while True:
    if botao.value():
        gira_caça_niquel()
        time.sleep(0.5)  # debounce simples