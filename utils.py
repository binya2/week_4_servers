def append_to_file(file_name, content):
    with open(file_name, 'a') as f:
        f.write(content)


def caesar_cipher(text: str, key: int):
    text_after_proses: str = ""
    for i in range(len(text)):
        if not text[i].isalpha():
            text_after_proses += text[i]
            continue
        else:
            first_letter_in_ask: int = 97
            letter_after_process: int = (ord(text[i].lower())+ key - first_letter_in_ask) % 26
            text_after_proses += chr(letter_after_process + first_letter_in_ask)
    return text_after_proses




def fence_cipher():
    pass

