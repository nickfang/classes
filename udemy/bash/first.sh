#!/bin/bash

#name=tea

#echo "the word $name contains ${#name} chars"
#echo $((2#111))

#var=-10
#if [ "$var" -gt 0 ]; then echo "YES"; else echo "NO"; fi 

#-------------------------------------------------------------
# " " preserves white space
# ' ' does not allow for referencing variables

#colors="red black white"

#for color in $colors
#do
#   echo $color
#done
##red
##black
##white

#for color in "$colors"
#do
#   echo $color
#done
##red black white

#for color in "red white blue"
#do
#   echo $color
#done
##red white blue

#echo '$colors'
##$colors

#-------------------------------------------------------------
# , links series of operations and returns the last one

#let "y=((x=20, 10/2))"
#echo $y
##5


#-------------------------------------------------------------
# ,, used in lower case letter conversion

#var=DSLConNeCtiOn

#echo ${var,}
##dSLConNeCtiOn

#echo ${var,,}
##dslconnection


#-------------------------------------------------------------
# \ escape character

#echo ""Linux is Awesome""
##Linux is Awesome

#echo "\"Linux is Awesome\""
##"Linux is Awesome"

#-------------------------------------------------------------
# / 
# ` - backquote used to assign 

#let val=500/2
#val2=`echo $val`
#echo $val
#echo $val2
#250
#250


#-------------------------------------------------------------
# : null command.  Do nothing. 
# 

#var=20
#if ["$var" -lt 15 ]
#then :
#else
#   echo $var
#fi
##15

#var=20
#if ["$var" -lt 25 ]
#then :
#else
#   echo $var
#fi
##

#touch wood.txt
#echo "here is something, use it" > wood.txt
#cat wood.txt
##here is something, use it
#echo "something else" > wood.txt
#cat wood.txt
##something else
#echo "something else" >> wood.txt
#cat wood.txt
##something else
##something else
#: > wood.txt
#cat wood.txt
##
#rm wood.txt
#: > wood.txt
#echo "something more" >> wood.txt
#cat wood.txt
##something more
#: >> wood.txt
#cat wood.txt
##something more
#rm wood.txt


#-------------------------------------------------------------
# ! - negate or reverse condition

#var=10
#if [ "$var" != 0 ]
#then
#   echo NOT
#else
#   echo YES
#fi
##NOT


#-------------------------------------------------------------
# * - wildcard
# * - multiplication
# ** - exponitiation

#touch test1 test2 test3 test4
#ls 
#rm test*
#ls
## test files are gone

#let var=100*10
#let var2=100**3
#echo "$var $var2"
##1000 1000000


#-------------------------------------------------------------
# ? - if statement

#var1=100
#echo $(( var2 = var1<20 ? 1:0))
##1
#echo $var2
##1

#if [ $var1 -lt 20 ]
#then
#   var2=1
#else
#   var2=0
#fi
#echo $var2
##1


#-------------------------------------------------------------
# () - used to store group of commands.  Will create subshell.
#    - used for array initialization
# {} - can represent a block of code
#    - can act as a one line for loop (generate an array)


#var=5
#( var=10; )
#echo $var

#Colors=(red white brown purple)
#echo \${test1,test2,test3}\$
##$test1$ $test2$ $test3$

#cat {file1, file2, file3} > file
##take the contents of file1, file2 and file3 and write them into file.

#echo {1..9}
##1 2 3 4 5 6 7 8 9

#var1=1
#var2=2
#(
#var1=10
#var2=20
#echo "$var1 $var2"
##10 20
#)
#echo "$var1 $var2"
##1 2
#{
#var1=10
#var2=20
#}
#echo "$var1 $var2"
##10 20


#-------------------------------------------------------------
# || - logical or
# && - logical and

#var=1

#if [ $var -gt 0 ] || [ $var -eq 10 ]
#then
#   echo "One or both conditions true"
#else
#   echo "Both conditions are false"
#fi
##One or both conditions are true

#if [ $var -gt 0 ] && [ $var -eq 10 ]
#then
#   echo "Both conditions true"
#else
#   echo "One or more conditions are false"
#fi
##One or more conditions are false


#-------------------------------------------------------------
# - - optional prefix
#   - use for redirection
#   - subtraction
# + - addition
# / - divide
# % - modulus

#ls -l

#cd -
##goes back to the directory you were last in


#-------------------------------------------------------------
# ^ - uppercase conversion

#someWord=tEsT

#echo ${someWord^}
##TEsT
#echo ${someWord^^}
##TEST
