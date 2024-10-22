import random

# Generate binary keys dari satu key yang sama
def generate_keys(key_bin, num_keys, length):
    random.seed(key_bin)  # Seed berdasarkan binary dari key string
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
    key_bin = text_to_binary(key)  # Convert key string ke binary
    length = len(text_bin)
    
    # Jika key lebih pendek dari text, perlu ulang keynya
    full_key_bin = (key_bin * ((length // len(key_bin)) + 1))[:length]

    keys = generate_keys(display_binary(full_key_bin), num_keys, length)

    # XOR chain (((A ^ B1) ^ B2) ^ B3) ...
    cypher_bin = text_bin
    for key_bin in keys:
        cypher_bin = xor_binary(cypher_bin, key_bin)

    return cypher_bin

# Dekripsi dari teks cipher
def decrypt(cypher_bin, key, num_keys):
    key_bin = text_to_binary(key)  # Convert key string ke binary
    length = len(cypher_bin)

    # Ulang key jika lebih pendek
    full_key_bin = (key_bin * ((length // len(key_bin)) + 1))[:length]

    keys = generate_keys(display_binary(full_key_bin), num_keys, length)

    # XOR chain reverse (((Cypher ^ B4) ^ B3) ^ B2) ...
    original_bin = cypher_bin
    for key_bin in reversed(keys):
        original_bin = xor_binary(original_bin, key_bin)

    return original_bin

# Tampilin binary dengan format yang lebih rapi
def display_binary(bin_data):
    return ''.join(str(b) for b in bin_data)

# Input teks dan key
A = "Hello World"
key = "dlroW olleH"
num_keys = 4

# Enkripsi
print("Original Text:", A)
text_bin = text_to_binary(A)
print("Binary Text:", display_binary(text_bin))

cypher_bin = encrypt(A, key, num_keys)
cypher_text = binary_to_text(cypher_bin)

# Key ke binary
binary_key = text_to_binary(key)
print("Secret Key (Binary):", display_binary(binary_key))

print("Ciphertext Binary:", display_binary(cypher_bin))
print("Ciphertext (Encoded as Text):", cypher_text)

# Decrypt dari binary langsung
decrypted_bin = decrypt(cypher_bin, key, num_keys)
decrypted_text = binary_to_text(decrypted_bin)

print("Decrypted Binary:", display_binary(decrypted_bin))
print("Decrypted Text:", decrypted_text)
