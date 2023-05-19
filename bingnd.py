import sys
from random import randint
from os import system
import datetime                              
import random


#Code Modificado : ***Yimber C 19/05/23 
#Made in Ecuador : $%$%$%%$%%%
        
system("clear")
print(" \033[1;33m-----------------------------------")                      
print(" \033[1;33m| `7MM'''Yp, `7MMF'`7MN.   `7MF'  |")
print(" |   MM    Yb   MM    MMN.    M    |")
print(" |   MM    dP   MM    M YMb   M    |")
print(" |   \033[1;34mMM'''bg.   MM    M  `MN. M    |")
print(" |   MM    `Y   MM    M   `MM.M    |")
print(" | \033[1;31m  MM    ,9   MM    M     YMM    |")
print(" | .JMMmmmd9  .JMML..JML.    YM    |")                
print(" |                                 |")
system("bash day")
print(" \033[1;31m-----------------------------------")
bin_format = input(" \033[1;34m> \033[1;32mBIN: \033[1;37m")
cantidad = input(" \033[1;34m> \033[1;32mCANTIDAD: \033[1;37m")
print("")
system("bash loading")
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


def dategen():
  now = datetime.datetime.now()
  date = ""
  month = str(randint(1, 9))
  current_year = str(now.year)
  year = str(random.randint(23, 32))
  date = month + "/" + year

  return date

print("")
print("  \033[1;32m-------------------------------")
print(" \033[1;32m|       BIN        | DATE | CVV |")
print("  \033[1;32m-------------------------------")

def main():
  for i in range(int(cantidad)):                
    cc = generar_cc(bin_format)
    print(f" \033[1;32m| \033[1;37m{cc} \033[1;32m| \033[1;37m{dategen()} \033[1;32m| \033[1;37m{ccv_gen()}\033[1;32m |")
main()

print("  \033[1;32m-------------------------------")
print("")
print("")
system("bash funcion")

