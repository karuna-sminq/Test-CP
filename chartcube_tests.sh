#!/usr/bin/bash

d="$(date +'%d-%m-%Y')"
t="$(date +%H:%M)"
now=$d-$t

#Begin console log
exec > >(tee -i logs/chart_logs_$now.txt)
#copy stderr to console output
exec 2>&1

echo '''
Copyright (C) 2015-2016  CODE PANDORA
Created on 2015-12-11
Updated on 2016-01-13

   __________  ____  ______   ____  ___    _   ______  ____  ____  ___
  / ____/ __ \/ __ \/ ____/  / __ \/   |  / | / / __ \/ __ \/ __ \/   |
 / /   / / / / / / / __/    / /_/ / /| | /  |/ / / / / / / / /_/ / /| |
/ /___/ /_/ / /_/ / /___   / ____/ ___ |/ /|  / /_/ / /_/ / _, _/ ___ |
\____/\____/_____/_____/  /_/   /_/  |_/_/ |_/_____/\____/_/ |_/_/  |_|

@author: Karuna Lingham
'''

echo "================================="
echo "Chartcube App v1.4 ..."
echo "Running Test Suite v1.13 ..."
echo "================================="

text1="OK"
text2="ERROR"
total_count=0

start=`date +%s`
#Begin iterating through every folder
for folder in ./*
do

  #Begin recording tests for every folder
  adb shell screenrecord /sdcard/$folder.mp4 &
  echo "------------------"
  echo "$folder"
  echo "------------------"

  #Begin iterating through every file in specified folder
  for fname in $folder/*.py
  do

    #Passed tests
    if grep --quiet $text1 logs/chart_logs_$now.txt; then
      echo "Tests Passed: "
      echo -e "\e[32m" #green
      grep -2A1 $text1 "logs/chart_logs_$now.txt"
      echo -e "\e[39m" #default color
    fi

    #Failed tests
    if grep --quiet $text2 logs/chart_logs_$now.txt; then
      echo "Tests Failed: "
      echo -e "\e[31m" #red
      grep -1A3 $text2 "logs/chart_logs_$now.txt"
      echo -e "\e[39m" #default color
    fi

    #Indicate when testing an Interim file
    if [ $(find $fname -regex .*interim.*\.py) ]
    then
      echo "*****$fname: INTERIM FILE*****"
    fi

    #Execute file
    python $fname
    total_count=$((total_count + 1))
  done
done

#Total test count and timer
end=`date +%s`
runtime=$((end - start))
echo "Time taken for $total_count tests: $runtime sec"
