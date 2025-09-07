import base64

def decode_pass(password):
    decode_bytes = base64.b64decode(password)
    decode_data = decode_bytes.decode()
    print(f"decoded password {decode_data}")

encode_string = input("Enter encoded password: ")
decode_pass(encode_string)