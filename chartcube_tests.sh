#!/usr/bin/bash

d="$(date +'%d-%m-%Y')"
t="$(date +%H:%M)"
now=$d-$t

#Begin console log
exec > >(tee -i ANDROID/logs/chart_logs_$now.txt)
#copy stderr to console output
exec 2>&1

echo '''
Copyright (C) 2015-2016  CODE PANDORA
Created on 2015-12-11
Updated on 2016-04-04

   __________  ____  ______   ____  ___    _   ______  ____  ____  ___
  / ____/ __ \/ __ \/ ____/  / __ \/   |  / | / / __ \/ __ \/ __ \/   |
 / /   / / / / / / / __/    / /_/ / /| | /  |/ / / / / / / / /_/ / /| |
/ /___/ /_/ / /_/ / /___   / ____/ ___ |/ /|  / /_/ / /_/ / _, _/ ___ |
\____/\____/_____/_____/  /_/   /_/  |_/_/ |_/_____/\____/_/ |_/_/  |_|

@author: Karuna Lingham
'''

echo "================================="
echo "Chartcube App v1.5.51 ..."
echo "Running Test Suite v1.71 ..."
echo "================================="

text1="OK"
text2="FAILED"
total_count=0
pass=" "
fail=" "
start=`date +%s`

interim()
{
      #Indicate when testing an Interim file
      if [ $(find $fname -regex .*interim.*\.py) ]
      then
        echo "*****$fname: INTERIM FILE*****"
      fi
}

for folder in ANDROID/*
do

  #  #Begin recording tests for every folder
  #  adb shell screenrecord /sdcard/$folder.mp4 &
  #  echo "------------------"
  #  echo "$folder"
  #  echo "------------------"

  #Begin iterating through every file in specified folder
  for fname in $folder/*.py
  do

    interim #call to interim function

    # #Passed tests
    # if grep --quiet $text1 logs/chart_logs_$now.txt; then
    #   echo "Tests Passed: "
    #   echo -e "\e[32m" #green
    #   grep -2A1 $text1 "logs/chart_logs_$now.txt"
    #   grep -2A1 $text1 "logs/chart_logs_$now.txt" >> logs/pass.txt
    #   echo -e "\e[39m" #default color
    #   pass=$(grep "Test Case" logs/pass.txt)
    # fi
    #
    # #Failed tests
    # if grep --quiet $text2 logs/chart_logs_$now.txt; then
    #   echo "Tests Failed: "
    #   echo -e "\e[31m" #red
    #   grep -1A3 $text2 "logs/chart_logs_$now.txt"
    #   grep -1A3 $text2 "logs/chart_logs_$now.txt" >> logs/fail.txt
    #   echo -e "\e[39m" #default color
    #   fail=$(grep "Test Case" logs/fail.txt)
    # fi

    #Execute file
    python $fname
    total_count=$((total_count + 1))
  done
done

#Test count and timer
end=`date +%s`
runtime=$((end - start))
echo "================================="
echo "Time taken for $total_count tests: $runtime sec"
# echo -e "\nPassed: "
# echo -e "\n$pass"
# echo -e "\nFailed: "
# echo -e "\n$fail"
echo "================================="
