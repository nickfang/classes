#!/bin/bash

#-----------------------------------------------------------------------
# Variables and Parameters


#-----------------------------------------------------------------------
# situations where you don't use the $

#var=10

#echo var
##var
#echo $var
##10

#unset var
#echo $var
##

#var1=4
#(( var2=var1<10?1:0))

#echo $var2


#-----------------------------------------------------------------------
# How to assign variables
# - using an '='
# - using the read command
# - in a loop

#var1=4

#echo "type in some value"
#read var2
#echo $var2
##prints out what you input

#for var in 1 2 3
#do 
#   echo "Value of var is $var"
#done


#-----------------------------------------------------------------------
# Properties of variables
# - need to use " " to preserve white spaces.  Otherwise echo will only

#var="T r a l a l a la   lalala "
#echo $var
##T r a l a l a la lalala
#echo "$var"
##T r a l a l a la   lalala 

#var=test1\ test2\ test3
#echo "$var"
##test1 test2 test3

#var=        #uninitialized variable
#echo $var
##

#var1=11 var2=22 var3=33 #better to put each variable on a separate line
#echo "$var1 $var2 $var3"
##11 22 33

#var=
#echo $var
##
#var=9
#echo $var
##9
#var=10
#echo $var
##10
#unset var
#echo $var
##

#var=
#let "var += 10"
#echo $var
##10
#let "var = var + 10"
#echo $var
##20

#hi='echo test'
#echo $hi

#hi=`ls ~/`
#echo "$hi"

#hi=$(ls -la)
#echo $hi


#-----------------------------------------------------------------------
# find and replace

#var=hey1100
#echo $var
##hey1100
#num=${var/hey/200}
#echo $num
##2001100

#var1=
#echo var1=$var1
##
#let "var1 += 10"
#echo $var1
##10  


#-----------------------------------------------------------------------
# 

MIN=10
if [ -n "$1" ]
then
   echo "1st one is $1"
fi

if [ -n "$2" ]
then
   echo "2nd one is $2"
fi

if [ -n "$3" ]
then
   echo "3rd one is $3"
fi

if [ -n "$4" ]
then
   echo "4th one is $4"
fi

if [ -n "$5" ]
then
   echo "5th one is $5"
fi

if [ -n "$6" ]
then
   echo "6th one is $6"
fi

if [ -n "$7" ]
then
   echo "7th one is $7"
fi

if [ -n "$8" ]
then
   echo "8th one is $8"
fi

if [ -n "$9" ]
then
   echo "9th one is $9"
fi
 
if [ -n "${10}" ]
then
   echo "10th one is ${10}"
fi

echo "List of arguments: "$*""
echo "Name of Script: \""$0"\""
if [ $# -lt "$MIN" ]
then
   echo "Not enough arguments, need 10 to run"
fi


