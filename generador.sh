#! /bin/bash

chmod 777 generador.sh
clear
echo ""
echo -e " \e[1;33m____ ___ _   _\e[0m"
echo -e "\e[1;33m| __ )_ _| \ | |\e[0m"
echo -e "\e[1;34m|  _ \| ||  \| |\e[0m"
echo -e "\e[1;34m| |_) | || |\  |\e[0m"
echo -e "\e[1;31m|____/___|_| \_|\e[0m"
echo "" 
while :
do
echo -e -n " \e[1;32m1)\e[0m\e[1;37mGenerar bin Rnd\e[0m      \e[1;32m2)\e[1;37mGenerar bin con fecha Rnd\e[0m"
echo ""
echo ""
echo -n -e " \e[1;32mOpción:\e[0m \e[1;37m\e[0m"
read bin
case $bin in
1)
#! /bin/bash
echo ""
python bingnd.py
exit
;;
2)
#! /bin/bash
echo ""
python binfecha.py
exit
;;
esac
done
