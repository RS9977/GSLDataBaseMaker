import os
import re
import random

def rearrange_code(input_file, output_file):
    with open(input_file, 'r') as f:
        original_code = f.read()

    # Perform code rearrangement using regular expressions
    # For example, swapping two function definitions:
    rearranged_code = re.sub(r'(void\s+\w+\s*\(.*\))\s*(\{.*\})\s*(void\s+\w+\s*\(.*\))\s*(\{.*\})',
                             r'\4 \2 \3 \1', original_code)

    # Perform control flow modification
    # For example, randomizing if-else conditions:
    modified_code = re.sub(r'if\s*\((.*?)\)\s*{', lambda match: random_if_else(match.group(1)), rearranged_code)

    # Perform variable renaming
    # For example, renaming variables with a random suffix:
    #modified_code = re.sub(r'\b(\w+)\b', lambda match: match.group(1) + f'_var{random.randint(1, 100)}', modified_code)

    # Perform loop unrolling
    # For example, unrolling 'for' loops by a random factor:
    modified_code = re.sub(r'for\s*\((.*?);(.*?);(.*?)\)\s*{',
                           lambda match: random_unroll(match.group(1), match.group(2), match.group(3)), modified_code)

    with open(output_file, 'w') as f:
        f.write(modified_code)

def random_if_else(condition):
    # Introduce randomness in if-else conditions
    if random.random() < 0.5:
        return f'if ({condition}) {{'
    else:
        return f'else if ({condition}) {{'

def random_unroll(init, condition, update):
    # Unroll 'for' loops by a random factor (between 1 and 4)
    unroll_factor = random.randint(1, 4)
    return f'for ({init}; {condition}; {update}) {{\n' + '    ' + f'{init}; {condition}; {update};\n' * unroll_factor + '    ' + '}'

def process_files_in_directory(input_dir):
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".c"):
                input_c_file = os.path.join(root, file)
                output_c_file = input_c_file[:-2] + "2.c"
                rearrange_code(input_c_file, output_c_file)
                print(f"Processed: {input_c_file} => {output_c_file}")

if __name__ == "__main__":
    input_directory = "./"  # Replace with the path to the directory containing your C code files
    process_files_in_directory(input_directory)
