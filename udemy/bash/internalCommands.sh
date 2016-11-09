#!/bin/bash

#--------------------------------------------------------------------------------
# printf - print to screen with formatting. 

#declare -r PI=3.1415926
#
#printf "Second decimal of PI is %1.2f\n" $PI
#printf "Fifth decimal of PI is %1.5f\n" $PI

#--------------------------------------------------------------------------------
# read - look at man page for all the options.  There are many

#up=$'\x1b[A'
#down=$'\x1b[B'
#left=$'\x1b[D'
#right=$'\x1B[C'
#
#read -s -n3 -p "Press an arrow key: " arrow
#
#case $arrow in
#   $up) echo "You pressed up";;
#   $down) echo "You pressed down";;
#   $left) echo "You pressed left";;
#   $right) echo "You pressed right";;
#esac
#
#
#echo "Enter a string"
#read var
#echo "$var"
##Enter a string
##test\\
##test\
#
#echo "Enter a string"
#read -r var
#echo $var
##Enter a string
##test\\
##test\\

## Take all the contents of file1 and echo them out.
#echo "Read"
#while read var
#do
#   echo $var
#done < file1

#--------------------------------------------------------------------------------
# eval -
# set - use +/- to enable and disable options

##look for a process that contains the first argument passed to the script
#if [ ! -z $1 ]
#then
#   process="ps -e | grep $1"
#fi
#
#eval $process

##turn on and off storing you commands
#set +o history
#set -o history
#echo "Before setting the parameters"
#echo "\$1 = $1"
#echo "\$2 = $2"
#
#set `echo "three four"`
#
#echo "After setting parameters"
#echo "\$1 = $1"
#echo "\$2 = $2"

##set can set options for a variable
#var="1 2 3"
#echo $var
#set -- $var
#i=1
#while [ $i -le $# ]
#do
#   echo -n "\$$i = "
#   eval echo \$$i
#   (( i++ ))
#done
#
#set --
#echo "\$1 = $1"
#echo "\$2 = $2"
#echo "\$3 = $3"
#
#
## unset
#var '1 2 3'
#echo "$var"
#unset var
#echo "$var"
#

##getops - take in option "d" "m" or "dm" any other option will echo usage
#while getopts :dm option
#do
#   case $option in
#      d) d_option=1
#      ;;
#      m) m_option=1
#      ;;
#      *) echo "Usage: -dm"
#   esac
#done
#
#day=`date | awk '{print $1 " " $3}'`
#
#if [[ ! -z $d_option ]]
#then
#   echo "Date is: $day"
#fi
#
#month=`date | awk '{print $2}'`
#if [[ ! -z $m_option ]]
#then
#   echo "Month is: $month"
#fi
#
#shift $(($OPTIND - 1))


#--------------------------------------------------------------------------------
# shopt - shell options.  ie. cdshell will auto correct words after cd
# type - 
# jobs
# disown


#sleep 5 & #run the sleep command in the background
#jobs # show the processes running in the background
#
#type disown
##disown is a shell builtin
#sleep 100 &
#sleep 90 &
#jobs
## shows the two running sleep jobs
#disown
#jobs
## shows one running sleep job

#--------------------------------------------------------------------------------
# fg - bring process to foreground
# wait - wait for all the background processes to finish 
# kill - kill a process

#sleep 1000 &
#sleep 1001 &
#sleep 1002 &
#jobs
#fg 2 #bring the second job listed to the foreground

#echo "Waiting for 5 seconds"
#sleep 5 &
#
#wait 
#
#times
#echo "done"


#ls ()
#{
#   echo "Overriding ls."
#}
#
#ls #run local function
#
#echo "####################"
#
#command ls #run ls command


