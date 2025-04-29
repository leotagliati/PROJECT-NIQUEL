from display_utils import printIcon, buildIcon
import time
import uasyncio as asyncio
import random

def init_reel(display, icon_list):
    display.fill(0)
    x_offsets = [0, 48, 96]  

    # Embaralhamento manual (Fisher-Yates)
    icons_copy = icon_list[:]  # Copia da lista original
    for i in range(len(icons_copy) - 1, 0, -1):
        j = random.randint(0, i)
        icons_copy[i], icons_copy[j] = icons_copy[j], icons_copy[i]

    random_icons = icons_copy[:3]  # Seleciona os 3 primeiros (sem repetição)F

    for i, icon in enumerate(random_icons[:3]):
        icon_rotated = buildIcon(icon)  
        x = x_offsets[i]
        y = 0
        printIcon(display, icon_rotated, x, y)

    display.show()
    return random_icons[:3]  # Retorna os ícones selecionados

def draw_single_reel(display, icon_list):
    display.fill(0)
    x_offsets = [0, 48, 96]  

    for i, icon in enumerate(icon_list[:3]):
        icon_rotated = buildIcon(icon)  
        x = x_offsets[i]
        y = 0
        printIcon(display, icon_rotated, x, y)

    display.show()

async def spin_reel_async(display, icons, duration_ms=2000, speed_ms=100):
    start = time.ticks_ms()
    current_icons = icons[:]

    while time.ticks_diff(time.ticks_ms(), start) < duration_ms:
        draw_single_reel(display, current_icons)
        await asyncio.sleep_ms(speed_ms if speed_ms > 0 else 50)
        current_icons = current_icons[1:] + current_icons[:1]
    print("Spin ended")
    return current_icons[:3]