from os.path import exists
def load_a_file(path : str, load_str : bool = False) -> object:
    v = ''
    if exists(path):
        with open(path, 'r') as f:
            v = f.read()
            if not load_str:
                v = int(v)
    return v
def write_on_a_file(path : str, text : str):
    with open(path, 'w') as f:
        f.write(text)
def append_to_a_file(path : str, text : str):
    with open(path, 'a') as f:
        f.write(text)