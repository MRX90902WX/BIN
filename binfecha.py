import sys
from random import randint
from os import system
import datetime                              
import random

bin_format = input(" \033[1;37m[~]\033[1;32mIngrese el bin: \033[1;37m")
mes = input(" \033[1;37m[~]\033[1;32mIngrese el mes ej[4]: \033[1;37m")
año = input(" \033[1;37m[~]\033[1;32mIngrese el año ej[26]: \033[1;37m")
cantidad = input(" \033[1;37m[~]\033[1;32mIngrese la cantidad a generar: \033[1;37m")

print("")
system("sleep 2")
system("setterm -foreground green")

def esValido(num_tarjeta):
  suma = 0
  num_digitos = len(num_tarjeta)
  pos_par_impar = num_digitos & 1

  for i in range(0, num_digitos):
    digito = int(num_tarjeta[i])
    if not ((i & 1) ^ pos_par_impar):
      digito = digito * 2
    if digito > 9:
      digito = digito - 9
    suma = suma + digito

  return (suma % 10 == 0)

def generar_cc(bin_format):
  cc = ""
  if len(bin_format) == 16:
    for i in range(15):
      if bin_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
        cc += bin_format[i]
        continue
      elif bin_format[i] == "x":
        cc += str(randint(0, 9))
      else:
        print("\nCaracter no valido en el formato: {}\n".format(bin_format))
        print("El formato del bin es: xxxxxxxxxxxxxxxx de 16 digitos\n")
        sys.exit()

    for i in range(10):
      verificador = cc + str(i)
      if esValido(verificador):
        cc = verificador
        break
      else:
        verificador = cc

  else:
    print("\nERROR: Inserte un bin válido\n")
    print("SOLUCIÓN: El formato del bin es: xxxxxxxxxxxxxxxx de 16 dígitos\n")
    sys.exit()

  return cc

def ccv_gen():
  ccv = ""
  num = randint(10, 999)
  ccv = "0" + str(num) if num < 100 else str(num)
  return ccv


print("  \033[1;32m-------------------------------")

def main():
  for i in range(int(cantidad)):                
    cc = generar_cc(bin_format)
    print(f" \033[1;32m| \033[1;37m{cc} \033[1;32m| \033[1;37m{mes}/{año} \033[1;32m| \033[1;37m{ccv_gen()}\033[1;32m |")
    print("  \033[1;32m-------------------------------")
main()

print("")
system("bash funcion")
