import random

# Generate binary keys dari satu key yang sama
def generate_keys(key, num_keys, length):
    random.seed(key)  # Seed berdasarkan key yang sama
    return [[random.randint(0, 1) for _ in range(length)] for _ in range(num_keys)]

# XOR operation
def xor_binary(text_bin, key_bin):
    return [t ^ k for t, k in zip(text_bin, key_bin)]

# Convert text to binary
def text_to_binary(text):
    return [int(b) for b in ''.join(format(ord(c), '08b') for c in text)]

# Convert binary to text
def binary_to_text(binary_data):
    binary_str = ''.join([str(b) for b in binary_data])
    text = ''.join(chr(int(binary_str[i:i+8], 2)) for i in range(0, len(binary_str), 8))
    return text

# Enkripsi dengan XOR chain
def encrypt(text, key, num_keys):
    text_bin = text_to_binary(text)
    length = len(text_bin)
    keys = generate_keys(key, num_keys, length)

    # XOR chain (((A ^ B1) ^ B2) ^ B3) ...
    cypher_bin = text_bin
    for key_bin in keys:
        cypher_bin = xor_binary(cypher_bin, key_bin)

    return cypher_bin

# Dekripsi dari teks cipher
def decrypt(cypher_text, key, num_keys):
    # Convert cipher text to binary
    cypher_bin = text_to_binary(cypher_text)
    
    length = len(cypher_bin)
    keys = generate_keys(key, num_keys, length)

    # XOR chain reverse (((Cypher ^ B4) ^ B3) ^ B2) ...
    original_bin = cypher_bin
    for key_bin in reversed(keys):
        original_bin = xor_binary(original_bin, key_bin)

    return original_bin

# Input teks dan key
A = "Hello World"
key = 1  # Bisa lu set sembarangan
num_keys = 4

# Enkripsi
cypher_bin = encrypt(A, key, num_keys)
cypher_text = binary_to_text(cypher_bin)

print("Ciphertext:", cypher_text)

# Decrypt
decrypted_bin = decrypt(cypher_text, key, num_keys)
decrypted_text = binary_to_text(decrypted_bin)

print("Decrypted text:", decrypted_text)
