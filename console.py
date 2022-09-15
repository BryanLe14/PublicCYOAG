import time

def log(*args):
    # https://thispointer.com/how-to-append-text-or-lines-to-a-file-in-python/
    # Open the file in append & read mode ('a+')
    with open("log.txt", "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0 :
            file_object.write("\n")
        # Append text at the end of file
        file_object.write("".join(args))

def clear(txt=""):
    with open("log.txt", "w") as f:
        f.write(txt)