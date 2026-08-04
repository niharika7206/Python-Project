"""
===========================================
CRYPTOGRAPHY TOOLKIT
-------------------------------------------
Classical Cipher Encryption & Decryption
Implemented in Python

Ciphers:
1. Caesar
2. Vigenere
3. Rail Fence
4. Playfair
5. Columnar
6. Double Columnar
7. Affine
8. Baconian
9. Bifid
-------------------------------------------
Author : Niharika
Language : Python
===========================================
"""

def caesar_encrypt(text, shift):

    result = ""

    for char in text:

        if char.isalpha():

            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            result += chr((ord(char) - start + shift) % 26 + start)

        else:

            result += char

    return result
# ===================================
# CAESAR DECRYPTION
# ===================================

def caesar_decrypt(text, shift):

    return caesar_encrypt(text, -shift)
# ===================================
# CAESAR BRUTE FORCE ATTACK
# ===================================

def caesar_bruteforce(ciphertext):

    print("\nPossible Plaintexts:\n")

    for key in range(26):
        plaintext = caesar_decrypt(ciphertext, key)
        print(f"Key {key:2}: {plaintext}")


# ===================================
# CAESAR MENU
# ===================================

def caesar_menu():
    while True:

        print("\n========== Caesar Cipher ==========")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Brute Force Attack")
        print("4. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            text = input("Enter Plaintext: ")
            shift = int(input("Enter Shift Value: "))

            ciphertext = caesar_encrypt(text, shift)

            print("\nCiphertext:", ciphertext)

        elif choice == "2":

            text = input("Enter Ciphertext: ")
            shift = int(input("Enter Shift Value: "))

            plaintext = caesar_decrypt(text, shift)

            print("\nPlaintext:", plaintext)

        elif choice == "3":

            text = input("Enter Ciphertext: ")

            caesar_bruteforce(text)

        elif choice == "4":

            break

        else:

            print("Invalid Choice!")

# ================================
# VIGENERE ENCRYPTION
# ================================

def vigenere_encrypt(text, key):

    result = ""

    key = key.upper()
    key_index = 0

    for char in text:

        if char.isalpha():

            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            shift = ord(key[key_index % len(key)]) - ord('A')

            result += chr((ord(char) - start + shift) % 26 + start)

            key_index += 1

        else:
            result += char

    return result
# ================================
# VIGENERE DECRYPTION
# ================================

def vigenere_decrypt(text, key):

    result = ""

    key = key.upper()
    key_index = 0

    for char in text:

        if char.isalpha():

            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            shift = ord(key[key_index % len(key)]) - ord('A')

            result += chr((ord(char) - start - shift) % 26 + start)

            key_index += 1

        else:
            result += char

    return result
# ================================
# VIGENERE MENU
# ================================

def vigenere_menu():

    while True:

        print("\n========== Vigenere Cipher ==========")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            text = input("Enter Plaintext: ")
            key = input("Enter Key: ")

            ciphertext = vigenere_encrypt(text, key)

            print("\nCiphertext:", ciphertext)

        elif choice == "2":

            text = input("Enter Ciphertext: ")
            key = input("Enter Key: ")

            plaintext = vigenere_decrypt(text, key)

            print("\nPlaintext:", plaintext)

        elif choice == "3":

            break

        else:

            print("Invalid Choice!")

# ===================================
# RAIL FENCE ENCRYPTION
# ===================================

def rail_fence_encrypt(text, rails):

    if rails <= 1:
        return text

    fence = ['' for _ in range(rails)]

    rail = 0
    direction = 1

    for char in text:

        fence[rail] += char

        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    return ''.join(fence)
# ===================================
# RAIL FENCE DECRYPTION
# ===================================

def rail_fence_decrypt(ciphertext, rails):

    if rails <= 1:
        return ciphertext

    pattern = []

    rail = 0
    direction = 1

    for _ in range(len(ciphertext)):
        pattern.append(rail)

        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    rail_counts = [pattern.count(i) for i in range(rails)]

    rails_data = []

    index = 0

    for count in rail_counts:
        rails_data.append(list(ciphertext[index:index + count]))
        index += count

    plaintext = ""

    for rail in pattern:
        plaintext += rails_data[rail].pop(0)

    return plaintext
# ===================================
# RAIL FENCE MENU
# ===================================

def rail_fence_menu():

    while True:

        print("\n========== Rail Fence Cipher ==========")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            text = input("Enter Plaintext: ")
            rails = int(input("Enter Number of Rails: "))

            ciphertext = rail_fence_encrypt(text, rails)

            print("\nCiphertext:", ciphertext)

        elif choice == "2":

            text = input("Enter Ciphertext: ")
            rails = int(input("Enter Number of Rails: "))

            plaintext = rail_fence_decrypt(text, rails)

            print("\nPlaintext:", plaintext)

        elif choice == "3":

            break

        else:

            print("Invalid Choice!")

# ===================================
# PLAYFAIR MATRIX
# ===================================

def generate_playfair_matrix(key):

    key = key.upper().replace("J", "I")

    matrix = []

    used = set()

    for char in key:

        if char.isalpha() and char not in used:

            matrix.append(char)

            used.add(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":

        if char not in used:

            matrix.append(char)

            used.add(char)

    matrix = [matrix[i:i + 5] for i in range(0, 25, 5)]

    return matrix
# ===================================
# FIND LETTER POSITION
# ===================================

def find_position(matrix, char):

    if char == 'J':
        char = 'I'

    for row in range(5):

        for col in range(5):

            if matrix[row][col] == char:

                return row, col
# ===================================
# PREPARE PLAYFAIR TEXT
# ===================================

def prepare_playfair_text(text):

    text = text.upper().replace("J", "I")
    text = "".join(char for char in text if char.isalpha())

    prepared = ""

    i = 0

    while i < len(text):

        first = text[i]

        if i + 1 < len(text):
            second = text[i + 1]
        else:
            second = "X"

        if first == second:

            prepared += first + "X"
            i += 1

        else:

            prepared += first + second
            i += 2

    if len(prepared) % 2 != 0:

        prepared += "X"

    return prepared
# ===================================
# PLAYFAIR ENCRYPTION
# ===================================

def playfair_encrypt(text, key):

    matrix = generate_playfair_matrix(key)

    text = prepare_playfair_text(text)

    ciphertext = ""

    for i in range(0, len(text), 2):

        first = text[i]
        second = text[i + 1]

        row1, col1 = find_position(matrix, first)
        row2, col2 = find_position(matrix, second)

        if row1 == row2:

            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]

        elif col1 == col2:

            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]

        else:

            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]

    return ciphertext
