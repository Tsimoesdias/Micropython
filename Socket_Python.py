"""
Autor: Thiago S. 01/02/21
Objetivo: receber dados coletados com o esp32 (1000 Hz) - Micropython - uPycraft
Cada coluna representa um sensor
"""

import socket
import time
# import pickle
from ast import literal_eval
import numpy as np

#Nome_Arquivo = "C:\\Users\\tsimo\\Desktop\\VS\\final_15.txt"

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

servidor.bind(('', 12000))



while True:
    mensagem_bytes, endereco_ip_client = servidor.recvfrom(10000)
    mensagem_resposta = mensagem_bytes
    msg = mensagem_resposta.decode() #transforma bytes em lista (descodifica)
    msg1 = literal_eval(msg) #transforma bytes em lista (descodifica)
    #servidor.sendto(mensagem.encode(), endereco_ip_client)
    #São 11 linhas, pois é o tamanho do buffer enviado pelo esp32
    #print(msg1[0][0])

    tempo = time.time()
    #arquivo = open(Nome_Arquivo, "a", newline="")
    # for i in range(4): #vai de 0 a 3
    #     print(i)
    for i in range(100):
        if(i != 99):
            print(repr(msg1[i]))
            #arquivo.write(repr(msg1[i]))
            #arquivo.write('\n')
        if(i == 99):
            print(repr(msg1[i])+str(tempo))
            #arquivo.write(repr(msg1[i])+str(tempo))
            #arquivo.write('\n')
    #arquivo.close()

    #a = str(mensagem_resposta.decode('UTF-8')+t+c)
    #a = mensagem_resposta.decode('UTF-8')+str(t)+"--"+str(c)
    #dados = mensagem_resposta.decode('UTF-8')
    #print(a)
    #escrita(a)

    # c = c+1
