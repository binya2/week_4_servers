def append_to_file(file_name, content):
    with open(file_name, 'a') as f:
        f.write(content + '\n')


def caesar_cipher(text: str, key: int):
    text_after_proses: str = ""
    for i in range(len(text)):
        if not text[i].isalpha():
            # If the character is not a letter
            text_after_proses += text[i]
            continue
        else:
            first_letter_in_ask: int = 97
            letter_after_process: int = (ord(text[i].lower()) + key - first_letter_in_ask) % 26
            text_after_proses += chr(letter_after_process + first_letter_in_ask)
    return text_after_proses


def fence_cipher_encrypt(text: str):
    # Hiding non-letter characters
    text_without_spaces = ''.join(filter(str.isalpha, text))
    even_row: str = ""
    odd_row: str = ""
    for index, char in enumerate(text_without_spaces):
        if index % 2 == 0:
            even_row += char
        else:
            odd_row += char

    return even_row + odd_row


def fence_cipher_decrypt(text: str):
    middle: int = (len(text) // 2) + 1
    part_1: str = text[:middle]
    part_2: str = text[middle:]
    part_1_size: int = len(part_1)
    part_2_size: int = len(part_2)
    result: str = ""
    i = 0
    j = 0
    for b in range(len(text)):
        if b % 2 == 0 and i < part_1_size:
            result += part_1[i]
            i += 1
        elif j < part_2_size:
            result += part_2[j]
            j += 1

    return result