# ===================================
# PLAYFAIR DECRYPTION
# ===================================

def playfair_decrypt(ciphertext, key):

    matrix = generate_playfair_matrix(key)

    plaintext = ""

    for i in range(0, len(ciphertext), 2):

        first = ciphertext[i]
        second = ciphertext[i + 1]

        row1, col1 = find_position(matrix, first)
        row2, col2 = find_position(matrix, second)

        if row1 == row2:

            plaintext += matrix[row1][(col1 - 1) % 5]
            plaintext += matrix[row2][(col2 - 1) % 5]

        elif col1 == col2:

            plaintext += matrix[(row1 - 1) % 5][col1]
            plaintext += matrix[(row2 - 1) % 5][col2]

        else:

            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]

    return plaintext
# ===================================
# PLAYFAIR MENU
# ===================================

def playfair_menu():

    while True:

        print("\n========== Playfair Cipher ==========")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            text = input("Enter Plaintext: ")
            key = input("Enter Key: ")

            ciphertext = playfair_encrypt(text, key)

            print("\nCiphertext:", ciphertext)

        elif choice == "2":

            text = input("Enter Ciphertext: ")
            key = input("Enter Key: ")

            plaintext = playfair_decrypt(text, key)

            print("\nPlaintext:", plaintext)

        elif choice == "3":

            break

        else:

            print("Invalid Choice!")

# ===================================
# COLUMNAR ENCRYPTION
# ===================================

def columnar_encrypt(text, key):

    text = text.replace(" ", "").upper()

    cols = len(key)
    rows = (len(text) + cols - 1) // cols

    while len(text) < rows * cols:
        text += "X"

    matrix = []

    index = 0

    for i in range(rows):
        matrix.append(list(text[index:index + cols]))
        index += cols

    order = sorted(list(enumerate(key)), key=lambda x: x[1])

    ciphertext = ""

    for col_index, _ in order:

        for row in matrix:

            ciphertext += row[col_index]

    return ciphertext

# ===================================
# COLUMNAR DECRYPTION
# ===================================

def columnar_decrypt(ciphertext, key):

    cols = len(key)
    rows = len(ciphertext) // cols

    order = sorted(list(enumerate(key)), key=lambda x: x[1])

    matrix = [['' for _ in range(cols)] for _ in range(rows)]

    index = 0

    for col_index, _ in order:

        for row in range(rows):

            matrix[row][col_index] = ciphertext[index]
            index += 1

    plaintext = ""

    for row in matrix:

        plaintext += "".join(row)

    return plaintext.rstrip("X")

