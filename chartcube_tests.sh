#!/usr/bin/env/ sh
'''
Copyright (C) 2015  CODE PANDORA
Created on 2015-12-11
   __________  ____  ______   ____  ___    _   ______  ____  ____  ___
  / ____/ __ \/ __ \/ ____/  / __ \/   |  / | / / __ \/ __ \/ __ \/   |
 / /   / / / / / / / __/    / /_/ / /| | /  |/ / / / / / / / /_/ / /| |
/ /___/ /_/ / /_/ / /___   / ____/ ___ |/ /|  / /_/ / /_/ / _, _/ ___ |
\____/\____/_____/_____/  /_/   /_/  |_/_/ |_/_____/\____/_/ |_/_/  |_|

@author: Karuna Lingham
'''

#Begin console log
exec 1>logs/test_logs.txt

echo "================================="
echo "Chartcube App v1.3 ..."
echo "Running Test Suite v1.0 ..."
echo "================================="

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
    python $fname
  done
done
