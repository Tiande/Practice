#!/bin/bash
# Program:
#          User inputs 2 integer numbers: program will cross these two numbers.
# History:
# 2015/05/20     Tiande     First release
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

echo -e "You SHOULD input 2 numbers, I will cross them!\n"
read -p "first number:" firstnu
read -p "second number:" secnu
total=$(($firstnu*$secnu))
# declare -i total=$firstnu*$secnu
echo -e "\nThe result of $firstnu x $secnu is ==> $total"