# ===================================
# COLUMNAR MENU
# ===================================

def columnar_menu():

    while True:

        print("\n========== Columnar Cipher ==========")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            text = input("Enter Plaintext: ")
            key = input("Enter Key: ")

            ciphertext = columnar_encrypt(text, key)

            print("\nCiphertext:", ciphertext)

        elif choice == "2":

            text = input("Enter Ciphertext: ")
            key = input("Enter Key: ")

            plaintext = columnar_decrypt(text, key)

            print("\nPlaintext:", plaintext)

        elif choice == "3":

            break

        else:

            print("Invalid Choice!")

# ===================================
# DOUBLE COLUMNAR ENCRYPTION
# ===================================

def double_columnar_encrypt(text, key1, key2):

    first = columnar_encrypt(text, key1)

    second = columnar_encrypt(first, key2)

    return second

# ===================================
# DOUBLE COLUMNAR DECRYPTION
# ===================================

def double_columnar_decrypt(ciphertext, key1, key2):

    first = columnar_decrypt(ciphertext, key2)

    second = columnar_decrypt(first, key1)

    return second

# ===================================
# DOUBLE COLUMNAR MENU
# ===================================

def double_columnar_menu():

    while True:

        print("\n========== Double Columnar Cipher ==========")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            text = input("Enter Plaintext: ")
            key1 = input("Enter First Key: ")
            key2 = input("Enter Second Key: ")

            ciphertext = double_columnar_encrypt(text, key1, key2)

            print("\nCiphertext:", ciphertext)

        elif choice == "2":

            text = input("Enter Ciphertext: ")
            key1 = input("Enter First Key: ")
            key2 = input("Enter Second Key: ")

            plaintext = double_columnar_decrypt(text, key1, key2)

            print("\nPlaintext:", plaintext)

        elif choice == "3":

            break

        else:

            print("Invalid Choice!")

# ===================================
# AFFINE ENCRYPTION
# ===================================

def affine_encrypt(text, a, b):

    result = ""

    for char in text:

        if char.isalpha():

            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            x = ord(char) - start

            encrypted = (a * x + b) % 26

            result += chr(encrypted + start)

        else:

            result += char

    return result


# ===================================
# MODULAR INVERSE
# ===================================

def mod_inverse(a):

    for i in range(26):

        if (a * i) % 26 == 1:

            return i

    return None

# ===================================
# AFFINE DECRYPTION
# ===================================

def affine_decrypt(text, a, b):

    result = ""

    a_inv = mod_inverse(a)

    if a_inv is None:

        return "Invalid Key! 'a' must be coprime with 26."

    for char in text:

        if char.isalpha():

            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            y = ord(char) - start

            decrypted = (a_inv * (y - b)) % 26

            result += chr(decrypted + start)

        else:

            result += char

    return result

# ===================================
# AFFINE MENU
# ===================================

def affine_menu():

    while True:

        print("\n========== Affine Cipher ==========")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            text = input("Enter Plaintext: ")
            a = int(input("Enter value of a: "))
            b = int(input("Enter value of b: "))

            ciphertext = affine_encrypt(text, a, b)

            print("\nCiphertext:", ciphertext)

        elif choice == "2":

            text = input("Enter Ciphertext: ")
            a = int(input("Enter value of a: "))
            b = int(input("Enter value of b: "))

            plaintext = affine_decrypt(text, a, b)

            print("\nPlaintext:", plaintext)

        elif choice == "3":

            break

        else:

            print("Invalid Choice!")

# ===================================
# BACONIAN ENCRYPTION
# ===================================

BACONIAN = {
    'A':'AAAAA','B':'AAAAB','C':'AAABA','D':'AAABB','E':'AABAA',
    'F':'AABAB','G':'AABBA','H':'AABBB','I':'ABAAA','J':'ABAAB',
    'K':'ABABA','L':'ABABB','M':'ABBAA','N':'ABBAB','O':'ABBBA',
    'P':'ABBBB','Q':'BAAAA','R':'BAAAB','S':'BAABA','T':'BAABB',
    'U':'BABAA','V':'BABAB','W':'BABBA','X':'BABBB','Y':'BBAAA',
    'Z':'BBAAB'
}

