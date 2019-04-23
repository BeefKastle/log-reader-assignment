out = open("log-output.txt", 'w+')

for line in open("samplefile", "r"):
    stuff = line.split(" ")
    print(stuff[8])
    if stuff[8] == "403" or stuff[8] == "404":
        if "GET" in stuff[5]:
            out.write(line)
