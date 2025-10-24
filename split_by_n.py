import os

def split_by_n(fname, n=3):
    '''
    Split files into sub files of near same size
    fname : Input file name
    n is the number of segments
    '''
    encoding="utf-8"
    total_size = os.path.getsize(fname)
    single_file_size = total_size // n 

    with open(fname, "r", encoding=encoding, newline="") as input_file:
        for i in range(n):
            out_name = f"{fname}_{i:03d}.txt"
            current_size = 0
            with open(out_name, "w", encoding=encoding, newline="") as out:
                while current_size < single_file_size:
                    line = input_file.readline()
                    if not line:
                        return True
                    out.write(line)
                    current_size += len(line.encode(encoding))
    return True

if __name__ == "__main__":
    print(split_by_n("pg5200.txt", 3))
    print(os.path.getsize("pg5200.txt_000.txt"))
    print(os.path.getsize("pg5200.txt_001.txt"))
    print(os.path.getsize("pg5200.txt_002.txt"))
