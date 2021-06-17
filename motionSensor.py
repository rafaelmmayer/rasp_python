import os
from gpiozero import MotionSensor
from datetime import datetime

pir = MotionSensor(14)
num_arquivo = 1

dir = "./data/"

while True:
    nome_arquivo = f"{dir}Arquivo {num_arquivo}.txt"
    pir.wait_for_motion()
    print("Movimento detectado")
    print(datetime.now())
    pir.wait_for_no_motion()
    if (os.path.exists(dir)) is not True:
        os.mkdir(dir)    
    with open(nome_arquivo, "w") as file:
        file.write(f"Movimento detectado em {datetime.now()}")
    num_arquivo += 1
    