from pathlib import Path


path = Path(Path(__file__).parent, "source.md")
tocs = []

with open(path, "rt") as f:
    while True:
        line = f.readline()

        if line == "":
            break

        elif line.startswith("#"):
            tabs = -1
            for c in line:
                if c == "#":
                    tabs+=1
            
            tocs.append("\t"*tabs + line)

print(tocs)

with open(path, "at") as f:
    f.writelines(tocs)