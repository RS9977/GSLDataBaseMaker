import os
from pycparser import c_parser, c_ast, parse_file

# Define a visitor class to modify the function
class FunctionVisitor(c_ast.NodeVisitor):
    def visit_FuncDef(self, node):
        if node.decl.name == "double_input":
            # Change the function body
            node.body.block_items = [
                c_ast.Return(
                    c_ast.BinaryOp(
                        op="+",
                        left=node.body.block_items[0].expr,
                        right=node.body.block_items[0].expr
                    )
                )
            ]

# Input and output directory paths
input_directory = "./"
output_directory = "./"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Process each C file in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".c"):
        input_filepath = os.path.join(input_directory, filename)
        
        # Load and parse the C code from the input file
        with open(input_filepath, "r") as file:
            c_code = file.read()

        parsed_ast = parse_file(input_filepath, use_cpp=True)

        # Apply the modifications using the visitor
        visitor = FunctionVisitor()
        visitor.visit(parsed_ast)

        # Generate the modified C code
        modified_code = parsed_ast.show()

        # Create the output filename with "__1" appended
        output_filename = filename.replace(".c", "__1.c")
        output_filepath = os.path.join(output_directory, output_filename)

        # Write the modified C code to the output file
        with open(output_filepath, "w") as file:
            file.write(modified_code)

        print(f"Modified code written to {output_filepath}")
