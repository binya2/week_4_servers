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
            new_letter_ack = ord(text[i].lower()) + key
            if new_letter_ack > 122:
                new_letter_ack = new_letter_ack - 26
            if new_letter_ack < 97:
                new_letter_ack = new_letter_ack + 26
            text_after_proses += chr(new_letter_ack)
    return text_after_proses
