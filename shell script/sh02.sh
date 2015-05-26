#!/bin/bash
# Program:
#   User inputs his first name and last name. Program will show his full name.
# History:
# 2015/05/20     Tiande     First release
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

read -p "Please input your first name: " firstname
read -p "Please input your last name: " lastname
echo -e "\nYour full name is: $firstname $lastname"
