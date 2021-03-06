import sys

from processor import Processor

def ingest_file(file):
    pitch = Processor()
    i = 0
    with open(file) as f:
        content = f.readlines()
        for line in content:
            pitch.parse(line)
            i += 1
        return pitch.print_top_symbols()
        
def terminal_input():
    continue_input = True
    pitch = Processor()
    while continue_input:
        op = input("Enter operation [Q to quit]: ")
        if op == "Q":
            return
        pitch.parse(op)
        pitch.print_top_symbols()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        ingest_file(sys.argv[1])