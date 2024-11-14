Here's a README file to explain the process of converting Python files into a Jupyter Notebook using various methods:


---

Python File to Jupyter Notebook Conversion

This README provides instructions for converting Python files (.py) into Jupyter Notebooks (.ipynb). Three methods are outlined below: using a Python script, manually using the Jupyter Notebook interface, and using jupytext, a command-line tool.

Method 1: Using nbformat and nbconvert in Python

This Python script will read the contents of two or more Python files and generate a single Jupyter notebook that contains the code from all specified files.

Prerequisites

Ensure you have the nbformat package installed:

pip install nbformat

Instructions

1. Save the following script as convert_to_notebook.py:

import nbformat as nbf

def py_to_ipynb(file_paths, output_notebook):
    # Create a new notebook object
    notebook = nbf.v4.new_notebook()
    cells = []

    # Convert each .py file content to a cell
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            code = file.read()
            # Create a new code cell with the file's content
            cells.append(nbf.v4.new_code_cell(code))

    # Add cells to the notebook
    notebook['cells'] = cells

    # Write notebook to the specified output file
    with open(output_notebook, 'w') as out_file:
        nbf.write(notebook, out_file)

# Define your .py file paths and output notebook name
file_paths = ['file1.py', 'file2.py']
output_notebook = 'combined_notebook.ipynb'
py_to_ipynb(file_paths, output_notebook)


2. Update file_paths to include the paths of your Python files, and set the desired output notebook name (e.g., combined_notebook.ipynb).


3. Run the script:

python convert_to_notebook.py


4. The generated notebook, combined_notebook.ipynb, will contain all the code from the specified .py files in separate cells.




---

Method 2: Manually Using Jupyter Notebook Interface

1. Open Jupyter Notebook from your Anaconda interface.


2. Create a new notebook.


3. Copy the code from each .py file, and paste it into separate cells in the notebook.


4. Save the notebook with your desired name.




---

Method 3: Using jupytext (Command Line Tool)

jupytext is a powerful tool that allows you to convert between .py and .ipynb formats directly from the command line.

Prerequisites

Install jupytext:

pip install jupytext

Instructions

1. To convert each .py file to a notebook, run:

jupytext --to notebook file1.py
jupytext --to notebook file2.py


2. To combine the contents, you can manually open the resulting .ipynb files in Jupyter and copy the cells into a single notebook.



