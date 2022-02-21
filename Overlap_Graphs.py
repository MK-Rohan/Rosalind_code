import sys

data = """
"""

id_lst = list()
seq_lst = list()
tmp = str()

##### id, sequence split #####
for line in data.strip().split("\n"):
    if line.startswith(">"):
        if len(tmp) > 1:
            seq_lst.append(tmp)
            tmp = str()
        id_lst.append(line[1:])
    else:
        tmp += line
seq_lst.append(tmp)

##### overlap check #####
for i, k in enumerate(seq_lst):
    for j, l in enumerate(seq_lst):
        if k == l:
            continue
        elif k[-3:] == l[:3]:
            print(id_lst[i] + " " + id_lst[j])
