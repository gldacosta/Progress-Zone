#!/bin/bash
#To pass three arguments
args=("$@")
echo ${args[0]} ${args[1]} ${args[2]}
echo $#                                           #prints the length f the array


#./pattc.sh Shell is Full