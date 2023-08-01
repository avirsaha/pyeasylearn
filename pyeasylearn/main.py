import ctypes
import os

# current working directory
print(os.getcwd())

# reading a regular .txt file
with open(r"tezx.txt", "r") as file:
    print(file.read())

# loading a simple c shared library
lib = ctypes.CDLL("cleaner.so")

# # defining the arguments and return types of the C functions.
# lib.process_string.argtypes = [ctypes.c_char_p]
# lib.process_string.restype = None
