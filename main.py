from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf, sys
import utime

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

def main():
    i2c_dev = init_i2c(scl_pin=27, sda_pin=26, barramento=1)
    oled = SSD1306_I2C(pix_res_x, pix_res_y, i2c_dev)
    oled.text("Hello World!", 0, 0)
    oled.show()
    
    i2c_2dev = init_i2c(scl_pin=1, sda_pin=0,barramento=0)
    oled_2 = SSD1306_I2C(pix_res_x, pix_res_y, i2c_2dev)
    oled_2.text("Hello World!", 0, 0)
    oled_2.show()

if __name__ == '__main__':
    main()
