import ctypes

# Load the shared library
cleaner_lib = ctypes.CDLL("./lib/cleaner.so")

# Define the return type and argument types for the C function
cleaner_lib.clean_text.restype = ctypes.c_char_p
cleaner_lib.clean_text.argtypes = [ctypes.c_char_p]

# Define the input text
input_text = b"This is @an example^ text!"

# Clean the text using the C function
cleaned_text = cleaner_lib.clean_text(input_text).decode("utf-8")

# Print the result
print(cleaned_text)
