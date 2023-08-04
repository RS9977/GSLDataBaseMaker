#!/bin/bash

# Check if the script was called with the correct number of arguments
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <directory_name>"
    exit 1
fi

# Store the input directory name in a variable
input_directory="$1"

# Check if the specified directory exists
if [ ! -d "$input_directory" ]; then
    echo "Error: Directory '$input_directory' does not exist."
    exit 1
fi

cd "$input_directory"

cp ../../DataBaseBuilder/*.py .
cp ../../DataBaseBuilder/D*.sh .
cp ../config.h .

python3 replaceHeader.py
python3 rearranger.py
python3 rearranger2.py
./DumpTrees.sh

cd ..