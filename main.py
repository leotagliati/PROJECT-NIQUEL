from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf, sys
import utime
from icones import heart, sword,skull
from display_utils import printIcon, buildIcon
from reel_utils import draw_single_reel, spin_reel_async, init_reel
import time
import random
import uasyncio as asyncio

pix_res_x = 128
pix_res_y = 32

def init_i2c(scl_pin, sda_pin,barramento):
    # Initialize I2C device
    i2c = I2C(barramento, scl=Pin(scl_pin), sda=Pin(sda_pin), freq=200000)
    i2c_addr = [hex(ii) for ii in i2c.scan()]
    
    if not i2c_addr:
        print('No I2C Display Found')
        sys.exit()
    else:
        print("I2C Address      : {}".format(i2c_addr[0]))
        print("I2C Configuration: {}".format(i2c))
    
    return i2c

# Ícones disponíveis
icon_map = {
    "heart": heart,
    "sword": sword,
    "skull": skull
}

iconNames = list(icon_map.keys())
icons = list(icon_map.values())

async def main():
    i2c_dev = init_i2c(scl_pin=27, sda_pin=26, barramento=1)
    i2c_2dev = init_i2c(scl_pin=1, sda_pin=0,barramento=0)
    
    oled = SSD1306_I2C(pix_res_x, pix_res_y, i2c_dev)
    oled_2 = SSD1306_I2C(pix_res_x, pix_res_y, i2c_2dev)
    
    iconsChosen_1 = init_reel(oled, icons)
    iconsChosen_2 = init_reel(oled_2, icons)
    
    
    start_spin_button = Pin(15, Pin.IN, Pin.PULL_UP)
    victory_led = Pin(16, Pin.OUT)
    victory_led.value(0)
    
    defeat_led = Pin(17, Pin.OUT)
    defeat_led.value(0)
        
    buzzer = Pin(14, Pin.OUT)
    
    result_1 = None
    result_2 = None
    while True:
        if start_spin_button.value() == 0:
            print("Button Pressed")
            
            result_1, result_2 = await asyncio.gather(
            spin_reel_async(oled, iconsChosen_1, duration_ms=random.randint(5000, 10000), speed_ms=100),
            spin_reel_async(oled_2, iconsChosen_2, duration_ms=random.randint(5000, 10000), speed_ms=100)
            )

            print("Spinning Reels Ended")
            
            if(result_1[0] == result_2[0]):
                print("You Win!")
                victory_led.value(1)
                buzzer.value(1)
                await asyncio.sleep(0.3)
                buzzer.value(0)
                await asyncio.sleep(0.1)
                buzzer.value(1)
                await asyncio.sleep(0.6)
                buzzer.value(0)
                victory_led.value(0)
                await asyncio.sleep(0.6)
                
            else:
                print("Try Again...")
                defeat_led.value(1)
                buzzer.value(1)
                await asyncio.sleep(0.1)
                buzzer.value(0)
                await asyncio.sleep(0.6)
                defeat_led.value(0)
                await asyncio.sleep(0.6)
            
            
if __name__ == '__main__':
    loop = asyncio.get_event_loop()  
    loop.create_task(main())  # Create a task to run the main function
    loop.run_forever()  # Run the event loop indefinitely
