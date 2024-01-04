# Import the os module for interacting with the operating system
import os

# Print the current working directory (cwd)
print("Current Working Directory:", os.getcwd())

# Get the directory name of the absolute path of the current script (__file__)
script_directory = os.path.dirname(os.path.abspath(__file__))
print("Directory of the Script:", script_directory)

# Get and print the absolute path of the current script (__file__)
absolute_path = os.path.abspath(__file__)
print("Absolute Path of the Script:", absolute_path)
