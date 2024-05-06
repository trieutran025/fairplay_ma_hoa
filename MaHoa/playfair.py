import tkinter as tk
from tkinter import messagebox

def generate_playfair_key(key):
    # Tạo một ma trận 5x5 từ key
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    key = key.upper().replace("J", "I")  # Loại bỏ J và thay thế bằng I
    key_matrix = ""
    for char in key + alphabet:
        if char not in key_matrix:
            key_matrix += char
    return key_matrix

def find_position(key_matrix, char):
    # Tìm vị trí của ký tự trong ma trận
    row = col = 0
    for i in range(5):
        for j in range(5):
            if key_matrix[5 * i + j] == char:
                row, col = i, j
                break
    return row, col

def decrypt(ciphertext, key):
    key_matrix = generate_playfair_key(key)

    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        row1, col1 = find_position(key_matrix, ciphertext[i])
        row2, col2 = find_position(key_matrix, ciphertext[i + 1])

        if row1 == row2:
            plaintext += key_matrix[row1 * 5 + (col1 - 1) % 5]
            plaintext += key_matrix[row2 * 5 + (col2 - 1) % 5]
        elif col1 == col2:
            plaintext += key_matrix[((row1 - 1) % 5) * 5 + col1]
            plaintext += key_matrix[((row2 - 1) % 5) * 5 + col2]
        else:
            plaintext += key_matrix[row1 * 5 + col2]
            plaintext += key_matrix[row2 * 5 + col1]

    return plaintext

def decrypt_text():
    key = key_entry.get()
    ciphertext = ciphertext_entry.get()
    decrypted_text = decrypt(ciphertext, key)
    plaintext_text.delete(1.0, tk.END)
    plaintext_text.insert(tk.END, decrypted_text)

# Tạo giao diện
root = tk.Tk()
root.title("Playfair Cipher Decrypt")

# Khóa
key_label = tk.Label(root, text="Key:")
key_label.grid(row=0, column=0, padx=5, pady=5)
key_entry = tk.Entry(root)
key_entry.grid(row=0, column=1, padx=5, pady=5)

# Văn bản mã hóa
ciphertext_label = tk.Label(root, text="Plaintext:")
ciphertext_label.grid(row=1, column=0, padx=5, pady=5)
ciphertext_entry = tk.Entry(root)
ciphertext_entry.grid(row=1, column=1, padx=5, pady=5)

# Nút giải mã
decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

# Kết quả giải mã
plaintext_label = tk.Label(root, text=" Decrypted text:")
plaintext_label.grid(row=3, column=0, padx=5, pady=5)
plaintext_text = tk.Text(root, height=5, width=30)
plaintext_text.grid(row=3, column=1, padx=5, pady=5)

root.mainloop()