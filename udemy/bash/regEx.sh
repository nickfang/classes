#!/bin/bash


#-----------------------------------------------------------------------
# 

#E_NOPATTERN=71
#DICT=/usr/share/dict/words
#
#if [ -z $1 ]
#then 
#   echo
#   echo "Usage:"
#   echo "`basename $0` \"pattern,\""
#   echo "where \"pattern\" is in the form"
#   echo "ooo..oo.o..."
#   echo
#   echo "the o's are letters you already know,"
#   echo "and the periods are missing letters."
#   echo "Letters are periods can be in any position."
#   echo "For example: w...i...n"
#   echo
#   echo $E_NOPATTERN
#fi
#
#grep ^"$1"$ "$DICT"



#-----------------------------------------------------------------------
#

#E_BADARGS=65
#if [ $# -eq 0 ]
#then
#   echo "Usage: `basename $0` file"
#   exit $E_BADARGS
#else
#   # for loop automatically works on positional parameters if like this
#   for i
#   do
#      # -e means set of instructions
#      # '1,/^$/d' delets from betinning of intput to first blank line
#      # '/^$/d'   delets all black lines
#      sed -e '1,/^$/d' -e '/^$/d' $i
#   done
#fi


#-----------------------------------------------------------------------
#

## ? will replace a single letter with wildcard
#ls -l woo?.txt
#
## specify a range of characters any letter between and including e-q.  recursive
#ls -l [e-q]*
#
## print out files that begin with w and print out files with oo in them (wood.txt is listed twice)
#ls -l {w*,*oo*}
#
## print out file names separated by space
#echo *
#
## print out files that begin with w
#echo w*

##lists all the files except for the . files
#for file in *
#do 
#   ls -la "$file"
#   shopt -s nullglob
#done


