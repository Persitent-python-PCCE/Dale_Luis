def parse_line(line):
    li = line.split(" ")
    level = li[2]
    message = " ".join(li[3:])
    return (level, message)


def read_logs(path):
    entries=[]
    with open(path,"r") as f:
        reader=f.read()
        for i in reader.splitlines():
            entries.append(parse_line(i))

        return entries
        


