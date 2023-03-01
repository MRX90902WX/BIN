#! /bin/bash

while :
do
echo -e "  \e[1;32mDesea generar un nuevo bin \e[0m"
echo ""
echo -n -e "  \e[1;32m(\e[0m\e[1;37msi\e[0m\e[1;32m)  (\e[0m\e[1;37mno\e[0m\e[1;32m) :\e[0m"
read bin
case $bin in
si)
#! /bash/bin
bash iniciar.sh
exit
;;
no)
#! /bash/bin
exit
;;
esac
done
