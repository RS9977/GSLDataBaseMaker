#!/bin/bash

# Set the directory path where the files are located
directory_path="./"

# Check if the directory exists
if [ ! -d "$directory_path" ]; then
  echo "Directory not found: $directory_path"
  exit 1
fi

# Move to the directory
cd "$directory_path" || exit 1

# Loop through each file in the directory
for file in *; do
  # Check if the item is a file (not a directory or symbolic link)
  if [ -f "$file" ]; then
    # Append '.c' to the end of the filename
    new_filename="${file}.c"
    
    # Rename the file
    mv "$file" "$new_filename"
    echo "Renamed $file to $new_filename"
  fi
done
