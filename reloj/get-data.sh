#!/usr/bin/env bash
# Source folder: where the .zip has been unpacked. Has one subfolder for each type of data that the watch returns.
SRCFOLDER=~/Documentos/reloj
# Destination folder: Where the .csv files are moved after preprocessing
DSTFOLDER=~/Projects/personal/reloj/input

# Hearthrate auto: This file needs no preprocessing
cp ${SRCFOLDER}/HEARTRATE_AUTO/$(ls -1 ${SRCFOLDER}/HEARTRATE_AUTO | head -n1) ${DSTFOLDER}/hearthrate-auto.csv

# Sleep file. I need to remove the last column
csvtool -c1-7 ${SRCFOLDER}/SLEEP/$(ls -1 ${SRCFOLDER}/SLEEP | head -n1)> ${DSTFOLDER}/sleep.csv
echo "Finished getting data"
