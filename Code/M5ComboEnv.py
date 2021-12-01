from m5stack import *
from m5ui import *
from uiflow import *
import time

setScreenColor(0xffc801)


temp = None
humi = None
ext_temp = None


image0 = M5Img(0, 0, "res/m5easter.jpg", True)
label0 = M5TextBox(35, 143, "Indoor Temp:", lcd.FONT_DejaVu18, 0xf00f0f, rotate=0)
label2 = M5TextBox(35, 199, "Outdoor Temp:", lcd.FONT_DejaVu18, 0xf00f0f, rotate=0)
label3 = M5TextBox(35, 170, "Humidity:", lcd.FONT_DejaVu18, 0xf00f0f, rotate=0)
hum = M5TextBox(195, 170, ".", lcd.FONT_DejaVu18, 0xf00f0f, rotate=0)
indoor = M5TextBox(195, 143, ".", lcd.FONT_DejaVu18, 0xf00f0f, rotate=0)
outdoor = M5TextBox(195, 199, ".", lcd.FONT_DejaVu18, 0xf00f0f, rotate=0)
label4 = M5TextBox(55, 2, "Happy M5mas", lcd.FONT_DejaVu24, 0xe34a1a, rotate=0)
label1 = M5TextBox(45, 0, "Happy Halloween", lcd.FONT_DejaVu24, 0xe3c31a, rotate=0)



def buttonA_wasPressed():
  global temp, humi, ext_temp
  lcd.clear()
  setScreenColor(0xffffff)
  label4.setColor(0xff0000)
  image0.setPosition(0, 0)
  image0.changeImg("res/m5babbo.jpg")
  label4.hide()
  label0.show()
  label2.show()
  label3.show()
  label4.setPosition(x=55)
  label4.setText('Happy M5mas')
  label4.show()
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  global temp, humi, ext_temp
  lcd.clear()
  setScreenColor(0x33ccff)
  label4.hide()
  label4.setText('              ')
  label4.setColor(0xff0000)
  setScreenColor(0xffffff)
  image0.setPosition(0, 0)
  image0.changeImg("res/m5easter.jpg")
  label4.hide()
  label0.show()
  label2.show()
  label3.show()
  label4.hide()
  label4.setPosition(x=90)
  label4.setText('Happy Easter')
  label4.show()
  pass
btnB.wasPressed(buttonB_wasPressed)

def buttonC_wasPressed():
  global temp, humi, ext_temp
  lcd.clear()
  setScreenColor(0xffcc00)
  label1.setColor(0xffcc00)
  label4.hide()
  image0.changeImg("res/hallowm5_b.jpg")
  image0.setPosition(0, 0)
  label1.hide()
  label0.show()
  label2.show()
  label3.show()
  label1.setText('Happy Halloween')
  label1.show()
  pass
btnC.wasPressed(buttonC_wasPressed)


lcd.clear()
from machine import Pin
from esp import dht_readinto

DHT_PIN = 22

def readHumidity():
  buf = bytearray(5)
  try:
    dht_readinto(Pin(DHT_PIN), buf)
  except:
    pass
  return(buf[0] + buf[1]*0.1)

def readTemperature():
  buf = bytearray(5)
  try:
    dht_readinto(Pin(DHT_PIN), buf)
  except:
    pass
  return(buf[2] + buf[3]*0.1)
from machine import Pin
import _onewire

def init(pin):
  Pin(pin, Pin.OPEN_DRAIN, Pin.PULL_UP)

def convert(pin):
  _onewire.reset(Pin(pin))
  _onewire.writebyte(Pin(pin), 0xcc)
  _onewire.writebyte(Pin(pin), 0x44)

def read(pin):
  _onewire.reset(Pin(pin))
  _onewire.writebyte(Pin(pin), 0xcc)
  _onewire.writebyte(Pin(pin), 0xbe)
  tlo = _onewire.readbyte(Pin(pin))
  thi = _onewire.readbyte(Pin(pin))
  _onewire.reset(Pin(pin))
  temp = tlo + thi * 256
  if temp > 32767:
    temp = temp - 65536
  temp = temp * 0.0625
  return(temp)

init(21)

setScreenColor(0xffcc00)
image0.changeImg("res/hallowm5_b.jpg")
label4.show()
label1.hide()
label0.show()
label2.show()
label3.show()
while True:
  temp = (str(("%.1f"%((readTemperature())))) + str(' C'))
  humi = (str(("%.1f"%((readHumidity())))) + str(' %'))
  convert(21)
  wait_ms(1000)
  ext_temp = (str(("%.1f"%((read(21))))) + str(' C'))
  indoor.setText('              ')
  hum.setText('      ')
  outdoor.setText('      ')
  indoor.setText(str(temp))
  hum.setText(str(humi))
  outdoor.setText(str(ext_temp))
  wait_ms(1000)
  wait_ms(2)
