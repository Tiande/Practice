#!/bin/bash
# Program:
#     Using for ... loop to print 3 animals
# History:
# 2015/05/25     Tiande     First release
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:/~bin
export PATH

for animal in dog cat elephant
do
    echo "There are ${animal}s"
done
