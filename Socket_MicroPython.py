"""
Thiago S. 01/02/21
versão utilizada do firmware: esp32-idf3-20200902-v1.13
Referência para micropython:<http://docs.micropython.org/en/latest/pyboard/quickref.html>
"""
from machine import ADC, Pin, I2C, RTC
import socket
import network
from time import sleep_ms
import urequests as requests
import utime


def connect_wifi():
    station = network.WLAN(network.STA_IF)
    if station.isconnected() == True:
        return
    station.active(True)
    station.connect("VIVOFIBRA-0823", "EAEA9A0823")
    i = 0
    while station.isconnected() == False:
        sleep_ms(100)
        i += 1
        if(i == 100):
            machine.reset()
        pass
    print("conectado")
    res = requests.get(url='https://api.ipify.org/?format=text').text
    print('External IP:'+res)

connect_wifi()
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#https://docs.micropython.org/en/latest/esp32/quickref.html#adc-analog-to-digital-conversion
ANALOG_0 = 36
ANALOG_1 = 39
ANALOG_2 = 34
ANALOG_3 = 35
ANALOG_4 = 32

ADC_0 = ADC(Pin(ANALOG_0))    # create ADC object on ADC pin
ADC_0.atten(ADC.ATTN_11DB)    # set 11dB input attenuation (voltage range roughly 0.0v - 3.6v)
ADC_0.width(ADC.WIDTH_12BIT)  # set 12 bit return values (returned range 0-4095)

ADC_1 = ADC(Pin(ANALOG_1))    # create ADC object on ADC pin
ADC_1.atten(ADC.ATTN_11DB)    # set 11dB input attenuation (voltage range roughly 0.0v - 3.6v)
ADC_1.width(ADC.WIDTH_12BIT)  # set 12 bit return values (returned range 0-4095)

ADC_2 = ADC(Pin(ANALOG_2))    # create ADC object on ADC pin
ADC_2.atten(ADC.ATTN_11DB)    # set 11dB input attenuation (voltage range roughly 0.0v - 3.6v)
ADC_2.width(ADC.WIDTH_12BIT)  # set 12 bit return values (returned range 0-4095)

ADC_3 = ADC(Pin(ANALOG_3))    # create ADC object on ADC pin
ADC_3.atten(ADC.ATTN_11DB)    # set 11dB input attenuation (voltage range roughly 0.0v - 3.6v)
ADC_3.width(ADC.WIDTH_12BIT)  # set 12 bit return values (returned range 0-4095)

ADC_4 = ADC(Pin(ANALOG_4))    # create ADC object on ADC pin
ADC_4.atten(ADC.ATTN_11DB)    # set 11dB input attenuation (voltage range roughly 0.0v - 3.6v)
ADC_4.width(ADC.WIDTH_12BIT)  # set 12 bit return values (returned range 0-4095)

ID = 0
buffer = []
linha = 0

rtc = RTC()
rtc.init((0, 0, 0, 0, 0, 0, 0, 0))
microseconds = 500

while True:
    start = utime.ticks_us()
    # read value using the newly configured attenuation and width
    #inertial = accel.gett_values() #dado do tipo dicionario
    # round() 茅 para delimitar a quantidade de casas decimais
    In_0 = round(((ADC_0.read())* 3.3 / 4095),2)
    In_1 = round(((ADC_0.read())* 3.3 / 4095),2)
    In_2 = round(((ADC_2.read())* 3.3 / 4095),2)
    #In_3 = round(((ADC_3.read())* 3.3 / 4095),2)
    #In_4 = round(((ADC_4.read())* 3.3 / 4095),2)
    #In_5 = 1.0
    #In_6 = 1.0
  ##  In_7 = 1.0
   # In_8 = 1.0
   # In_9 = 1.0
   # In_10 = 1.0
    In_11 = utime.ticks_ms( )
    sensores = [In_0, In_1, In_2, In_11, ID]
    
    #sensores = [In_0, In_1, In_2, In_3, In_4, In_5, In_6, In_7, In_8, In_9, In_10,In_11,ID]
    buffer.append(sensores)
   # print(len(data_string))
    #sleep_us(700) #para alcan莽ar um tempo de 20ms no final(real)
    #utime.sleep_us(900)
    #antes = utime.ticks_us()
    #gc.collect() resolve o problema de memória, mas é muito lento (cerca de 2 a 5ms a cada chamada)
    #gc.collect()
    #gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())
    #print(utime.ticks_diff(utime.ticks_us(), antes))
    while utime.ticks_diff(utime.ticks_us(), start) < microseconds:
        pass
        
    ID = ID + 1
    if(ID == 100): #numero de linhas -1 (ajusta o tamanho do buffer)
      ID = 0
      #buffer = (repr(buffer).encode())
      #data_string = repr(buffer).encode()  #coloca ''(repr) e depois transforma em bytes(encode) para conseguir enviar via socket
      #print(len(buffer))
     # print("passou aqui")
      cliente.sendto(repr(buffer).encode(), ("192.168.15.6", 12000))
      buffer = [] #limpa o buffer
      
    
















