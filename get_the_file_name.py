example = "C:/Projects/pil_tests/ascii/edabit.txt"
example2 = "ffprobe.exe"


def get_filename(path):
    ext = path.split("/")
    print(ext)
    print(ext[-1])


get_filename(example)
