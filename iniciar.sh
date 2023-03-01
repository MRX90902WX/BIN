#! /bin/bash
chmod 777 generador.sh
echo ""
setterm -foreground green
figlet BIN
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
