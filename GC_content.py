sequence = """ FASTQ sequence """
rosa = dict()
tmp_id = str()
line_n = 0
for line in sequence.strip().split("\n"):
    if line.startswith(">"):
        line_n += 1
        if not tmp_id:
            tmp_id = line[line.find(">")+1:]
            rosa[tmp_id] = ""
        else:
            tmp_id = line[line.find(">")+1:]
            rosa[tmp_id] = ""
    elif not line:
        continue
    else:
        rosa[tmp_id] += line

GC_percent = list()
perc = dict()
ma = list()
for i in list(rosa.keys()):
    tot = 0
    gc = 0
    for j in list(rosa[i]):
        tot += 1
        if j == "G" or j == "C":
            gc += 1
    perc[i] = gc/tot*100
    ma.append(gc/tot*100)

for key, value in perc.items():
    if value == max(ma):
        print(key)
        print(value)
