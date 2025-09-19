import base64

def decode_base64(encoded_str):
    try:
        decoded_bytes = base64.b64decode(encoded_str)
        return decoded_bytes.decode('utf-8')
    except Exception as e:
        print(f"Error decoding: {e}")
        return None

if __name__ == "__main__":
    encoded_input = input("Enter Base64 encoded string: ")
    decoded_output = decode_base64(encoded_input)
    if decoded_output is not None:
        print("Decoded string:", decoded_output)