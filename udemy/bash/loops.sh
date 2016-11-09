#!/bin/bash

#-----------------------------------------------------------------
# for loop

#for i in 1 2 3 4 5
#do
#   echo "Outer Loop $i -----------------"
#   for j in 1 2 3
#   do
#      echo "Inner Loop $j!!! Outer Loop Iteration $i"
#   done
#done
##Outer Loop 1 -----------------
##Inner Loop 1!!! Outer Loop Iteration 1
##Inner Loop 2!!! Outer Loop Iteration 1
##Inner Loop 3!!! Outer Loop Iteration 1
##Outer Loop 2 -----------------
##Inner Loop 1!!! Outer Loop Iteration 2
##Inner Loop 2!!! Outer Loop Iteration 2
##Inner Loop 3!!! Outer Loop Iteration 2
##Outer Loop 3 -----------------
##Inner Loop 1!!! Outer Loop Iteration 3
##Inner Loop 2!!! Outer Loop Iteration 3
##Inner Loop 3!!! Outer Loop Iteration 3
##Outer Loop 4 -----------------
##Inner Loop 1!!! Outer Loop Iteration 4
##Inner Loop 2!!! Outer Loop Iteration 4
##Inner Loop 3!!! Outer Loop Iteration 4
##Outer Loop 5 -----------------
##Inner Loop 1!!! Outer Loop Iteration 5
##Inner Loop 2!!! Outer Loop Iteration 5
##Inner Loop 3!!! Outer Loop Iteration 5
#


#-----------------------------------------------------------------
# while loop - continue if true

#a=unset
#prev=$a
#
#while echo "Previous variable = $prev"
#      echo
#      prev=$a
#      [ "$a" != end ]
#do
#   echo "Input end to exit or anything else to go on!"
#   read a
#   echo "variable = $a"
#done
#
#
#while [ $a != end ]
#do
#   echo "Input end to exit or anything else to go on!"
#   read a
#   echo "variable = $a"
#done


#-----------------------------------------------------------------
# until loop - exit if true

#until [ $n = end ]
#do
#   echo "Input end to exit or something else to move on"
#   read n
#   echo $n
#done



#-----------------------------------------------------------------
# break
# continue

#UPPER_LIMIT=9
#
#echo "Numbers 1 to 10 (but not 3 and 11)."
#
#n=0
#
#while [ $n -le $UPPER_LIMIT ]
#do
#   n=$(($n+1))
#
#   if [ "$n" -eq 3 ] || [ "$n" -eq 11 ]
#   then 
#      continue
#   fi
#   
#   echo -n "$n "
#done
#
#echo
#
#n=0
#
#while [ $n -le $UPPER_LIMIT ]
#do
#   n=$(($n+1))
#
#   if [ "$n" -gt 2 ] 
#   then 
#      break
#   fi
#   
#   echo -n "$n "
#done


#-----------------------------------------------------------------
# break and continue in nested loops

#for i in 1 2
#do
#   echo "Loop 1: iteration $i"
#   for j in 1 2 3
#   do
#      echo -e "\tLoop 2: iteration $j"
#      for k in 1 2 3 4
#      do
#         echo -e "\t\tLoop 3: iteration $k"
#         if [ $k -eq 2 ]
#         then 
#            break 2 # break two levels. break out of loop 3 and 2.
#         fi
#      done
#   done
#done
#
#for i in 1 2 3 4 5
#do
#   echo "Loop 1: iteration $i"
#   for j in 1 2 3
#   do
#      echo -e "\tLoop 2: iteration $j"
#      for k in 1 2 3 4
#      do
#         echo -e "\t\tLoop 3: iteration $k"
#         if [ $k -eq 2 ]
#         then
#            continue 3 # continue to the next iteration on loop 1
#         fi
#      done
#   done
#done


               
#-----------------------------------------------------------------
# case

#echo -n "Enter a letter or a digit: "
#read a
#
#case $a in
#   [[:lower:]] ) echo "$a is a lower case letter";;
#   [[:upper:]] ) echo "$a is an upper case letter";;
#   [0-9]       ) echo "$a is a digit";;
#   *           ) echo "$a is a special character";;
#esac
#
#exit 0


#-----------------------------------------------------------------
# PS3 - for select prompt

#PS3='Pick a color: '
#
#select color in "brown" "grey" "black" "orange" "red"
#do
#   echo "You selected this color: $color"
#   break
#done
