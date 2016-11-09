#!/bin/bash

#--------------------------------------------------------------------------------------
# $$ - process id of the current script
# $BASH_VERSINFO - bash version info
# $PATH - 
# $UID
# $EUID
# $EDITOR
# $FUNCNAME


#echo $$ 

#for n in {0..5}
#do
#   echo "BASH_VERSINFO[$n] = ${BASH_VERSINFO[$n]}"
#done

#ROOT_UID=0
#echo -n "YOU ARE: "  # -n does not do a \n
#if [ "$UID" -eq "$ROOT_UID" ]
#then 
#   echo -n "root. "
#else
#   echo -n "user. "
#fi
#echo " YOUR \$UID = $UID."


#someFunction()
#{
#   echo "Function name is $FUNCNAME"
#   #Function name is someFunction
#}

#someFunction
#echo "Outside, \$FUNCNAME = $FUNCNAME"
##Outside, $FUNCNAME = 



#--------------------------------------------------------------------------------------
# $GROUPS - can be an array
# $HOME
# $HOSTNAME
# $HOSTTYPE - system hardware
# $MACHTYPE - machine type
# $IFS - field separator
# $LINENO - current line number
# $OLDPWD - last directory 
# $OSTYPE - 
# #PWD - current directory

#if [[ $HOSTNAME && $USER && $HOME ]]
#then 
#   echo "HOSTNAME: $HOSTNAME"
#   echo "USER: $USER"
#   echo "HOME: $HOME"
#   echo "Variables are set"
#else
#   echo "Variables are not set"
#fi
#
#
#colors1="red-brown-orange"
#colors2="red+brown+orange"
#
#echo "IFS=-"
#IFS=-
#echo $colors1
##red brown orange
#echo $colors2
##red+brown+orange
#
#echo "IFS=+"
#IFS=+
#echo $colors1
##red-brown-orange
#echo $colors2
##red brown orange
#
#echo $LINENO
##83
#
#echo $OLDPWD
#
#
#echo $OSTYPE
#
#echo $PWD
#
#echo ${PIPESTATUS[*]}
#


#--------------------------------------------------------------------------------------
# $REPLY - what the user typed for a read.  this is for if you don't read into a variable
# $SECONDS - number of seconds the script has been running
# declare -r - make a variable read only
# declare -i - make a variable an integer
# declare -a - make a variable an array
# declare -f - make a function
# declare -x - declare a variable that can be exported outside of environment

#echo "Some Question"
#read
#
#echo "The answer to the question is $REPLY"
#
#echo "Some other question"
#read var
#
#echo "Your answer is $var"
#


#LIMIT_TIME=12
#TIME_INTERVAL=3
#
#echo "This script will runn for $LIMIT_TIME seconds."
#echo "Press ctrl-c to exit before the time limit."
#while [ $SECONDS -le $LIMIT_TIME ]
#do
#   echo "This script has been running for $SECONDS seconds."
#   sleep $TIME_INTERVAL
#done


#declare -r var_r=5
#echo "\$var_r = $var_r"
##$var_r = 5
#
#declare -i var_i=10
#echo "\$var_i = $var_i"
##$var_i = 10
#var_i=blue
#echo "\$var_i = $var_i"
##$var_i = 0
#

#x=8/2
#echo "\$x = $x"
##$x = 8/2
#let x=8/2
#echo "\$x = $x"
##$x = 4
#declare -i x=8/2
#echo "\$x = $x"
##$x = 4
#

#declare -a x=(1 2 3 4 5)
#for i in {0..4}
#do
#   echo "${x[$i]}"
#   let "i += 1"
#done
#

#declare -f someFunction
#
#someFunction()
#{
#   echo "Hey, how are you doing?"
#}
#someFunction
#

#declare -x var_x=10
#echo $var_x


#--------------------------------------------------------------------------------------
# $RANDOM - generate number between 0 and 32767

MAX=10
i=1
while [ $i -le $MAX ]
do
   n=$RANDOM
   echo $n
   let "i += 1"
done
