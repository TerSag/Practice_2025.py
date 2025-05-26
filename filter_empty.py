import sys

if __name__ == "__main__":
    for line in sys.stdin:
        if line.rstrip():
            sys.stdout.write(line)