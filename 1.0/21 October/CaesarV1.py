def decrypt_char(char, key):
    return chr(ord('A') + (ord(char) - ord('A') + 26 - key) % 26)
def decrypt_message(key, ciper):
    cipher = cipher.upper()
    message = ''
    for char in cipher:
        if char not in ' ,.':
            message += decrypt_char(char, key)
        else:
            message += char
    return message
decrypt_message(str(int(input)), input())