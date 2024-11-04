import hashlib

# Base string
base_string = "DPf0Vayhe7uuIGLM"

# Function to find valid input
def find_valid_input():
    input_counter = 0
    while True:
        input_str = str(input_counter)
        combined_string = base_string + input_str
        sha256_hash = hashlib.sha256(combined_string.encode()).hexdigest()
        if sha256_hash.endswith('000000'):
            return input_str, sha256_hash
        input_counter += 1

# Find a valid input
valid_input, resulting_hash = find_valid_input()
print(f"Input: {valid_input}, SHA-256 Hash: {resulting_hash}") 