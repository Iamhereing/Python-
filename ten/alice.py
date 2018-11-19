filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    words = contents
