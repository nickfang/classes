#!/bin/bash

#--------------------------------------------------
# $? - return last return value

#echo "tralalala"
##tralalala
#echo $?
##0

#;aslkdfj;lkj
#echo $?
##127

#--------------------------------------------------
#


NO_OF_ARGS=2
E_BADARGS=85
E_UNREADABLE=86

if [ $# -ne "$NO_OF_ARGS" ]
then
   echo "Usage: 'basename $0' testFile1 testFile2"
exit $E_BADARGS
fi

if [[ ! -r "$1" || ! -r "$2" ]] # -r is a primary expression for if.  "True if FILE exists and is readable" http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_07_01.html
then
   echo "Files are not real"
   exit "$E_UNREADABLE"
fi

cmp $1 $2 &> /dev/null

if [ $? -eq 0 ]
then
   echo "Files are the same"
else
   echo "Files are different"
fi

exit 0   