def baconian_encrypt(text):

    result = ""

    text = text.upper()

    for char in text:

        if char.isalpha():

            result += BACONIAN[char] + " "

        else:

            result += char

    return result.strip()

# ===================================
# BACONIAN DECRYPTION
# ===================================

def baconian_decrypt(ciphertext):

    reverse = {v: k for k, v in BACONIAN.items()}

    result = ""

    words = ciphertext.split()

    for code in words:

        if code in reverse:

            result += reverse[code]

        else:

            result += "?"

    return result

# ===================================
# BACONIAN MENU
# ===================================

def baconian_menu():

    while True:

        print("\n========== Baconian Cipher ==========")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            text = input("Enter Plaintext: ")

            ciphertext = baconian_encrypt(text)

            print("\nCiphertext:", ciphertext)

        elif choice == "2":

            text = input("Enter Ciphertext: ")

            plaintext = baconian_decrypt(text)

            print("\nPlaintext:", plaintext)

        elif choice == "3":

            break

        else:

            print("Invalid Choice!")

# ===================================
# BIFID MATRIX
# ===================================

def bifid_matrix(key):

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    key = key.upper().replace("J", "I")

    seen = ""

    for ch in key:

        if ch.isalpha() and ch not in seen:

            seen += ch

    for ch in alphabet:

        if ch not in seen:

            seen += ch

    matrix = []

    index = 0

    for i in range(5):

        matrix.append(list(seen[index:index+5]))

        index += 5

    return matrix

# ===================================
# FIND LETTER POSITION
# ===================================

def bifid_find(matrix, ch):

    ch = ch.replace("J", "I")

    for i in range(5):

        for j in range(5):

            if matrix[i][j] == ch:

                return i + 1, j + 1

# ===================================
# BIFID ENCRYPTION
# ===================================

def bifid_encrypt(text, key):

    matrix = bifid_matrix(key)

    text = text.upper().replace("J", "I")
    text = "".join(ch for ch in text if ch.isalpha())

    rows = []
    cols = []

    for ch in text:

        r, c = bifid_find(matrix, ch)

        rows.append(r)
        cols.append(c)

    numbers = rows + cols

    ciphertext = ""

    for i in range(0, len(numbers), 2):

        r = numbers[i]
        c = numbers[i + 1]

        ciphertext += matrix[r - 1][c - 1]

    return ciphertext

# ===================================
# BIFID DECRYPTION
# ===================================

def bifid_decrypt(ciphertext, key):

    matrix = bifid_matrix(key)

    coords = []

    for ch in ciphertext:

        r, c = bifid_find(matrix, ch)

        coords.append(r)
        coords.append(c)

    half = len(coords) // 2

    rows = coords[:half]
    cols = coords[half:]

    plaintext = ""

    for r, c in zip(rows, cols):

        plaintext += matrix[r - 1][c - 1]

    return plaintext

# ===================================
# BIFID MENU
# ===================================

def bifid_menu():

    while True:

        print("\n========== Bifid Cipher ==========")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            text = input("Enter Plaintext: ")
            key = input("Enter Key: ")

            ciphertext = bifid_encrypt(text, key)

            print("\nCiphertext:", ciphertext)

        elif choice == "2":

            text = input("Enter Ciphertext: ")
            key = input("Enter Key: ")

            plaintext = bifid_decrypt(text, key)

            print("\nPlaintext:", plaintext)

        elif choice == "3":

            break

        else:

            print("Invalid Choice!")

def main():

    while True:

        print("\n")
        print("=" * 50)
        print("          CRYPTOGRAPHY TOOLKIT")
        print("=" * 50)

        print("1. Caesar Cipher")
        print("2. Vigenere Cipher")
        print("3. Rail Fence Cipher")
        print("4. Playfair Cipher")
        print("5. Columnar Cipher")
        print("6. Double Columnar Cipher")
        print("7. Affine Cipher")
        print("8. Baconian Cipher")
        print("9. Bifid Cipher")
        print("10. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            caesar_menu()

        elif choice == "2":
            vigenere_menu()

        elif choice == "3":
            rail_fence_menu()

        elif choice == "4":
            playfair_menu()

        elif choice == "5":
            columnar_menu()

        elif choice == "6":
            double_columnar_menu()

        elif choice == "7":
            affine_menu()

        elif choice == "8":
            baconian_menu()

        elif choice == "9":
            bifid_menu()

        elif choice == "10":
            print("\nThank you!")
            break

        else:
            print("\nInvalid Choice!")


if __name__ == "__main__":
    main()