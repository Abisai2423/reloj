# realizar un codigo en python que simule un reloj
# formato 24 horas
# que empiece n 00:00 hasta 23:59 y se reinicie
# pero que implemente time.seeo(x) para qu se actualice
# cada segundo o mas acelerado

import time
hora = 0
minuto = 0

while True:
    print(f"{hora:02d}:{minuto:02d}")
    time.sleep(1)
    minuto += 1
    if minuto == 60:
     minuto = 0
    hora += 1
    if hora == 24:
      hora = 0
