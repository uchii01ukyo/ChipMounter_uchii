#! /bin/bash
cd /Users/uchiiukyo/ChipMounter_uchii/src/
if [ ! -e $"waiting.txt" ]; then
  touch waiting.txt
fi
echo -n "" > waiting.txt
open start-2.command
python csv_gcode.py main -i '../data/sample.csv'