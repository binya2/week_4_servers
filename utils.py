
def append_to_file(file_name, content):
    with open(file_name, 'a') as f:
        f.write(content)