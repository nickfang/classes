#!/bin/bash

#num=1
#if [ $num -gt 0 ]
#then
#   if [ $num -lt 5 ]
#   then
#      if [ $num -gt 3 ]
#      then 
#         echo "GT 0, LT 5, GT3"
#      fi
#   fi
#elif [ $num -eq 0 ]
#then
#   echo "EQ 0"
#else
#   echo "I have no idea"
#fi


#var=/home/nfang/git/rpi/classes/udemy-bash/file1
#
#if [[ -e $var ]]
#then
#   echo "File exists"
#else
#   echo "File does not exist"
#fi


#(( 2 > 1 ))
#echo "Exit status is $? for 2 > 1"
##0
#(( 2 < 1 ))
#echo "Exit status is $? for 2 < 1"
##1
#(( 2 + 2 ))
#echo "Exit status is $? for 2 + 2"
##0

#------------------------------------------------------------
# standard file operators

#-f file is a regular file
#-s file size greater than zero
#-r file is readable
#-x file can be executable
#-w file is writable
#! reverses file test operator

#------------------------------------------------------------
# standard errors

NO_OF_ARGS=2

E_NOARGS=65
E_BADARGS=85
E_UNREADABLE=86
E_NOFILE=87
E_SIZE=89



#------------------------------------------------------------
#

if [ -z $var ] # if string is NULL or has zero length
