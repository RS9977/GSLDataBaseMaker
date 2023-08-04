#!/bin/bash

# Set the directory where your C source files are located
SOURCE_DIR="./"

# Function to compile C source files with -fdump-tree-ssa
compile_with_ssa_dump() {
    local source_file="$1"
    local output_file="$(basename "$source_file" .c).o"
    gcc -c -fdump-tree-ssa-gimple "$source_file" -o "$output_file"
}

# Loop through all C source files in the directory and compile them with -fdump-tree-ssa
for source_file in "$SOURCE_DIR"/*.c; do
    echo "Compiling $source_file with SSA dump..."
    compile_with_ssa_dump "$source_file"
    echo "Compilation with SSA dump for $source_file completed."
done

echo "All C source files in the directory have been compiled with SSA dump."
