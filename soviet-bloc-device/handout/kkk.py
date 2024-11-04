hex_string = " 97ebd3cb97eab0f4"

# Decode the hexadecimal string
try:
    decoded_bytes = bytes.fromhex(hex_string)
    decoded_string = decoded_bytes.decode('utf-8', errors='ignore')  # Ignore errors for non-printable characters
    print(decoded_string)
except Exception as e:
    print(f"Error: {e}")
