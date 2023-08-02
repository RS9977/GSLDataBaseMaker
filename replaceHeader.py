import os
import fileinput

def replace_include_lines(directory):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith(".c"):
                file_path = os.path.join(root, file_name)
                replace_include_line(file_path)

def replace_include_line(file_path):
    with fileinput.FileInput(file_path, inplace=True) as file:
        for line in file:
            # Replace "#include <config.h>" with "#include "config.h""
            print(line.replace("#include <config.h>", '#include \"config.h\"'), end='')

if __name__ == "__main__":
    source_directory = "./"
    replace_include_lines(source_directory)
    print("Done! Replaced '#include <config.h>' with '#include \"config.h\"' in C source files.")
